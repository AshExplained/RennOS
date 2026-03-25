#!/usr/bin/env python3
"""Scan all data/*/ directories for the most recent files.

Lists what data is available per department with file names and last
modified dates. Summarizes data freshness.
"""

import sys
from scripts.lib.paths import DATA_DIR
from scripts.lib.data_scanner import scan_directory, list_departments
def main():
    print("=" * 70)
    print("KPI DATA AVAILABILITY - DEPARTMENT SCAN")
    print("=" * 70)

    if not DATA_DIR.exists():
        print(f"\nData directory does not exist: {DATA_DIR}")
        print("No department data available yet.")
        return

    dept_names = list_departments()

    if not dept_names:
        print("\nNo department directories found in data/")
        print("Tip: Create directories like data/analytics/, data/content/, etc.")
        return

    dept_summaries = []
    total_files = 0

    for dept_name in dept_names:
        dept_dir = DATA_DIR / dept_name
        files = scan_directory(dept_dir)

        print(f"\n--- {dept_name}/ ---")

        if not files:
            print("  No data files found.")
            dept_summaries.append({"name": dept_name, "count": 0, "freshness": "EMPTY"})
            continue

        # Sort by most recently modified
        files.sort(key=lambda x: x["days_old"])
        most_recent = files[0]

        print(f"  {'File':<40} {'Modified':<18} {'Freshness'}")
        print(f"  {'-'*40} {'-'*18} {'-'*10}")
        for f in files[:10]:  # Show top 10 most recent per dept
            print(f"  {f['name']:<40} {f['modified']:<18} {f['freshness']}")
        if len(files) > 10:
            print(f"  ... and {len(files) - 10} more files")

        total_files += len(files)
        dept_summaries.append({
            "name": dept_name,
            "count": len(files),
            "freshness": most_recent["freshness"],
            "most_recent_date": most_recent["modified"],
        })

    # Summary table
    print(f"\n{'=' * 70}")
    print("DATA FRESHNESS SUMMARY")
    print(f"{'=' * 70}")
    print(f"  {'Department':<20} {'Files':<8} {'Most Recent':<18} {'Status'}")
    print(f"  {'-'*20} {'-'*8} {'-'*18} {'-'*10}")
    for s in dept_summaries:
        if s["count"] == 0:
            print(f"  {s['name']:<20} {'0':<8} {'N/A':<18} EMPTY")
        else:
            print(f"  {s['name']:<20} {s['count']:<8} {s['most_recent_date']:<18} {s['freshness']}")

    print(f"\n  Total data files across all departments: {total_files}")

    # Freshness warnings
    stale_depts = [s for s in dept_summaries if s.get("freshness") in ("STALE", "OUTDATED")]
    if stale_depts:
        print(f"\n  Warning: {len(stale_depts)} department(s) have stale/outdated data:")
        for s in stale_depts:
            print(f"    - {s['name']} (last updated: {s.get('most_recent_date', 'N/A')})")

    empty_depts = [s for s in dept_summaries if s["count"] == 0]
    if empty_depts:
        print(f"\n  Note: {len(empty_depts)} department(s) have no data files:")
        for s in empty_depts:
            print(f"    - {s['name']}")

    print(f"{'=' * 70}")
if __name__ == "__main__":
    main()
