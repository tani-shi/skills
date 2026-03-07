# User

## Browse user timeline

```bash
xai user @<username> [--since DATE] [--until DATE] [--format FORMAT] [--model MODEL]
```

Retrieves posts from the specified user's timeline.

- `--since DATE` — only posts after this date
- `--until DATE` — only posts before this date
- `--format FORMAT` — output format (`plain`, `json`, `markdown`)
- `--model MODEL` — xAI model to use

## Examples

```bash
# Get recent posts from a user
xai user @elonmusk

# Get posts from last week
xai user @xaboratories --since 7d

# Get user timeline as JSON
xai user @anthropic --format json --since 2026-03-01
```
