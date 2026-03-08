---
name: fam
description: >
  Use the `fam` CLI to manage and track financial assets across MoneyForward, Coincheck, and Binance.
  Trigger when the user asks to fetch asset data, view portfolio snapshots, export/import financial data,
  configure financial services, or check asset balances.
  Also trigger when the user mentions "fam", "financial assets", "MoneyForward", "Coincheck", "Binance",
  "portfolio", or similar terms in the context of performing actions.
---

# fam — Financial Asset Management CLI

Use the `fam` command to fetch, track, and view financial asset data from multiple services. The CLI is already installed and authenticated.

Built from fam (caa2b06, 2026-03-07)

## Environment variables

- `FAM_WORKSPACE` — Override default workspace location (default: `~/.fam`)
- `LOG_LEVEL` — Logging verbosity: `DEBUG`, `INFO`, `WARNING` (default), `ERROR`, `CRITICAL`

## Workspace structure

```
~/.fam/
├── config.json
├── data/{YYYY}/{MM}/{YYYY-MM-DD}.json
└── sessions/moneyforward/
```

## Supported services

| Service | Type | Credentials |
|---------|------|-------------|
| MoneyForward | Web scraping (Playwright) | email, password |
| Coincheck | REST API (HMAC-SHA256) | api_key, api_secret |
| Binance | REST API (binance-connector) | api_key, api_secret |

Credentials are stored in the system keyring with prefix `fam:{service}:{field}`.

## Date format

All date inputs use ISO 8601: `YYYY-MM-DD` (e.g., `2026-03-08`).

## Output handling

Default output is a Rich table. Use `--format json` or `--format csv` for machine-readable output.

- **JSON**: Array of daily snapshots with records, metadata, and totals
- **CSV**: Header row + data rows; tags are semicolon-separated
- **Table**: Columns: Date, Service, Institution, Name, Category, Amount, Value (JPY), Tags

## Asset categories

`cash`, `deposit`, `stock`, `fund`, `bond`, `crypto`, `pension`, `insurance`, `real_estate`, `points`, `other`

## Command reference files

Load the relevant reference file based on which command the user needs:

- **init** (setup, initialize, workspace): See [references/init.md](references/init.md)
- **fetch** (download, pull, get data): See [references/fetch.md](references/fetch.md)
- **update** (refresh, sync MoneyForward): See [references/update.md](references/update.md)
- **show** (view, display, list, query): See [references/show.md](references/show.md)
- **export** (backup, save, dump): See [references/export.md](references/export.md)
- **import** (restore, load): See [references/import.md](references/import.md)
- **config** (settings, preferences): See [references/config.md](references/config.md)
- **service** (add, remove, test, list services): See [references/service.md](references/service.md)

## Common patterns

### Daily fetch with MoneyForward refresh

```bash
fam fetch --update
```

Triggers MoneyForward bulk account refresh, then fetches all enabled services and saves snapshot.

### View latest portfolio summary

```bash
fam show --summary
```

### Check crypto holdings over time

```bash
fam show --from 2026-01-01 --to 2026-03-08 --category crypto --format json
```

### Backup and restore

```bash
fam export backup.json --from 2026-01-01
fam import backup.json --dry-run
fam import backup.json
```
