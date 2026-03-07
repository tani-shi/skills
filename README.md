# skills

A Claude Code plugin marketplace.

## Installation

Add the marketplace:

```bash
/plugin marketplace add git@github.com:tani-shi/skills.git
```

Then install individual plugins:

```bash
/plugin install gog@tani-shi-skills
```

## Plugins

### gog

Use the `gog` CLI to interact with Google Workspace services.

- Gmail (search, read, send, drafts, labels)
- Google Calendar (events, create, freebusy, respond)
- Google Drive (list, search, upload, download, share)
- Google Chat (spaces, messages, DMs)
- Google Tasks (lists, add, update, complete)
- Google Classroom (courses, students, coursework, submissions)
- Google Contacts & People (search, create, update, directory)

Requires [gogcli](https://github.com/steipete/gogcli) installed and authenticated.

### xai

Use the `xai` CLI to search and browse X (Twitter) content and the web via the xAI API.

- Search X posts (by query, user, date range, image filter)
- User timelines (browse posts from specific users)
- Threads (retrieve and summarize full threads)
- Trending topics (global and by country/category)
- Web search (with domain filtering)

Requires [xai-cli](https://github.com/tani-shi/xai-cli) installed and `XAI_API_KEY` environment variable set.
