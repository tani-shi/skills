#!/usr/bin/env python3
"""Validate a SKILL.md file against skill packaging rules."""

import re
import sys
from pathlib import Path

from utils import parse_skill_md

ALLOWED_FIELDS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024


def validate_skill(skill_dir: str | Path) -> list[str]:
    """Validate a skill directory's SKILL.md.

    Returns a list of error messages. Empty list means valid.
    """
    errors: list[str] = []
    skill_dir = Path(skill_dir)

    # 1. SKILL.md existence
    try:
        fields = parse_skill_md(skill_dir)
    except FileNotFoundError as e:
        return [str(e)]
    except ValueError as e:
        return [str(e)]

    # 2. Required fields
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append("Missing required field: name")
    if not description:
        errors.append("Missing required field: description")

    # 3. Name validation (kebab-case)
    if name:
        if len(name) > MAX_NAME_LENGTH:
            errors.append(f"name exceeds {MAX_NAME_LENGTH} characters (got {len(name)})")
        if name.startswith("-") or name.endswith("-"):
            errors.append("name must not start or end with a hyphen")
        if "--" in name:
            errors.append("name must not contain consecutive hyphens")
        if not re.match(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$", name):
            errors.append(f"name must be kebab-case (lowercase alphanumeric and hyphens): got '{name}'")

    # 4. Description validation
    if description:
        if len(description) > MAX_DESCRIPTION_LENGTH:
            errors.append(f"description exceeds {MAX_DESCRIPTION_LENGTH} characters (got {len(description)})")
        if re.search(r"[<>]", description):
            errors.append("description must not contain angle brackets (< or >)")

    # 5. Unknown fields
    known_keys = ALLOWED_FIELDS | {"_body"}
    unknown = set(fields.keys()) - known_keys
    if unknown:
        errors.append(f"Unknown frontmatter fields: {', '.join(sorted(unknown))}")

    return errors


def main():
    if len(sys.argv) < 2:
        print("Usage: quick_validate.py <skill-directory>", file=sys.stderr)
        sys.exit(2)

    skill_dir = sys.argv[1]
    errors = validate_skill(skill_dir)

    if errors:
        print(f"FAIL: {skill_dir}")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"PASS: {skill_dir}")


if __name__ == "__main__":
    main()
