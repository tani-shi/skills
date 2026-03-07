# Thread

## Retrieve a thread

```bash
xai thread <URL> [--summarize] [--format FORMAT] [--model MODEL]
```

Retrieves and displays a full thread from a post URL.

- `--summarize` — generate a summary of the thread
- `--format FORMAT` — output format (`plain`, `json`, `markdown`)
- `--model MODEL` — xAI model to use

## Examples

```bash
# Retrieve a thread by URL
xai thread https://x.com/user/status/1234567890

# Retrieve and summarize a thread
xai thread https://x.com/user/status/1234567890 --summarize

# Get thread as markdown
xai thread https://x.com/user/status/1234567890 --format markdown
```
