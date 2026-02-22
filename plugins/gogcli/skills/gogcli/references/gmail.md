# Gmail

## Search

```bash
gog gmail search <query> [--max N] [--page TOKEN]
```

Returns thread IDs matching the Gmail search query. Uses Gmail's search syntax (e.g., `from:user@example.com`, `subject:meeting`, `is:unread`, `after:2024/01/01`).

## Message search

```bash
gog gmail messages search <query> [--max N] [--page TOKEN] [--include-body]
```

Returns individual messages (not threads). Use `--include-body` to include message body text.

## Read a thread

```bash
gog gmail thread get <threadId> [--download]
```

Returns all messages in a thread. `--download` saves attachments.

## Modify thread labels

```bash
gog gmail thread modify <threadId> [--add LABEL,...] [--remove LABEL,...]
```

## Read a single message

```bash
gog gmail get <messageId> [--format full|metadata|raw] [--headers HEADER,...]
```

- `--format full` (default): headers + body
- `--format metadata`: headers only
- `--format raw`: raw RFC 2822

## Download attachment

```bash
gog gmail attachment <messageId> <attachmentId> [--out PATH] [--name NAME]
```

## Get thread URLs

```bash
gog gmail url <threadIds...>
```

## Labels

```bash
gog gmail labels list
gog gmail labels get <labelIdOrName>
gog gmail labels create <name>
gog gmail labels modify <threadIds...> [--add LABEL,...] [--remove LABEL,...]
```

## Send email

```bash
gog gmail send --to a@b.com --subject S [--body B] [--body-html H] \
  [--cc addr,...] [--bcc addr,...] \
  [--reply-to-message-id <messageId>] [--reply-to addr] \
  [--attach <file>...]
```

- `--reply-to-message-id`: reply to a specific message (sets In-Reply-To/References headers)
- `--attach`: attach one or more local files

## Drafts

```bash
gog gmail drafts list [--max N] [--page TOKEN]
gog gmail drafts get <draftId> [--download]
gog gmail drafts create --subject S [--to a@b.com] [--body B] [--body-html H] \
  [--cc ...] [--bcc ...] [--reply-to-message-id <messageId>] [--reply-to addr] \
  [--attach <file>...]
gog gmail drafts update <draftId> --subject S [--to a@b.com] [--body B] ...
gog gmail drafts send <draftId>
gog gmail drafts delete <draftId>
```

## Watch (push notifications)

```bash
gog gmail watch start    # start push notifications
gog gmail watch status   # check current watch
gog gmail watch renew    # renew expiring watch
gog gmail watch stop     # stop push notifications
gog gmail watch serve    # run webhook server
```

## History

```bash
gog gmail history --since <historyId>
```

Returns mailbox changes since a given history ID (from watch or previous history call).
