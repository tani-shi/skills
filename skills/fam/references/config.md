# config

## fam config show

```bash
fam config show
```

Display the current configuration as JSON.

## fam config set

```bash
fam config set <key> <value>
```

Set a configuration value using dot-notation keys.

- `<key>` — Dot-notation path (e.g., `default_currency`, `services.binance.enabled`)
- `<value>` — Value to set. Type coercion: `"true"/"false"/"yes"/"1"` → boolean, numeric strings → int, otherwise string

### Config file structure

```json
{
  "schema_version": 1,
  "default_currency": "JPY",
  "services": {
    "service_name": {
      "type": "moneyforward|coincheck|binance",
      "enabled": true,
      "settings": {}
    }
  },
  "tags": {
    "rules": [
      {
        "match": { "category": "crypto", "service": "binance" },
        "apply_tags": ["volatile", "exchange"]
      }
    ]
  }
}
```

### Examples

```bash
# View current config
fam config show

# Change default currency
fam config set default_currency USD

# Disable a service
fam config set services.binance.enabled false

# Enable Binance testnet
fam config set services.binance.settings.testnet true
```
