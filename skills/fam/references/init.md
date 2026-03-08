# init

## fam init

```bash
fam init
```

Initialize the fam workspace. Creates the directory structure, prompts for service configuration, and tests connections.

### What it creates

- `~/.fam/config.json` — Main configuration file
- `~/.fam/data/` — Daily snapshot storage
- `~/.fam/sessions/moneyforward/` — Playwright browser session cache

### Interactive setup flow

1. Creates workspace directory (default: `~/.fam`, override with `FAM_WORKSPACE`)
2. Prompts to select which services to enable (MoneyForward, Coincheck, Binance)
3. For each enabled service, prompts for credentials:
   - Sensitive fields (password, secret, key) use hidden input
   - Credentials stored in system keyring as `fam:{service}:{field}`
4. Prompts for service-specific settings (e.g., Binance testnet mode)
5. Tests each service connection automatically

### Examples

```bash
# Standard initialization
fam init

# Use custom workspace location
FAM_WORKSPACE=/path/to/workspace fam init
```
