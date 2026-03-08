# fetch

## fam fetch

```bash
fam fetch [--service TEXT] [--date TEXT] [--force] [--update]
```

Fetch asset data from enabled services and save a daily snapshot.

- `--service, -s TEXT` — Fetch from a specific service only (e.g., `binance`, `coincheck`, `moneyforward`)
- `--date, -d TEXT` — Target date in `YYYY-MM-DD` format (default: today)
- `--force, -f` — Overwrite existing snapshot for the date
- `--update, -u` — Run MoneyForward bulk account refresh before fetching

### Behavior

- Fetches from all enabled services unless `--service` is specified
- Applies tag rules from config after fetching
- Saves snapshot to `~/.fam/data/{YYYY}/{MM}/{YYYY-MM-DD}.json`
- If a snapshot already exists for the date, requires `--force` to overwrite
- If a service fails, continues with remaining services and records the error in metadata
- Missing credentials raises `AuthenticationError` with hint to run `fam service add`

### Examples

```bash
# Fetch all services for today
fam fetch

# Fetch with MoneyForward refresh first
fam fetch --update

# Fetch only Binance data
fam fetch --service binance

# Fetch for a specific date, overwriting existing data
fam fetch --date 2026-03-01 --force
```
