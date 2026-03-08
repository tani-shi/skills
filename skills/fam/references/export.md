# export

## fam export

```bash
fam export <path> [--from TEXT] [--to TEXT]
```

Export snapshots to a JSON file (ExportBundle format).

- `<path>` — Output file path (creates parent directories if needed)
- `--from TEXT` — Start date (`YYYY-MM-DD`)
- `--to TEXT` — End date (`YYYY-MM-DD`)

### Output format (ExportBundle)

```json
{
  "exported_at": "2026-03-08T12:34:56.123456",
  "schema_version": 1,
  "snapshots": [
    {
      "date": "2026-03-08",
      "fetched_at": "...",
      "schema_version": 1,
      "records": [...],
      "metadata": {...}
    }
  ]
}
```

### Examples

```bash
# Export all snapshots
fam export backup.json

# Export date range
fam export backup.json --from 2026-01-01 --to 2026-03-08
```
