# show

## fam show

```bash
fam show [--date TEXT] [--from TEXT] [--to TEXT] [--service TEXT] [--category TEXT] [--tag TEXT] [--format TEXT] [--summary]
```

Display asset snapshots with filtering and formatting options.

- `--date, -d TEXT` — Show a specific date (default: latest available)
- `--from TEXT` — Start date for range query (`YYYY-MM-DD`)
- `--to TEXT` — End date for range query (`YYYY-MM-DD`)
- `--service, -s TEXT` — Filter by service name
- `--category, -c TEXT` — Filter by asset category (e.g., `crypto`, `stock`, `deposit`)
- `--tag, -t TEXT` — Filter by tag (repeatable for multiple tags)
- `--format TEXT` — Output format: `table` (default), `json`, `csv`
- `--summary` — Show totals only (date, record count, total JPY value)

### Output formats

**Table** (default): Rich-formatted table with columns: Date, Service, Institution, Name, Category, Amount, Value (JPY), Tags

**JSON**: Array of daily snapshot objects with full record details including `id`, `currency`, `amount`, `value`, `value_jpy`, `tags`, `memo`, `raw`

**CSV**: Header row + data rows. Tags are semicolon-separated within the field.

### Examples

```bash
# Show latest snapshot
fam show

# Show specific date
fam show --date 2026-03-01

# Show date range filtered by category
fam show --from 2026-01-01 --to 2026-03-08 --category crypto

# Show summary for a date range
fam show --from 2026-01-01 --to 2026-03-08 --summary

# Machine-readable output
fam show --format json
fam show --format csv

# Filter by service and tag
fam show --service binance --tag volatile
```
