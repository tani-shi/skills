# Swift / Apple — Version Files

## Version File Patterns

| File | Tool | Notes |
|------|------|-------|
| `Info.plist` | `/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString NEW" Info.plist` | Use PlistBuddy, not sed |
| `.xcconfig` | `s/MARKETING_VERSION = .*/MARKETING_VERSION = NEW/` | |
| `Package.swift` | Usually no version field | |
