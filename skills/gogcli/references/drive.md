# Drive

## List files

```bash
gog drive ls [--parent ID] [--max N] [--page TOKEN] [--query Q] [--[no-]all-drives]
```

- `--parent`: list contents of a specific folder
- `--query`: raw Google Drive query (e.g., `mimeType='application/pdf'`)
- `--all-drives`: include shared drives

## Search files

```bash
gog drive search <text> [--raw-query] [--max N] [--page TOKEN] [--[no-]all-drives]
```

- Default: searches file names and content for `<text>`
- `--raw-query`: treat `<text>` as a raw Drive API query string

## Get file metadata

```bash
gog drive get <fileId>
```

## Download file

```bash
gog drive download <fileId> [--out PATH] [--format F]
```

- `--format`: export format for Google Workspace files (e.g., `pdf`, `docx`, `xlsx`, `csv`, `txt`)
- Native files (non-Workspace) are downloaded as-is

## Upload file

```bash
gog drive upload <localPath> [--name N] [--parent ID] [--convert] [--convert-to doc|sheet|slides]
```

- `--convert`: auto-convert to Google Workspace format
- `--convert-to`: specify target format

## Create folder

```bash
gog drive mkdir <name> [--parent ID]
```

## Delete file

```bash
gog drive delete <fileId> [--permanent]
```

- Default: moves to trash
- `--permanent`: permanently deletes (irreversible)

## Move file

```bash
gog drive move <fileId> --parent ID
```

## Rename file

```bash
gog drive rename <fileId> <newName>
```

## Share file

```bash
gog drive share <fileId> --to anyone|user|domain \
  [--email addr] [--domain example.com] [--role reader|writer] [--discoverable]
```

## List permissions

```bash
gog drive permissions <fileId> [--max N] [--page TOKEN]
```

## Remove sharing

```bash
gog drive unshare <fileId> <permissionId>
```

## Get web URLs

```bash
gog drive url <fileIds...>
```

## List shared drives

```bash
gog drive drives [--max N] [--page TOKEN] [--query Q]
```

## Advanced search (Drive search bar & `--query` / `--raw-query` syntax)

### UI search operators (Drive search bar, also usable with `gog drive search`)

| Operator | Example | Description |
|----------|---------|-------------|
| `owner:` | `owner:alice@example.com` | Files owned by user |
| `from:` | `from:bob@example.com` | Files shared by user |
| `to:` | `to:me` | Files you shared with someone |
| `title:` | `title:budget` | Match file name only |
| `type:` | `type:spreadsheet` | Filter by type: `document`, `spreadsheet`, `presentation`, `pdf`, `image`, `video`, `folder`, `form` |
| `is:starred` | `is:starred` | Starred files |
| `is:trashed` | `is:trashed` | Trashed files |
| `before:` | `before:2025-01-01` | Modified before date (YYYY-MM-DD) |
| `after:` | `after:2025-01-01` | Modified after date |
| `"exact phrase"` | `"Q3 report"` | Exact phrase match |
| `-` | `budget -draft` | Exclude term |

### API query terms (for `--query` on `gog drive ls` and `--raw-query` on `gog drive search`)

| Term | Operators | Example |
|------|-----------|---------|
| `name` | `contains`, `=`, `!=` | `name contains 'budget'` |
| `fullText` | `contains` | `fullText contains '"Q3 report"'` |
| `mimeType` | `contains`, `=`, `!=` | `mimeType = 'application/pdf'` |
| `modifiedTime` | `<`, `<=`, `=`, `!=`, `>`, `>=` | `modifiedTime > '2025-01-01T00:00:00'` |
| `createdTime` | `<`, `<=`, `=`, `!=`, `>`, `>=` | `createdTime >= '2025-06-01T00:00:00'` |
| `viewedByMeTime` | `<`, `<=`, `=`, `!=`, `>`, `>=` | `viewedByMeTime > '2025-01-01T00:00:00'` |
| `trashed` | `=`, `!=` | `trashed = false` |
| `starred` | `=`, `!=` | `starred = true` |
| `parents` | `in` | `'FOLDER_ID' in parents` |
| `owners` | `in` | `'user@example.com' in owners` |
| `writers` | `in` | `'user@example.com' in writers` |
| `readers` | `in` | `'user@example.com' in readers` |
| `sharedWithMe` | `=`, `!=` | `sharedWithMe = true` |
| `visibility` | `=`, `!=` | `visibility = 'anyoneWithLink'` |
| `shortcutDetails.targetId` | `=`, `!=` | Target file ID of a shortcut |

Combine with `and`, `or`, `not`:
```
mimeType = 'application/pdf' and modifiedTime > '2025-01-01T00:00:00'
name contains 'report' and 'user@example.com' in owners
```

### Common MIME types

| Type | MIME |
|------|------|
| Google Doc | `application/vnd.google-apps.document` |
| Google Sheet | `application/vnd.google-apps.spreadsheet` |
| Google Slides | `application/vnd.google-apps.presentation` |
| Google Form | `application/vnd.google-apps.form` |
| Folder | `application/vnd.google-apps.folder` |
| PDF | `application/pdf` |
| CSV | `text/csv` |
| Plain text | `text/plain` |
| JPEG | `image/jpeg` |
| PNG | `image/png` |

### Examples

```bash
# PDFs modified this year
gog drive ls --query "mimeType = 'application/pdf' and modifiedTime > '2025-01-01T00:00:00'"

# Spreadsheets shared with me
gog drive ls --query "mimeType = 'application/vnd.google-apps.spreadsheet' and sharedWithMe = true"

# Files in a specific folder
gog drive ls --query "'FOLDER_ID' in parents"

# Search by owner using UI syntax
gog drive search "owner:alice@example.com budget"

# Raw API query
gog drive search --raw-query "name contains 'invoice' and 'finance@company.com' in owners"
```
