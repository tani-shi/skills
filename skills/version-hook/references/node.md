# Node.js / JavaScript / TypeScript — Version Files

## Version File Patterns

| File | sed pattern |
|------|-------------|
| `package.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

For monorepos, check `workspaces` in root `package.json` or `lerna.json` / `pnpm-workspace.yaml`.

## Lock File Regeneration

npm, yarn, and pnpm auto-update their lock files on install — no explicit regeneration needed in the hook.
