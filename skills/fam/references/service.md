# service

## fam service list

```bash
fam service list
```

Show all available and configured services with their status.

## fam service add

```bash
fam service add <type>
```

Add and configure a new service. Prompts for credentials and settings interactively.

- `<type>` — Service type: `moneyforward`, `coincheck`, `binance`

Credentials are stored in the system keyring as `fam:{service}:{field}`.

### Per-service credentials

| Service | Fields |
|---------|--------|
| MoneyForward | `email`, `password` |
| Coincheck | `api_key`, `api_secret` |
| Binance | `api_key`, `api_secret` |

### Per-service settings

| Service | Settings |
|---------|----------|
| Binance | `testnet` (boolean, default: false) |

## fam service remove

```bash
fam service remove <name>
```

Remove a configured service.

## fam service test

```bash
fam service test <name>
```

Test the connection for a configured service. Validates credentials and connectivity.

### Examples

```bash
# List all services
fam service list

# Add Binance service
fam service add binance

# Test connection
fam service test binance

# Remove a service
fam service remove coincheck
```
