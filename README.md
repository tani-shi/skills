# skills

A Claude Code plugin marketplace.

## Installation

```bash
/install tani-shi-skills@tani-shi-skills
```

## Prerequisites

Some skills depend on external CLI tools. Install and configure the ones you need:

- [gogcli](https://github.com/steipete/gogcli) — for the **gog** skill. Install and authenticate before use.

## Skills

### cli-inspector

Investigate CLI tools by discovering their full command trees and inspecting source repositories.

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

