#!/usr/bin/env python3
"""Pull the most recent file from each department's data directory.

Departments: analytics, content, social, marketing, pr, strategy.
Lists each with name, date, and first 3 lines of content.
"""

import sys
from datetime import datetime
from pathlib import Path
from scripts.lib.paths import DATA_DIR
from scripts.lib.data_scanner import get_most_recent_file

DEPARTMENTS = [
    "analytics",
    "content",
    "social",
    "marketing",
    "pr",
    "strategy",
]
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
