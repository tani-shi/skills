# Calendar

## List calendars

```bash
gog calendar calendars
```

## Calendar ACL

```bash
gog calendar acl <calendarId>
```

## List events

```bash
gog calendar events <calendarId> [--cal ID_OR_NAME] [--calendars CSV] [--all] \
  [--from RFC3339] [--to RFC3339] [--max N] [--page TOKEN] [--query Q] [--weekday]
```

- `--all`: show events from all calendars
- `--from` / `--to`: date range (accepts relatives like `today`, `tomorrow`, `next monday`)
- `--query`: free-text search within events
- `--weekday`: show day-of-week in output (default if `GOG_CALENDAR_WEEKDAY=1`)

## Get a single event

```bash
gog calendar event <calendarId> <eventId>
gog calendar get <calendarId> <eventId>
```

## Create event

```bash
gog calendar create <calendarId> --summary S --from DT --to DT \
  [--description D] [--location L] [--attendees a@b.com,c@d.com] \
  [--all-day] [--event-type TYPE]
```

- `--all-day`: create an all-day event (use date-only for `--from`/`--to`)
- `--attendees`: comma-separated email addresses

## Update event

```bash
gog calendar update <calendarId> <eventId> \
  [--summary S] [--from DT] [--to DT] [--description D] [--location L] \
  [--attendees ...] [--add-attendee ...] [--all-day] [--event-type TYPE]
```

- `--attendees`: replaces all attendees
- `--add-attendee`: adds to existing attendees

## Delete event

```bash
gog calendar delete <calendarId> <eventId>
```

## Free/busy check

```bash
gog calendar freebusy <calendarIds> --from RFC3339 --to RFC3339
```

Check availability for one or more calendars in a time range.

## Respond to event

```bash
gog calendar respond <calendarId> <eventId> \
  --status accepted|declined|tentative \
  [--send-updates all|none|externalOnly]
```

## Common examples

```bash
# Today's events
gog calendar events primary --from today --to tomorrow

# This week
gog calendar events primary --from today --to "next monday"

# Create a meeting
gog calendar create primary --summary "Team sync" \
  --from "2025-03-01T10:00:00" --to "2025-03-01T11:00:00" \
  --attendees "alice@example.com,bob@example.com"

# Check if someone is free
gog calendar freebusy primary --from "2025-03-01T09:00:00" --to "2025-03-01T17:00:00"
```
