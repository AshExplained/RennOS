#!/usr/bin/env python3
"""Scan data/ for recently modified files (last 7 days).

Groups results by department. Also checks .claude/ceo-memory/active_projects.md
for the active project list.
"""

import os
from datetime import datetime, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
DATA_DIR = REPO_ROOT / "data"
ACTIVE_PROJECTS_PATH = REPO_ROOT / ".claude" / "ceo-memory" / "active_projects.md"
LOOKBACK_DAYS = 7


def scan_recent_files(base_dir: Path, days: int) -> dict:
    """Scan for files modified within the last N days, grouped by department."""
    cutoff = datetime.now() - timedelta(days=days)
    departments: dict[str, list[dict]] = {}

    if not base_dir.exists():
        return departments

    for item in base_dir.rglob("*"):
        if not item.is_file():
            continue
        if item.name in (".gitkeep", ".DS_Store"):
            continue

        stat = item.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        if mod_time < cutoff:
            continue

        # Determine department from path
        rel = item.relative_to(base_dir)
        parts = rel.parts
        dept = parts[0] if parts else "(root)"

        departments.setdefault(dept, []).append({
            "name": item.name,
            "path": str(item.relative_to(REPO_ROOT)),
            "modified": mod_time.strftime("%Y-%m-%d %H:%M"),
            "days_ago": (datetime.now() - mod_time).days,
        })

    # Sort each department's files by most recent first
    for dept in departments:
        departments[dept].sort(key=lambda x: x["days_ago"])

    return departments


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
                    age = f"{f['days_ago']}d ago" if f["days_ago"] > 0 else "today"
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
        # Print content with indentation
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
        all_depts = sorted([d.name for d in DATA_DIR.iterdir() if d.is_dir() and d.name != ".DS_Store"])
        inactive = [d for d in all_depts if d not in active_depts]
        if inactive:
            print(f"  Inactive departments (no changes in {LOOKBACK_DAYS}d): {', '.join(inactive)}")
    print(f"{'=' * 70}")


if __name__ == "__main__":
    main()
