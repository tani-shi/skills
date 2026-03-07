---
name: cli-skill-creator
description: >
  Automate creating Claude Code skills for CLI tools. Takes a CLI name and git repo path,
  discovers commands via recursive --help execution, reads source code for supplementary details,
  extracts version info, and generates a complete skill with SKILL.md and reference files.
  Trigger when the user asks to create a skill for a CLI tool, generate CLI documentation as a skill,
  or mentions "cli-skill-creator".
---

# cli-skill-creator — Generate Skills from CLI Tools

Create a complete Claude Code skill for any CLI tool by discovering its commands and reading its source code.

## Workflow

### Step 1: Discover the CLI command tree

```bash
uv run skills/cli-skill-creator/scripts/discover_cli.py <cli-name> [--max-depth 3] [--help-flag "--help"]
```

This recursively runs `--help` on all subcommands and outputs a JSON command tree with commands, arguments, flags, and descriptions.

### Step 2: Extract version info from the repo

```bash
uv run skills/cli-skill-creator/scripts/inspect_repo.py <repo-path>
```

Outputs commit hash, branch, version tag, commit date, and remote URL.

### Step 3: Read source code for supplementary details

Browse the CLI's source code to find information not captured by `--help`:
- Environment variables (e.g., API keys, config paths)
- Authentication methods and setup steps
- Output format details (JSON structure, special fields)
- Date/time input format expectations
- Error handling and edge cases

### Step 4: Generate the skill

Using the JSON command tree, version info, and source code insights, generate:

1. **SKILL.md** — Following the template in [references/cli-skill-template.md](references/cli-skill-template.md):
   - Frontmatter with name and description (include trigger conditions)
   - Version line: `Built from <cli> <version-tag> (<commit-hash-short>, <commit-date>)`
   - Global flags section
   - Output handling section
   - Reference file index with links
   - Common usage patterns

2. **Reference files** — One per top-level subcommand (or grouped if >15 subcommands):
   - Command syntax with all arguments and flags
   - Flag descriptions with types, defaults, and required markers
   - Practical examples

### Step 5: Validate

1. Run the SKILL.md validator to check frontmatter structure:

```bash
uv run skills/cli-skill-creator/scripts/quick_validate.py skills/<cli-name>
```

2. Pick 2-3 commands and verify the generated documentation matches `--help` output.

## Updating an existing skill

To check if a skill needs updating:
1. Run `inspect_repo.py` on the CLI's repo
2. Compare the commit hash with the version recorded in SKILL.md
3. If different, re-run `discover_cli.py` and diff against existing references
4. Update only the changed reference files and the version line in SKILL.md

## Output location

Generated skills are placed in:
```
skills/<cli-name>/
├── SKILL.md
└── references/
    ├── <command1>.md
    ├── <command2>.md
    └── ...
```

## Reference

- [CLI Skill Template](references/cli-skill-template.md) — Structure and formatting rules for generated skills
