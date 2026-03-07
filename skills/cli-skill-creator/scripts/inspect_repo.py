#!/usr/bin/env python3
"""Extract version information from a git repository."""

import argparse
import json
import subprocess
import sys
from pathlib import Path


def git_run(repo_path: str, *git_args: str) -> str | None:
    """Run a git command in the given repo directory and return stdout."""
    try:
        result = subprocess.run(
            ["git"] + list(git_args),
            capture_output=True,
            text=True,
            cwd=repo_path,
            timeout=10,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        pass
    return None


def get_version_tag(repo_path: str) -> str | None:
    """Get the latest version tag."""
    # Try describe first
    tag = git_run(repo_path, "describe", "--tags", "--abbrev=0", "--match", "v*")
    if tag:
        return tag
    # Fallback to sorted tags
    tags = git_run(repo_path, "tag", "--sort=-v:refname")
    if tags:
        for t in tags.splitlines():
            if t.startswith("v"):
                return t
    return None


def inspect_repo(repo_path: str) -> dict:
    """Extract version information from a git repository."""
    path = Path(repo_path).resolve()
    if not (path / ".git").exists():
        print(f"Error: '{path}' is not a git repository", file=sys.stderr)
        sys.exit(1)

    repo = str(path)

    commit_hash = git_run(repo, "rev-parse", "HEAD") or ""
    commit_hash_short = git_run(repo, "rev-parse", "--short", "HEAD") or ""
    branch = git_run(repo, "rev-parse", "--abbrev-ref", "HEAD") or ""
    version_tag = get_version_tag(repo)
    commit_date = git_run(repo, "log", "-1", "--format=%aI") or ""
    remote_url = git_run(repo, "remote", "get-url", "origin")

    return {
        "commit_hash": commit_hash,
        "commit_hash_short": commit_hash_short,
        "branch": branch,
        "version_tag": version_tag,
        "commit_date": commit_date,
        "remote_url": remote_url,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract version information from a git repository"
    )
    parser.add_argument("repo_path", help="Path to the git repository")
    parser.add_argument(
        "--output",
        help="Output file path (default: stdout)",
    )
    args = parser.parse_args()

    info = inspect_repo(args.repo_path)
    output = json.dumps(info, indent=2, ensure_ascii=False)

    if args.output:
        with open(args.output, "w") as f:
            f.write(output + "\n")
        print(f"Output written to {args.output}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
