# Other Ecosystems — Version Files

## Go

| File | sed pattern |
|------|-------------|
| `version.go` or similar | `s/Version = "[^"]*"/Version = "NEW"/` |

Go modules don't have a manifest version. Look for a `version.go` or constant declaration.

## Ruby

| File | sed pattern |
|------|-------------|
| `*.gemspec` | `s/\.version *= *"[^"]*"/.version = "NEW"/` |
| `lib/*/version.rb` | `s/VERSION = "[^"]*"/VERSION = "NEW"/` |

## PHP

| File | sed pattern |
|------|-------------|
| `composer.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

## .NET / C#

| File | sed pattern |
|------|-------------|
| `*.csproj` | `s\|<Version>.*</Version>\|<Version>NEW</Version>\|` |
| `Directory.Build.props` | Same as above |

## Claude Code Plugin

| File | sed pattern |
|------|-------------|
| `marketplace.json` | `s/"version": *"[^"]*"/"version": "NEW"/` |

## Generic / Other

| File | sed pattern |
|------|-------------|
| `VERSION` or `VERSION.txt` | Replace entire file content |
| `version.txt` | Replace entire file content |
| Custom config (YAML/JSON/TOML) | Adapt pattern to match the version field |
