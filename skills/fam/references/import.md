# import

## fam import

```bash
fam import <path> [--force] [--dry-run]
```

Import snapshots from an ExportBundle JSON file.

- `<path>` — Input file path (must be a valid ExportBundle JSON)
- `--force, -f` — Overwrite existing snapshots for conflicting dates
- `--dry-run` — Preview import without writing any data

### Behavior

- Validates the file matches ExportBundle schema before importing
- Checks for date conflicts (existing snapshots for the same dates)
- Without `--force`, lists conflicting dates and aborts
- Writes each snapshot to the proper location in `~/.fam/data/`

### Examples

```bash
# Preview what would be imported
fam import backup.json --dry-run

# Import, overwriting conflicts
fam import backup.json --force

# Standard import (fails on conflicts)
fam import backup.json
```
