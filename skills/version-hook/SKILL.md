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

**Important distinctions — what to update, regenerate, or skip:**

| Update (sed) | Regenerate (package manager) | Skip |
|--------------|------------------------------|------|
| The project's own version field | `uv.lock` (if exists & `uv` available) | `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml` (npm/yarn/pnpm auto-update) |
| Root-level or package-level version | `poetry.lock` (if exists & `poetry` available) | Dependency version constraints |
| Manifest version fields | `Cargo.lock` (if exists & `cargo` available) | Version fields inside `[dependencies]`, `[dev-dependencies]`, etc. |
| | | `parent` version in `pom.xml` |
| | | Generated or vendored files |

### Step 3: Confirm with user

Before generating the hook, present:
- The list of files and fields that will be updated
- For monorepos: whether to update only changed packages or the root version
- Any existing hook that will be modified

Wait for user confirmation before proceeding.

### Step 4: Generate and install the hook

Generate the pre-commit hook script and install it. Follow the hook generation rules below.

### Step 5: Verify (required)

After installing the hook, run these verification substeps. Do NOT skip this step.

#### 5a. Syntax & quality check

Run `shellcheck <hook-file>` to detect syntax errors and semantic issues. If shellcheck is not available, fall back to `sh -n <hook-file>` for basic syntax validation. Fix any errors before proceeding.

#### 5b. Version computation test

Source the hook file to extract `__vh_compute_version`, then verify with three test cases:

```sh
# Test 1: Past date → today's date
result=$(__vh_compute_version "2020.01.01")
expected=$(date +"%Y.%m.%d")
[ "$result" = "$expected" ] && echo "PASS" || echo "FAIL: got $result, expected $expected"

# Test 2: Today's date → today.1
result=$(__vh_compute_version "$(date +%Y.%m.%d)")
expected="$(date +%Y.%m.%d).1"
[ "$result" = "$expected" ] && echo "PASS" || echo "FAIL: got $result, expected $expected"

# Test 3: today.3 → today.4
result=$(__vh_compute_version "$(date +%Y.%m.%d).3")
expected="$(date +%Y.%m.%d).4"
[ "$result" = "$expected" ] && echo "PASS" || echo "FAIL: got $result, expected $expected"
```

All three must pass. If any fails, fix the `__vh_compute_version` function and re-test.

#### 5c. sed pattern dry-run

For each target version file, run the sed command in dry-run mode (output to stdout, do not modify the file) and verify the version string is actually replaced. For example:

```sh
# For a file using: s/"version": *"[^"]*"/"version": "TEST"/
sed 's/"version": *"[^"]*"/"version": "TEST"/' package.json | grep '"version"'
# Confirm the output shows "version": "TEST"
```

If the pattern does not produce a replacement, fix the sed pattern in the hook before proceeding.

#### 5d. E2E commit test

Perform a real commit to verify the hook works end-to-end:

1. Make a trivial change (e.g., add a blank line to a tracked file)
2. Stage and commit
3. Verify the version file(s) were updated with today's date
4. Verify that lock files (if applicable) were regenerated and staged in the commit
5. Present the result to the user, and inform them they can undo the test commit with `git reset HEAD~1`

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

  # ... lock file regeneration here (see Lock File Regeneration section) ...

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
5. **Stage updated files**: After each file is modified, run `git add <file>` to include the change in the commit. This includes lock files that are regenerated by package managers.
6. **Check staging**: Only update version files that have other staged changes in the same package/directory. Use `git diff --cached --name-only` to determine what is staged.
7. **Existing hooks**: If a pre-commit hook already exists, insert the version-hook block using marker comments. Do not overwrite existing content.
8. **Hook frameworks**: If the project uses husky, lefthook, or similar:
   - **husky**: Add to `.husky/pre-commit`
   - **lefthook**: Add to `lefthook.yml` under `pre-commit.commands`
   - **pre-commit (Python)**: Add as a `local` hook in `.pre-commit-config.yaml`
   - Fall back to `.git/hooks/pre-commit` if no framework is detected
9. **Make executable**: Run `chmod +x` on the hook file after writing.
10. **Regenerate lock files**: After updating manifest files, regenerate associated lock files if they exist and the tool is available. Only regenerate if the lock file already exists. Check tool availability with `command -v <tool> >/dev/null 2>&1`. Append `|| :` so failures do not block the commit. Stage the regenerated lock file with `git add`. See the ecosystem reference files for specific commands.
11. **Sourceable `__vh_compute_version`**: Define `__vh_compute_version` so it can be sourced and called independently for testing. Do not nest it inside constructs that prevent external invocation (e.g., avoid inlining it within a pipeline or command substitution that hides it).

## Ecosystem References

Per-ecosystem version file patterns, sed commands, and lock file regeneration rules.
Read the relevant reference file based on the project's ecosystem.

- **Node.js / JavaScript / TypeScript**: See [references/node.md](references/node.md)
- **Python**: See [references/python.md](references/python.md)
- **Rust**: See [references/rust.md](references/rust.md)
- **Java / Kotlin**: See [references/jvm.md](references/jvm.md)
- **Swift / Apple**: See [references/apple.md](references/apple.md)
- **Go, Ruby, PHP, .NET, Claude Code Plugin, Generic**: See [references/other.md](references/other.md)

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
- [ ] Verify 5a: shellcheck (or sh -n) passes with no errors
- [ ] Verify 5b: __vh_compute_version returns correct results for all 3 test cases
- [ ] Verify 5c: sed pattern actually replaces the version in each target file (dry-run)
- [ ] Verify 5d: test commit proves version was updated end-to-end
- [ ] Lock file regeneration added for applicable ecosystems
