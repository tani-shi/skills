# Python — Version Files & Lock Regeneration

## Version File Patterns

| File | sed pattern |
|------|-------------|
| `pyproject.toml` | `s/^version = "[^"]*"/version = "NEW"/` (under `[project]` or `[tool.poetry]`) |
| `setup.cfg` | `s/^version = .*/version = NEW/` (under `[metadata]`) |
| `__version__.py` or `_version.py` | `s/__version__ = "[^"]*"/__version__ = "NEW"/` |
| `setup.py` | `s/version="[^"]*"/version="NEW"/` |

## Lock File Regeneration

| Manifest | Lock file | Command | Condition |
|---|---|---|---|
| `pyproject.toml` | `uv.lock` | `uv lock` | `uv.lock` exists & `uv` available |
| `pyproject.toml` | `poetry.lock` | `poetry lock --no-update` | `poetry.lock` exists & `poetry` available |

Check `uv.lock` first; if absent, check `poetry.lock` (mutually exclusive).

### Example

```sh
# Add after pyproject.toml update:
if [ -f uv.lock ] && command -v uv >/dev/null 2>&1; then
  uv lock || :
  git add uv.lock
elif [ -f poetry.lock ] && command -v poetry >/dev/null 2>&1; then
  poetry lock --no-update || :
  git add poetry.lock
fi
```
