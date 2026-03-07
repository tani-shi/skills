#!/usr/bin/env python3
"""Discover CLI command tree by recursively executing --help."""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone


def strip_rich_formatting(text: str) -> str:
    """Strip Rich/Typer box-drawing characters and ANSI escape codes."""
    # Remove ANSI escape codes
    text = re.sub(r"\x1b\[[0-9;]*m", "", text)
    # Remove box-drawing characters (╭╮╰╯│─)
    text = re.sub(r"[╭╮╰╯─]", "", text)
    text = text.replace("│", " ")
    # Collapse multiple spaces but preserve leading indentation structure
    lines = []
    for line in text.splitlines():
        # Strip trailing whitespace
        line = line.rstrip()
        lines.append(line)
    return "\n".join(lines)


def run_help(cli_parts: list[str], help_flag: str = "--help") -> str | None:
    """Run a CLI command with --help and return the output text."""
    cmd = cli_parts + [help_flag]
    env = dict(__import__("os").environ)
    # Disable Rich formatting for cleaner output
    env["NO_COLOR"] = "1"
    env["TERM"] = "dumb"
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=10, env=env
        )
        # Some CLIs print help to stderr
        output = result.stdout or result.stderr
        if output and result.returncode in (0, 1, 2):
            return strip_rich_formatting(output.strip())
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass

    # Fallback to -h if --help failed
    if help_flag == "--help":
        return run_help(cli_parts, "-h")
    return None


def parse_flags(lines: list[str]) -> list[dict]:
    """Parse flag/option lines from help output."""
    flags = []
    # Match lines like: -s, --long VALUE   description
    #                    --long VALUE       description
    #                    -s                 description
    flag_re = re.compile(
        r"^\s+"
        r"(?:(-\w),?\s*)?"       # optional short flag
        r"(--[\w][\w-]*)"        # long flag
        r"(?:\s+(\S+))?"         # optional value placeholder
        r"\s{2,}(.+)?$"          # description (2+ spaces before it)
    )
    # Also match short-only flags: -s VALUE  description
    short_only_re = re.compile(
        r"^\s+(-\w)"
        r"(?:\s+(\S+))?"
        r"\s{2,}(.+)?$"
    )

    i = 0
    while i < len(lines):
        line = lines[i]
        m = flag_re.match(line)
        if m:
            short, long, value_type, desc = m.groups()
            desc = (desc or "").strip()
            # Check for continuation lines
            while i + 1 < len(lines) and lines[i + 1].startswith("          ") and not flag_re.match(lines[i + 1]) and not short_only_re.match(lines[i + 1]):
                i += 1
                desc += " " + lines[i].strip()

            required = False
            default = None
            if desc:
                req_match = re.search(r"\(required\)", desc, re.IGNORECASE)
                if req_match:
                    required = True
                def_match = re.search(r"\(default[:\s]+([^)]+)\)", desc, re.IGNORECASE)
                if not def_match:
                    def_match = re.search(r"\[default[:\s]+([^\]]+)\]", desc, re.IGNORECASE)
                if def_match:
                    default = def_match.group(1).strip()

            flags.append({
                "name": long,
                "short": short,
                "value_type": value_type,
                "required": required,
                "default": default,
                "description": desc,
            })
        else:
            m2 = short_only_re.match(line)
            if m2:
                short, value_type, desc = m2.groups()
                flags.append({
                    "name": short,
                    "short": short,
                    "value_type": value_type,
                    "required": False,
                    "default": None,
                    "description": (desc or "").strip(),
                })
        i += 1
    return flags


def parse_arguments(lines: list[str]) -> list[dict]:
    """Parse positional argument lines from help output."""
    args = []
    arg_re = re.compile(r"^\s+(<[^>]+>|[A-Z][A-Z_]+|\[[\w.]+\])\s{2,}(.+)$")
    for line in lines:
        m = arg_re.match(line)
        if m:
            name, desc = m.groups()
            required = not (name.startswith("[") and name.endswith("]"))
            # Strip angle brackets
            clean_name = name.strip("<>[]")
            args.append({
                "name": clean_name,
                "required": required,
                "description": desc.strip(),
            })
    return args


def is_section_header(line: str) -> str | None:
    """Check if a line is a section header. Returns the section name or None."""
    # "Commands:" or "Options:" (with optional leading whitespace, optional colon)
    m = re.match(
        r"^\s*(commands|subcommands|available commands|options|flags|"
        r"global options|global flags|arguments|args|positional arguments|usage)\s*:?\s*$",
        line,
        re.IGNORECASE,
    )
    if m:
        return m.group(1).strip().lower()
    return None


