---
name: gogcli
description: >
  Use the `gog` CLI to interact with Google Workspace services on the user's behalf.
  Supports Gmail (search, read, send, drafts, labels), Google Calendar (list, create, update, delete events),
  Google Drive (list, search, upload, download, share files), Google Chat (spaces, messages, DMs),
  Google Tasks (lists, add, update, complete), Google Classroom (courses, students, coursework, submissions),
  Google Contacts and People (search, create, update), and more.
  Trigger when the user asks to read/send email, check/create calendar events, manage Drive files,
  send Chat messages, manage tasks, interact with Classroom, look up contacts, or any Google Workspace operation.
  Also trigger when the user mentions "gog", "gogcli", "Gmail", "Google Calendar", "Google Drive",
  "Google Chat", "Google Tasks", "Google Classroom", "Google Contacts", or similar Google service names
  in the context of performing actions (not just discussing them).
---

# gogcli — Google Workspace CLI

Use the `gog` command to interact with Google services. The CLI is already installed and authenticated.

## Global flags

- `--json` — JSON output (use for parsing structured data)
- `--plain` — TSV output (stable, no colors)
- `--force` — skip confirmations for destructive commands
- `--account EMAIL` — select account (or set `GOG_ACCOUNT`)
- `--client NAME` — select OAuth client bucket

Hints/progress go to stderr; data goes to stdout.

## Output handling

- Default output is human-readable tables. Use `--json` when you need to parse results programmatically.
- Always capture stderr separately — it contains progress/hints, not data.
- For piping: `gog ... --json 2>/dev/null` gives clean JSON on stdout.

## Date/time input

- Date-only: `YYYY-MM-DD`
- Datetime: RFC3339 or `YYYY-MM-DDTHH:MM[:SS]`
- Relatives: `now`, `today`, `tomorrow`, `yesterday`, weekday names (`monday`, `next friday`)
- Durations: `24h` (for `--since` flags)

## Service reference files

Load the relevant reference file based on which Google service the user needs:

- **Gmail** (search, read, send, drafts, labels, watch): See [references/gmail.md](references/gmail.md)
- **Calendar** (events, create, freebusy, respond): See [references/calendar.md](references/calendar.md)
- **Drive** (list, search, upload, download, share): See [references/drive.md](references/drive.md)
- **Chat** (spaces, messages, DMs): See [references/chat.md](references/chat.md)
- **Tasks** (lists, add, update, complete): See [references/tasks.md](references/tasks.md)
- **Classroom** (courses, students, coursework, submissions): See [references/classroom.md](references/classroom.md)
- **Contacts & People** (search, create, update, directory): See [references/contacts.md](references/contacts.md)
- **Auth & Config** (credentials, tokens, config): See [references/auth.md](references/auth.md)

## Common patterns

### Multi-step workflows

When performing complex tasks (e.g., "find an email and reply to it"), chain commands:
1. Search/list to find the resource ID
2. Get details if needed
3. Perform the action using the ID

### Checking available accounts

```bash
gog auth list
```

### Quick time check

```bash
gog time now
```
