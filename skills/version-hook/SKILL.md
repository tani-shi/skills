---
name: version-hook
description: >
  Set up a git pre-commit hook that auto-updates version strings using date-based versioning (yyyy.mm.dd).
  Use when the user wants automatic version bumping on commit, date-based versioning,
  or a pre-commit hook for version management.
  Trigger on: "version hook", "auto version", "version bump", "pre-commit version",
  "date-based version", "auto-update version", "set up version hook",
  or any request to automatically update version strings on git commit.
---

# version-hook — Auto-Update Version on Commit

Generate and install a git pre-commit hook that automatically updates version strings using date-based versioning.

## Version Format

- **Base**: `yyyy.mm.dd` (e.g., `2026.03.13`)
- **Same-day increments**: `yyyy.mm.dd.N` where N starts at 1 (e.g., `2026.03.13.1`, `2026.03.13.2`)
- If the current version already matches today's date with a suffix, increment N
- If the current version is exactly today's date, append `.1`
- Otherwise, set to today's date

## Workflow

### Step 1: Analyze the project

Examine the project root to determine:
- Language/ecosystem (Node.js, Python, Rust, Go, Swift, Java, etc.)
- Whether it is a monorepo (workspaces, lerna, turborepo, Cargo workspaces, etc.)
- Which files contain a `version` field that should be auto-updated
- Whether an existing pre-commit hook or hook framework (husky, lefthook, pre-commit) is in place

### Step 2: Identify version files

Find all files containing version strings. Use the pattern reference below to determine which files and fields to target.

**Important distinctions — what to update vs. skip:**

| Update | Skip |
|--------|------|
| The project's own version field | Dependency version constraints |
| Root-level or package-level version | Lock files (`package-lock.json`, `Cargo.lock`, `poetry.lock`, etc.) |
| Manifest version fields | Version fields inside `[dependencies]`, `[dev-dependencies]`, etc. |
| | `parent` version in `pom.xml` |
| | Generated or vendored files |

### Step 3: Confirm with user

Before generating the hook, present:
- The list of files and fields that will be updated
- For monorepos: whether to update only changed packages or the root version
- Any existing hook that will be modified

Wait for user confirmation before proceeding.

### Step 4: Generate and install the hook

Generate the pre-commit hook script and install it. Follow the hook generation rules below.

## Hook Generation Rules

### Structure

The generated hook MUST follow this structure:

```sh
#!/bin/sh

# --- version-hook: start ---
(
  __vh_compute_version() {
    CURRENT="$1"
    TODAY=$(date +"%Y.%m.%d")
    if echo "$CURRENT" | grep -q "^${TODAY}\.[0-9][0-9]*$"; then
      N=$(echo "$CURRENT" | sed "s/^${TODAY}\.\([0-9][0-9]*\)$/\1/")
      echo "${TODAY}.$((N + 1))"
    elif [ "$CURRENT" = "$TODAY" ]; then
      echo "${TODAY}.1"
    else
      echo "$TODAY"
    fi
  }

  # ... per-file update logic here ...

) || true
# --- version-hook: end ---
```

### Rules

1. **Wrap in subshell with `|| true`**: The hook must never block a commit. All logic goes inside `( ... ) || true`.
2. **Marker comments**: Use `# --- version-hook: start ---` and `# --- version-hook: end ---` to delimit the hook's section. This allows coexistence with other hook content.
3. **Common version function**: Always define `__vh_compute_version` once and reuse it for all files.
4. **Cross-platform `sed -i`**: macOS `sed` requires `sed -i ''` while GNU `sed` uses `sed -i`. Use this wrapper:
   ```sh
   __vh_sed_i() {
     if sed --version 2>/dev/null | grep -q GNU; then
       sed -i "$@"
     else
       sed -i '' "$@"
     fi
   }
   ```
5. **Stage updated files**: After each file is modified, run `git add <file>` to include the change in the commit.
6. **Check staging**: Only update version files that have other staged changes in the same package/directory. Use `git diff --cached --name-only` to determine what is staged.
7. **Existing hooks**: If a pre-commit hook already exists, insert the version-hook block using marker comments. Do not overwrite existing content.
8. **Hook frameworks**: If the project uses husky, lefthook, or similar:
   - **husky**: Add to `.husky/pre-commit`
   - **lefthook**: Add to `lefthook.yml` under `pre-commit.commands`
   - **pre-commit (Python)**: Add as a `local` hook in `.pre-commit-config.yaml`
   - Fall back to `.git/hooks/pre-commit` if no framework is detected
