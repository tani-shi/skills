# update

## fam update

```bash
fam update
```

Trigger MoneyForward bulk account refresh. This refreshes balances on MoneyForward's side but does **not** fetch or save any data locally.

### Behavior

1. Requires an enabled MoneyForward service in config
2. Authenticates to MoneyForward via Playwright
3. Clicks the bulk update button on the accounts page
4. Polls account status in real-time, showing progress: `"Updating accounts... (X/Y)"`
5. Reports accounts with error statuses
6. Exits after update completes

### Difference from `fam fetch --update`

| Aspect | `fam update` | `fam fetch --update` |
|--------|-------------|---------------------|
| Scope | MoneyForward only | All configured services |
| Saves data | No | Yes (snapshot JSON) |
| Typical use | Manual refresh before fetch | Automated daily fetch |

### Examples

```bash
# Refresh MoneyForward account data
fam update

# Then fetch all services
fam fetch
```
