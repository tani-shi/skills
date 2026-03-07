# Web

## Web search

```bash
xai web "<query>" [--domain DOMAIN,...] [--exclude-domain DOMAIN,...] \
  [--format FORMAT] [--model MODEL]
```

Performs a web search via the xAI API.

- `--domain DOMAIN,...` — restrict results to these domains (comma-separated)
- `--exclude-domain DOMAIN,...` — exclude results from these domains
- `--format FORMAT` — output format (`plain`, `json`, `markdown`)
- `--model MODEL` — xAI model to use

## Examples

```bash
# Basic web search
xai web "xAI Grok latest updates"

# Search within specific domains
xai web "AI safety research" --domain arxiv.org,openai.com

# Search excluding certain domains
xai web "machine learning tutorial" --exclude-domain medium.com --format markdown
```