9. **Make executable**: Run `chmod +x` on the hook file after writing.

## Version File Patterns

Reference for locating and updating version strings per ecosystem.

### Node.js / JavaScript / TypeScript

| File | sed pattern |
|------|-------------|
| `package.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

For monorepos, check `workspaces` in root `package.json` or `lerna.json` / `pnpm-workspace.yaml`.

### Python

| File | sed pattern |
|------|-------------|
| `pyproject.toml` | `s/^version = "[^"]*"/version = "NEW"/` (under `[project]` or `[tool.poetry]`) |
| `setup.cfg` | `s/^version = .*/version = NEW/` (under `[metadata]`) |
| `__version__.py` or `_version.py` | `s/__version__ = "[^"]*"/__version__ = "NEW"/` |
| `setup.py` | `s/version="[^"]*"/version="NEW"/` |

### Rust

| File | sed pattern | Notes |
|------|-------------|-------|
| `Cargo.toml` | `s/^version = "[^"]*"/version = "NEW"/` | Only under `[package]`, NOT under `[dependencies]` |

For Cargo workspaces, check `[workspace]` members in root `Cargo.toml`. Use a flag or line-range approach to target only `[package].version`:
```sh
awk '/^\[package\]/{p=1} /^\[/{if(!/\[package\]/)p=0} p && /^version = /{sub(/"[^"]*"/, "\"NEW\""); print; next} {print}' Cargo.toml > Cargo.toml.tmp && mv Cargo.toml.tmp Cargo.toml
```

### Go

| File | sed pattern |
|------|-------------|
| `version.go` or similar | `s/Version = "[^"]*"/Version = "NEW"/` |

Go modules don't have a manifest version. Look for a `version.go` or constant declaration.

### Java / Kotlin

| File | Tool/pattern | Notes |
|------|-------------|-------|
| `pom.xml` | `s|<version>OLD</version>|<version>NEW</version>|` | Only the project's own `<version>`, not `<parent>` or dependency versions. Target the first occurrence or use xpath. |
| `build.gradle` / `build.gradle.kts` | `s/version = "[^"]*"/version = "NEW"/` or `s/version '[^']*'/version 'NEW'/` | |

### Swift / Apple

| File | Tool | Notes |
|------|------|-------|
| `Info.plist` | `/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString NEW" Info.plist` | Use PlistBuddy, not sed |
| `.xcconfig` | `s/MARKETING_VERSION = .*/MARKETING_VERSION = NEW/` | |
| `Package.swift` | Usually no version field | |

### Ruby

| File | sed pattern |
|------|-------------|
| `*.gemspec` | `s/\.version *= *"[^"]*"/.version = "NEW"/` |
| `lib/*/version.rb` | `s/VERSION = "[^"]*"/VERSION = "NEW"/` |

### PHP

| File | sed pattern |
|------|-------------|
| `composer.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

### .NET / C#

| File | sed pattern |
|------|-------------|
| `*.csproj` | `s|<Version>.*</Version>|<Version>NEW</Version>|` |
| `Directory.Build.props` | Same as above |

### Claude Code Plugin

| File | sed pattern |
|------|-------------|
| `marketplace.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

### Generic / Other

| File | sed pattern |
|------|-------------|
| `VERSION` or `VERSION.txt` | Replace entire file content |
| `version.txt` | Replace entire file content |
| Custom config (YAML/JSON/TOML) | Adapt pattern to match the version field |

## Monorepo Strategy

When a monorepo is detected:

1. **Identify workspace structure**: Check for workspace config files (`pnpm-workspace.yaml`, `lerna.json`, `Cargo.toml [workspace]`, etc.)
2. **Ask the user** which strategy to use:
   - **Changed packages only**: Update version only in packages that have staged changes
   - **Root only**: Update only the root version file
   - **All packages**: Update all packages on every commit
3. **Implement staging check**: For "changed packages only", use `git diff --cached --name-only` to detect which packages have changes and only update those.

## Checklist

- [ ] Project analyzed: language, ecosystem, monorepo status
- [ ] Version files identified and confirmed with user
- [ ] Existing hook/framework detected
- [ ] Hook generated following all rules
- [ ] Hook installed and made executable
- [ ] Tested with a dry run (`git stash && git stash pop` or similar)
