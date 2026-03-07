#!/usr/bin/env python3
"""SKILL.md parser utilities."""

import re
from pathlib import Path


def parse_skill_md(skill_dir: str | Path) -> dict:
    """Parse a SKILL.md file and extract frontmatter fields.

    Args:
        skill_dir: Path to the skill directory containing SKILL.md.

    Returns:
        Dict with parsed frontmatter fields (name, description, etc.)
        and 'body' containing the content after frontmatter.

    Raises:
        FileNotFoundError: If SKILL.md does not exist.
        ValueError: If SKILL.md has no valid YAML frontmatter.
    """
    skill_dir = Path(skill_dir)
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        raise FileNotFoundError(f"SKILL.md not found in {skill_dir}")

    content = skill_md.read_text(encoding="utf-8")

    # Extract YAML frontmatter between --- delimiters
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n?(.*)", content, re.DOTALL)
    if not m:
        raise ValueError(f"No valid YAML frontmatter found in {skill_md}")

    frontmatter_text = m.group(1)
    body = m.group(2)

    # Parse YAML fields (simple key: value and key: >\n  multiline)
    fields: dict[str, str] = {}
    current_key = None
    current_value_lines: list[str] = []
    is_multiline = False

    for line in frontmatter_text.splitlines():
        # Check for a new key
        key_match = re.match(r"^(\w[\w-]*)\s*:\s*(.*)", line)
        if key_match:
            # Save previous key if any
            if current_key is not None:
                if is_multiline:
                    fields[current_key] = " ".join(current_value_lines).strip()
                else:
                    fields[current_key] = current_value_lines[0] if current_value_lines else ""
                current_value_lines = []

            current_key = key_match.group(1)
            value = key_match.group(2).strip()

            if value == ">":
                is_multiline = True
            else:
                is_multiline = False
                current_value_lines = [value]
        elif current_key and is_multiline:
            stripped = line.strip()
            if stripped:
                current_value_lines.append(stripped)

    # Save last key
    if current_key is not None:
        if is_multiline:
            fields[current_key] = " ".join(current_value_lines).strip()
        else:
            fields[current_key] = current_value_lines[0] if current_value_lines else ""

    return {**fields, "_body": body}
