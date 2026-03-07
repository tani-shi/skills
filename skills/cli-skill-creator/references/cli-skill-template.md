# CLI Skill Template

This template defines the structure for generated CLI skills. Follow these patterns when producing SKILL.md and reference files.

## SKILL.md structure

```markdown
---
name: <cli-name>
description: >
  Use the `<cli-name>` CLI to <purpose>.
  Trigger when <trigger conditions>.
  Also trigger when the user mentions "<cli-name>", <aliases>, or similar terms
  in the context of performing actions (not just discussing them).
---

# <cli-name> — <short title>

Use the `<cli-name>` command to <what it does>. The CLI is already installed and authenticated.

Built from <cli-name> <version-tag> (<commit-hash-short>, <commit-date>)

## Global flags

- `--flag` — description

## Output handling

<Describe default output format and how to get machine-readable output>

## Command reference files

Load the relevant reference file based on which command the user needs:

- **<Command>** (<keywords>): See [references/<command>.md](references/<command>.md)

## Common patterns

### <Pattern name>

<Description and example>
```

## Reference file structure

Each reference file covers one top-level subcommand (or a logical group):

```markdown
# <Command Name>

## <Subcommand>

\`\`\`bash
<cli> <command> <subcommand> <args> [flags]
\`\`\`

<Description of what this does>

- `--flag VALUE` — description
- `--another` — description

## Examples

\`\`\`bash
# Short description of what this example does
<cli> <command> <subcommand> --flag value
\`\`\`
```

## Grouping rules

- If the CLI has 15 or fewer top-level subcommands: one reference file per subcommand
- If the CLI has more than 15 top-level subcommands: group related commands into logical files
- Auth/config commands should always be in a separate reference file

## Version tracking

Format: `Built from <cli> <version-tag> (<commit-hash-short>, <commit-date>)`

Example: `Built from gog v0.3.1 (abc123d, 2026-03-07)`

To check if a skill needs updating:
1. Compare the stored commit hash with the repo's current HEAD
2. If different, re-run discover_cli.py
3. Diff the new tree against the existing references
4. Update only the changed reference files

## Content guidelines

- Include information not available in --help when found in source code:
  - Environment variables
  - Authentication methods
  - Output format details
  - Date/time input formats
  - Error handling behavior
- Keep descriptions concise — one line per flag/argument
- Use backticks for all CLI commands, flags, and values
- Show practical examples that demonstrate common use cases