def extract_subcommand_names(help_text: str) -> list[str]:
    """Extract subcommand names from help text."""
    subcommands = []
    in_commands_section = False
    command_section_names = {"commands", "subcommands", "available commands"}

    for line in help_text.splitlines():
        header = is_section_header(line)
        if header:
            in_commands_section = header in command_section_names
            continue

        if in_commands_section:
            stripped = line.strip()
            if not stripped:
                continue

            # Kong/cobra format: "  cmd (aliases) <args> [flags]"
            # Description follows on a deeper-indented line — skip those
            m_kong = re.match(r"^  ([\w][\w-]*)\s", line)
            if m_kong and not line.startswith("    "):
                cmd_name = m_kong.group(1)
                if cmd_name.lower() not in ("help", "completion"):
                    subcommands.append(cmd_name)
                continue

            # Typer/Click format: "  command-name   description" (same line)
            m = re.match(r"^\s{2,}([\w][\w-]*)\s{2,}(.+)$", line)
            if m:
                cmd_name = m.group(1)
                if cmd_name.lower() not in ("help", "completion"):
                    subcommands.append(cmd_name)
                continue

            # Skip description lines (4+ leading spaces) and other continuation
            if line.startswith("    "):
                continue

    return subcommands


def extract_description(help_text: str) -> str:
    """Extract the main description from help text."""
    lines = help_text.splitlines()
    desc_lines = []

    for line in lines:
        stripped = line.strip()
        # Skip empty lines at the start
        if not stripped and not desc_lines:
            continue
        # Stop at first section header or usage line
        if re.match(r"^(usage|commands|options|flags|arguments|available):", stripped, re.IGNORECASE):
            break
        if stripped.startswith("Usage:") or stripped.startswith("usage:"):
            break
        if desc_lines and not stripped:
            break
        desc_lines.append(stripped)

    return " ".join(desc_lines).strip()


def split_sections(help_text: str) -> dict[str, list[str]]:
    """Split help text into named sections."""
    sections: dict[str, list[str]] = {"_header": []}
    current = "_header"

    for line in help_text.splitlines():
        header = is_section_header(line)
        if header:
            current = header
            sections[current] = []
        else:
            # Also try traditional "Word:" format
            m = re.match(r"^(\w[\w\s]*):\s*$", line)
            if m:
                current = m.group(1).strip().lower()
                sections[current] = []
            else:
                sections.setdefault(current, []).append(line)

    return sections


def discover_command(
    cli_parts: list[str],
    help_flag: str,
    max_depth: int,
    depth: int = 0,
) -> dict | None:
    """Recursively discover a command and its subcommands."""
    help_text = run_help(cli_parts, help_flag)
    if not help_text:
        return None

    command_name = " ".join(cli_parts)
    sections = split_sections(help_text)

    # Get description
    description = extract_description(help_text)

    # Parse flags from options/flags sections
    flag_lines = []
    for key in ("options", "flags", "global options", "global flags"):
        if key in sections:
            flag_lines.extend(sections[key])
    flags = parse_flags(flag_lines)

    # Parse arguments
    arg_lines = []
    for key in ("arguments", "args", "positional arguments"):
        if key in sections:
            arg_lines.extend(sections[key])
    arguments = parse_arguments(arg_lines)

    node = {
        "command": command_name,
        "description": description,
        "arguments": arguments,
        "flags": flags,
        "subcommands": [],
    }

    # Discover subcommands if within depth limit
    if depth < max_depth:
        subcmd_names = extract_subcommand_names(help_text)
        for name in subcmd_names:
            child = discover_command(
                cli_parts + [name], help_flag, max_depth, depth + 1
            )
            if child:
                node["subcommands"].append(child)

    return node


def main():
    parser = argparse.ArgumentParser(
        description="Discover CLI command tree by recursively executing --help"
    )
    parser.add_argument("cli", help="CLI command name to discover")
    parser.add_argument(
        "--max-depth",
        type=int,
        default=3,
        help="Maximum recursion depth for subcommands (default: 3)",
    )
    parser.add_argument(
        "--help-flag",
        default="--help",
        help="Help flag to use (default: --help)",
    )
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    tree = discover_command([args.cli], args.help_flag, args.max_depth)
    if not tree:
        print(f"Error: Could not get help output from '{args.cli}'", file=sys.stderr)
        sys.exit(1)

    result = {
        "cli": args.cli,
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "tree": tree,
    }

    output = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
