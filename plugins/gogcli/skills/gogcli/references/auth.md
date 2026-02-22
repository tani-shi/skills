# Auth & Config

## Credentials

```bash
gog auth credentials <credentials.json|->         # import OAuth client (default)
gog auth credentials list                          # list stored clients
gog --client <name> auth credentials <file>        # import named client
```

## Add account

```bash
gog auth add <email> [--services user|all|gmail,calendar,...] [--readonly] \
  [--drive-scope full|readonly|file] [--manual] [--remote] [--step 1|2] \
  [--auth-url URL] [--timeout DURATION] [--force-consent]
```

- `--services`: comma-separated list or `user` (default) / `all`
- `--readonly`: request read-only scopes where applicable
- `--manual`: paste redirect URL instead of opening browser
- `--remote --step 1|2`: two-step flow for headless servers
- `--force-consent`: force consent prompt (needed when Google doesn't return refresh token)

## List services

```bash
gog auth services [--markdown]
```

## Keep (Workspace service account)

```bash
gog auth keep <email> --key <service-account.json>
```

## Account management

```bash
gog auth list                    # list authenticated accounts
gog auth status                  # show current auth status
gog auth remove <email>          # remove an account
```

## Aliases

```bash
gog auth alias list
gog auth alias set <alias> <email>
gog auth alias unset <alias>
```

## Token management

```bash
gog auth tokens list
gog auth tokens delete <email>
```

## Config

```bash
gog config path                  # show config directory path
gog config keys                  # list available config keys
gog config list                  # show all config values
gog config get <key>             # get a config value
gog config set <key> <value>     # set a config value
gog config unset <key>           # remove a config value
```

## Environment variables

- `GOG_ACCOUNT=you@gmail.com` — default account
- `GOG_CLIENT=work` — select OAuth client bucket
- `GOG_TIMEZONE=America/New_York` — output timezone (IANA name or `UTC`)
- `GOG_KEYRING_BACKEND={auto|keychain|file}` — force keyring backend
- `GOG_KEYRING_PASSWORD=...` — password for file backend (headless)
- `GOG_ENABLE_COMMANDS=calendar,tasks` — allowlist top-level commands
- `GOG_CALENDAR_WEEKDAY=1` — show weekday in calendar output
