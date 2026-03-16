# Rust — Version Files & Lock Regeneration

## Version File Patterns

| File | sed pattern | Notes |
|------|-------------|-------|
| `Cargo.toml` | `s/^version = "[^"]*"/version = "NEW"/` | Only under `[package]`, NOT under `[dependencies]` |

For Cargo workspaces, check `[workspace]` members in root `Cargo.toml`. Use a flag or line-range approach to target only `[package].version`:

```sh
awk '/^\[package\]/{p=1} /^\[/{if(!/\[package\]/)p=0} p && /^version = /{sub(/"[^"]*"/, "\"NEW\""); print; next} {print}' Cargo.toml > Cargo.toml.tmp && mv Cargo.toml.tmp Cargo.toml
```

## Lock File Regeneration

| Manifest | Lock file | Command | Condition |
|---|---|---|---|
| `Cargo.toml` | `Cargo.lock` | `cargo generate-lockfile` | `Cargo.lock` exists & `cargo` available |

### Example

```sh
# Add after Cargo.toml update:
if [ -f Cargo.lock ] && command -v cargo >/dev/null 2>&1; then
  cargo generate-lockfile || :
  git add Cargo.lock
fi
```
