#!/usr/bin/env python3
"""Pull the most recent file from each department's data directory.

Departments: analytics, content, social, marketing, pr, strategy.
Lists each with name, date, and first 3 lines of content.
"""

import os
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
DATA_DIR = REPO_ROOT / "data"

DEPARTMENTS = [
    "analytics",
    "content",
    "social",
    "marketing",
    "pr",
    "strategy",
]


def get_most_recent_file(dept_dir: Path):
    """Find the most recently modified file in a department directory."""
    if not dept_dir.exists():
        return None

    most_recent = None
    most_recent_time = 0

    for item in dept_dir.rglob("*"):
        if not item.is_file():
            continue
        if item.name in (".gitkeep", ".DS_Store"):
            continue

        mtime = item.stat().st_mtime
        if mtime > most_recent_time:
            most_recent_time = mtime
            most_recent = item

    if most_recent is None:
        return None

    # Read first 3 content lines (skip blank lines and markdown frontmatter delimiters)
    preview_lines = []
    try:
        with open(most_recent, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                stripped = line.strip()
                if stripped and stripped != "---":
                    preview_lines.append(stripped)
                if len(preview_lines) >= 3:
                    break
    except (OSError, UnicodeDecodeError):
        preview_lines = ["(binary or unreadable file)"]

    return {
        "name": most_recent.name,
        "path": str(most_recent.relative_to(REPO_ROOT)),
        "modified": datetime.fromtimestamp(most_recent_time).strftime("%Y-%m-%d %H:%M"),
        "preview": preview_lines,
    }


def main():
    print("=" * 70)
    print("WEEKLY DIGEST - DATA COMPILATION")
    print(f"Compiled: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    if not DATA_DIR.exists():
        print(f"\nData directory does not exist: {DATA_DIR}")
        print("No department data available to compile.")
        return

    found_count = 0
    missing_depts = []

    for dept in DEPARTMENTS:
        dept_dir = DATA_DIR / dept
        print(f"\n--- {dept.upper()} ---")

        result = get_most_recent_file(dept_dir)

        if result is None:
            if not dept_dir.exists():
                print(f"  Directory not found: data/{dept}/")
            else:
                print(f"  No data files found in data/{dept}/")
            missing_depts.append(dept)
            continue

        found_count += 1
        print(f"  File:     {result['name']}")
        print(f"  Path:     {result['path']}")
        print(f"  Modified: {result['modified']}")
        print(f"  Preview:")
        for line in result["preview"]:
            # Truncate long lines for readability
            display = line[:80] + "..." if len(line) > 80 else line
            print(f"    > {display}")

    # Summary
    print(f"\n{'=' * 70}")
    print("COMPILATION SUMMARY")
    print(f"  Departments with data:    {found_count}/{len(DEPARTMENTS)}")
    print(f"  Departments missing data: {len(missing_depts)}")
    if missing_depts:
        print(f"  Missing: {', '.join(missing_depts)}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
