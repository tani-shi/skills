# Java / Kotlin — Version Files

## Version File Patterns

| File | Tool/pattern | Notes |
|------|-------------|-------|
| `pom.xml` | `s\|<version>OLD</version>\|<version>NEW</version>\|` | Only the project's own `<version>`, not `<parent>` or dependency versions. Target the first occurrence or use xpath. |
| `build.gradle` / `build.gradle.kts` | `s/version = "[^"]*"/version = "NEW"/` or `s/version '[^']*'/version 'NEW'/` | |
