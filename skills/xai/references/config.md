# Config

## Initialize configuration

```bash
xai config init
```

Sets up the configuration file with default settings. Prompts for API key if `XAI_API_KEY` is not set.

## Set configuration values

```bash
xai config set <key> <value>
```

## List configuration

```bash
xai config list
```

Shows current configuration values.

## List available models

```bash
xai models
```

Lists all available xAI models.

## Environment variables

- `XAI_API_KEY` — xAI API key (required)

## Config file location

Configuration is stored in `~/.config/xai-cli/config.json`.
