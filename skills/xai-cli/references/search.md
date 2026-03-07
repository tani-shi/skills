# Search

## Search X posts

```bash
xai search "<query>" [--since DATE] [--until DATE] [--from-users USER,...] \
  [--to-users USER,...] [--exclude-from-users USER,...] \
  [--has-image] [--format FORMAT] [--model MODEL]
```

Searches X posts matching the given query.

- `--since DATE` — only posts after this date
- `--until DATE` — only posts before this date
- `--from-users USER,...` — filter by post authors (comma-separated usernames)
- `--to-users USER,...` — filter by reply targets (comma-separated usernames)
- `--exclude-from-users USER,...` — exclude posts from these users
- `--has-image` — only posts containing images
- `--format FORMAT` — output format (`plain`, `json`, `markdown`)
- `--model MODEL` — xAI model to use

## Examples

```bash
# Search for recent posts about a topic
xai search "Claude AI" --since 24h

# Search posts from specific users
xai search "announcement" --from-users elonmusk,xaboratories

# Search with image filter
xai search "infographic" --has-image --format json

# Search within a date range
xai search "product launch" --since 2026-01-01 --until 2026-02-01
```
