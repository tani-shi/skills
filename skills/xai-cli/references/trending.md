# Trending

## Discover trending topics

```bash
xai trending [--country CODE] [--category CATEGORY] [--format FORMAT] [--model MODEL]
```

Shows currently trending topics on X.

- `--country CODE` — country code to filter trends (e.g., `US`, `JP`, `GB`)
- `--category CATEGORY` — topic category filter
- `--format FORMAT` — output format (`plain`, `json`, `markdown`)
- `--model MODEL` — xAI model to use

## Examples

```bash
# Get global trending topics
xai trending

# Get trending topics in Japan
xai trending --country JP

# Get trending in a specific category as JSON
xai trending --category technology --format json
```
