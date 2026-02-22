# Chat

## List spaces

```bash
gog chat spaces list [--max N] [--page TOKEN]
```

## Find space by name

```bash
gog chat spaces find <displayName> [--max N]
```

## Create space

```bash
gog chat spaces create <displayName> [--member email,...]
```

## List messages in a space

```bash
gog chat messages list <space> [--max N] [--page TOKEN] [--order ORDER] [--thread THREAD] [--unread]
```

- `<space>`: space name/ID (e.g., `spaces/AAAA...`)
- `--thread`: filter to a specific thread
- `--unread`: only unread messages

## Send message

```bash
gog chat messages send <space> --text TEXT [--thread THREAD]
```

## List threads

```bash
gog chat threads list <space> [--max N] [--page TOKEN]
```

## Direct messages

```bash
# Find or create DM space with a user
gog chat dm space <email>

# Send a DM
gog chat dm send <email> --text TEXT [--thread THREAD]
```
