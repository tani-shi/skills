# Contacts & People

## Contacts — search

```bash
gog contacts search <query> [--max N]
gog contacts list [--max N] [--page TOKEN]
gog contacts get <people/...|email>
```

## Contacts — create/update/delete

```bash
gog contacts create --given NAME [--family NAME] [--email addr] [--phone num]
gog contacts update <people/...> [--given NAME] [--family NAME] [--email addr] \
  [--phone num] [--birthday YYYY-MM-DD] [--notes TEXT] [--from-file PATH|-] [--ignore-etag]
gog contacts delete <people/...>
```

## Directory (Workspace)

```bash
gog contacts directory list [--max N] [--page TOKEN]
gog contacts directory search <query> [--max N] [--page TOKEN]
```

## Other contacts (auto-saved)

```bash
gog contacts other list [--max N] [--page TOKEN]
gog contacts other search <query> [--max N]
```

## People API

```bash
gog people me                              # current user profile
gog people get <people/...|userId>         # get a person's profile
gog people search <query> [--max N] [--page TOKEN]
gog people relations [<people/...|userId>] [--type TYPE]
```
