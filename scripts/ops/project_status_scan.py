#!/usr/bin/env python3
"""Scan data/ for recently modified files (last 7 days).

Groups results by department. Also checks .claude/ceo-memory/active_projects.md
for the active project list.
"""

import sys
from datetime import datetime
from pathlib import Path
from scripts.lib.paths import DATA_DIR, CEO_MEMORY_DIR, REPO_ROOT
from scripts.lib.data_scanner import scan_recent_files, list_departments

ACTIVE_PROJECTS_PATH = CEO_MEMORY_DIR / "active_projects.md"
LOOKBACK_DAYS = 7
def read_active_projects(filepath: Path):
    """Read and return active projects file content."""
    if not filepath.exists():
        return None
    try:
        content = filepath.read_text(encoding="utf-8").strip()
        return content if content else None
    except OSError:
        return None
def main():
    print("=" * 70)
    print(f"PROJECT STATUS SCAN - Last {LOOKBACK_DAYS} Days")
    print(f"Scan date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    # Part 1: Recent file activity
    print("\n" + "=" * 70)
    print("SECTION 1: RECENT FILE ACTIVITY")
    print("=" * 70)

    recent = {}
    if not DATA_DIR.exists():
        print(f"\nData directory does not exist: {DATA_DIR}")
        print("No activity data available.")
    else:
        recent = scan_recent_files(DATA_DIR, LOOKBACK_DAYS)

        if not recent:
            print(f"\nNo files modified in the last {LOOKBACK_DAYS} days.")
            print("This could mean: no active work, or data lives elsewhere.")
        else:
            total_recent = sum(len(files) for files in recent.values())
            print(f"\nFound {total_recent} file(s) modified across {len(recent)} department(s):\n")

            for dept in sorted(recent.keys()):
                files = recent[dept]
                print(f"  --- {dept}/ ({len(files)} file{'s' if len(files) != 1 else ''}) ---")
                print(f"  {'File':<40} {'Modified':<18} {'Age'}")
                print(f"  {'-'*40} {'-'*18} {'-'*10}")
                for f in files:
                    age = f"{f['days_old']}d ago" if f["days_old"] > 0 else "today"
                    print(f"  {f['name']:<40} {f['modified']:<18} {age}")
                print()

    # Part 2: Active projects from CEO memory
    print("=" * 70)
    print("SECTION 2: ACTIVE PROJECTS (from CEO memory)")
    print("=" * 70)

    projects_content = read_active_projects(ACTIVE_PROJECTS_PATH)

    if projects_content is None:
        if not ACTIVE_PROJECTS_PATH.exists():
            print(f"\nActive projects file not found: {ACTIVE_PROJECTS_PATH}")
            print("Tip: Create this file to track active project status.")
        else:
            print("\nActive projects file is empty.")
    else:
        print(f"\nSource: {ACTIVE_PROJECTS_PATH.relative_to(REPO_ROOT)}")
        print("-" * 50)
        for line in projects_content.split("\n"):
            print(f"  {line}")

    # Part 3: Summary
    print(f"\n{'=' * 70}")
    print("SCAN COMPLETE")
    active_depts = sorted(recent.keys()) if recent else []
    total = sum(len(f) for f in recent.values()) if recent else 0
    print(f"  Recent activity: {total} files across {len(active_depts)} departments")
    if active_depts:
        print(f"  Active departments: {', '.join(active_depts)}")

    # Check for departments with NO recent activity
    if DATA_DIR.exists():
        all_depts = list_departments()
        inactive = [d for d in all_depts if d not in active_depts]
        if inactive:
            print(f"  Inactive departments (no changes in {LOOKBACK_DAYS}d): {', '.join(inactive)}")
    print(f"{'=' * 70}")
if __name__ == "__main__":
    main()
