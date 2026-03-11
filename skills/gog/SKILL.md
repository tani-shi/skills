---
name: gog
description: >
  Use the `gog` CLI to interact with Google Workspace services: Gmail, Google Calendar,
  Google Drive, Google Chat, Google Tasks, Google Classroom, and Google Contacts.
  Use when the user wants to send or read email, check or create calendar events,
  upload or download Drive files, send Chat messages, manage tasks, or look up contacts.
  Trigger on: "gog", "Gmail", "Google Calendar", "Google Drive", "Google Chat",
  "Google Tasks", "Google Classroom", "Google Contacts", "send email", "read email",
  "check my calendar", "schedule a meeting", "upload to Drive", "share a file",
  "send a message on Chat", "add a task", "find contact",
  or any request to perform an action on a Google Workspace service.
  Do NOT trigger when the user is just discussing Google services conceptually
  without wanting to perform an action.
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
