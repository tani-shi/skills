---
name: cli-inspector
description: >
  Investigate CLI tools by discovering their full command trees and inspecting their source repos.
  Use when the user wants to understand what a CLI tool can do, explore its subcommands,
  see its command hierarchy, or learn how a CLI works internally.
  Trigger on: "what commands does X have", "show me the subcommands", "how does this CLI work",
  "explore this CLI", "what can X do", discovering available commands of any CLI tool,
  or mentions "cli-inspector".
  Also trigger when the user provides a CLI tool name and wants to know its capabilities.
---

# cli-inspector — Investigate CLI Tools

Discover the full command tree and source code details of any CLI tool. Pass the results to skill-creator to generate a skill.

## Workflow

### Step 1: Discover the CLI command tree

```bash
uv run skills/cli-inspector/scripts/discover_cli.py <cli-name> [--max-depth 3] [--help-flag "--help"]
```

This recursively runs `--help` on all subcommands and outputs a JSON command tree with commands, arguments, flags, and descriptions.

### Step 2: Extract version info from the repo

```bash
uv run skills/cli-inspector/scripts/inspect_repo.py <repo-path>
```

Outputs commit hash, branch, version tag, commit date, and remote URL.

### Step 3: Read source code for supplementary details

Browse the CLI's source code to find information not captured by `--help`:
- Environment variables (e.g., API keys, config paths)
- Authentication methods and setup steps
- Output format details (JSON structure, special fields)
- Date/time input format expectations
- Error handling and edge cases

## Investigation checklist

A complete investigation should capture:

- [ ] Full command tree (all subcommands, arguments, and flags)
- [ ] Version info (commit hash, tag, branch, date, remote URL)
- [ ] Global flags that apply to all subcommands
- [ ] Environment variables and config file paths
- [ ] Authentication setup requirements
- [ ] Output formats and their structure
- [ ] Input format expectations (dates, IDs, etc.)
- [ ] Notable edge cases or gotchas from source code

## Passing results to skill-creator

Once the investigation is complete, hand off the collected data (command tree JSON, repo info, source code notes) to `skill-creator` to generate the actual skill files.
