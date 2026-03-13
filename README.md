# skills

A Claude Code plugin marketplace.

## Installation

```bash
/install tani-shi-skills@tani-shi-skills
```

## Prerequisites

Some skills depend on external CLI tools. Install and configure the ones you need:

- [gogcli](https://github.com/steipete/gogcli) — for the **gog** skill. Install and authenticate before use.
- [xai-cli](https://github.com/tani-shi/xai-cli) — for the **xai** skill. Install and set the `XAI_API_KEY` environment variable.
- [fam](https://github.com/tani-shi/fam) — for the **fam** skill. Install and authenticate before use.

## Skills

### cli-inspector

Investigate CLI tools by discovering their full command trees and inspecting source repositories.

### fam

Use the `fam` CLI to manage and track financial assets across MoneyForward, Coincheck, and Binance.

### gog

Use the `gog` CLI to interact with Google Workspace services.

- Gmail (search, read, send, drafts, labels)
- Google Calendar (events, create, freebusy, respond)
- Google Drive (list, search, upload, download, share)
- Google Chat (spaces, messages, DMs)
- Google Tasks (lists, add, update, complete)
- Google Classroom (courses, students, coursework, submissions)
- Google Contacts & People (search, create, update, directory)

### version-hook

Set up a git pre-commit hook that auto-updates version strings using date-based versioning (`yyyy.mm.dd`). Analyzes the project structure to identify version files and generates a cross-platform hook script that coexists with existing hooks. Supports monorepos, multiple languages/ecosystems, and hook frameworks (husky, lefthook, etc.).

### xai

Use the `xai` CLI to search and browse X (Twitter) content and the web via the xAI API.

- Search X posts (by query, user, date range, image filter)
- User timelines (browse posts from specific users)
- Threads (retrieve and summarize full threads)
- Trending topics (global and by country/category)
- Web search (with domain filtering)
