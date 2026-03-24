#!/usr/bin/env python3
"""
Calendar Conflict Checker
Reads all calendar files in data/. Parses dates and looks for overlapping events
on the same date across different departments.
Run from repo root: python3 .claude/skills/ops/conflict-check/scripts/calendar_conflict_check.py
"""

import os
import re
import sys
from collections import defaultdict
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
DATA_DIR = os.path.join(REPO_ROOT, "data")
TODAY = datetime.now().date()

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[\s\-:]+\|$")

SKIP_DIRS = {"archive", ".git", "node_modules", "__pycache__"}


def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def find_schedule_files(data_dir):
    """Find files with calendar/schedule/roadmap keywords."""
    files = []
    if not os.path.isdir(data_dir):
        return files
    keywords = ["calendar", "schedule", "roadmap", "timeline", "milestone"]
    for root, dirs, fnames in os.walk(data_dir):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in fnames:
            if any(kw in f.lower() for kw in keywords) and f.endswith(".md"):
                files.append(os.path.join(root, f))
    return sorted(set(files))


def extract_events(filepath):
    """Extract all dated events from a file."""
    events = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError, UnicodeDecodeError):
        return events

    rel_path = os.path.relpath(filepath, REPO_ROOT)
    dept = os.path.relpath(filepath, DATA_DIR).split(os.sep)[0]

    headers = []
    in_table = False
    table_events = []

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            in_table = False
            headers = []
            continue

        row_match = TABLE_ROW_PATTERN.match(stripped)
        if not row_match:
            if not stripped.startswith("#") and not stripped.startswith("<!--"):
                dates = DATE_PATTERN.findall(stripped)
                for ds in dates:
                    d = parse_date(ds)
                    if d:
                        desc = stripped.replace(ds, "").strip(" -|:*#>")
                        events.append({
                            "date": d,
                            "description": desc or stripped,
                            "department": dept,
                            "source": rel_path,
                            "line_num": i + 1,
                        })
            in_table = False
            headers = []
            continue

        if SEPARATOR_PATTERN.match(stripped):
            in_table = True
            continue

        cells = [c.strip() for c in row_match.group(1).split("|")]

        if not in_table:
            headers = [h.lower() for h in cells]
            continue

        if headers and len(cells) >= len(headers):
            row = dict(zip(headers, cells))
            event_date = None
            event_desc = None

            for key, val in row.items():
                d = parse_date(val)
                if d:
                    event_date = d
                if any(w in key for w in ["event", "title", "task", "item", "description",
                                           "name", "milestone", "content", "topic"]):
                    event_desc = val

            if not event_desc:
                for key, val in row.items():
                    if val and not parse_date(val) and val.strip("-"):
                        event_desc = val
                        break

            if event_date:
                table_events.append({
                    "date": event_date,
                    "description": event_desc or "(no description)",
                    "department": dept,
                    "source": rel_path,
                    "line_num": i + 1,
                })

    if table_events:
        return table_events
    return events


def main():
    print("=" * 70)
    print("CALENDAR CONFLICT CHECK")
    print(f"Generated: {TODAY}")
    print("=" * 70)

    if not os.path.isdir(DATA_DIR):
        print(f"\n[!] Data directory not found: {DATA_DIR}")
        print("    Create data/ and add calendar/schedule files.")
        sys.exit(0)

    all_files = find_schedule_files(DATA_DIR)

    if not all_files:
        print(f"\n[!] No calendar/schedule files found in {DATA_DIR}")
        print("    Files should have 'calendar', 'schedule', 'roadmap', 'timeline',")
        print("    or 'milestone' in the filename.")
        sys.exit(0)

    print(f"\nScanning {len(all_files)} file(s):\n")
    for f in all_files:
        print(f"  {os.path.relpath(f, REPO_ROOT)}")

    all_events = []
    for fpath in all_files:
        events = extract_events(fpath)
        all_events.extend(events)

    if not all_events:
        print(f"\n[i] No dated events found in any calendar files.")
        print("    Add events with dates in YYYY-MM-DD format.")
        sys.exit(0)

    print(f"\nFound {len(all_events)} event(s) total.\n")

    by_date = defaultdict(list)
    for event in all_events:
        by_date[event["date"]].append(event)

    conflicts = []
    overload_dates = []

    for date, events in sorted(by_date.items()):
        if len(events) < 2:
            continue

        departments = set(e["department"] for e in events)
        sources = set(e["source"] for e in events)

        if len(departments) > 1:
            conflicts.append({
                "date": date,
                "events": events,
                "type": "cross-department",
                "departments": departments,
            })
        elif len(sources) > 1:
            conflicts.append({
                "date": date,
                "events": events,
                "type": "same-department",
                "departments": departments,
            })

        if len(events) >= 3:
            overload_dates.append({
                "date": date,
                "count": len(events),
                "events": events,
            })

    if not conflicts and not overload_dates:
        print("--- NO CONFLICTS DETECTED ---")
        print("Schedule is clean across all scanned calendars.")
    else:
        if conflicts:
            print(f"!!! CONFLICTS FOUND: {len(conflicts)} date(s) with overlapping events !!!\n")

            for i, conflict in enumerate(conflicts, 1):
                d = conflict["date"]
                delta = (d - TODAY).days
                time_label = ""
                if delta < 0:
                    time_label = f" (PAST - {-delta}d ago)"
                elif delta == 0:
                    time_label = " (TODAY)"
                else:
                    time_label = f" (in {delta}d)"

                ctype = "CROSS-DEPARTMENT" if conflict["type"] == "cross-department" else "SAME DEPT"
                depts = ", ".join(sorted(conflict["departments"]))

                print(f"  Conflict #{i}: {d}{time_label} [{ctype}]")
                print(f"  Departments: {depts}")
                for event in conflict["events"]:
                    print(f"    - {event['description'][:60]}")
                    print(f"      Source: {event['source']}:{event['line_num']}")
                print(f"  Recommendation: Review and reschedule if these require the user's attention.")
                print()

        if overload_dates:
            print(f"--- OVERLOAD DATES ({len(overload_dates)}) ---")
            print("Days with 3+ events that may be too packed:\n")
            for od in sorted(overload_dates, key=lambda x: x["date"]):
                d = od["date"]
                delta = (d - TODAY).days
                time_label = f"in {delta}d" if delta >= 0 else f"{-delta}d ago"
                print(f"  {d} ({time_label}): {od['count']} events")
                for e in od["events"]:
                    print(f"    - [{e['department']}] {e['description'][:50]}")
            print()

    all_dates = sorted(by_date.keys())
    future_dates = [d for d in all_dates if d >= TODAY]

    print("--- SUMMARY ---")
    print(f"Total events scanned:    {len(all_events)}")
    print(f"Unique dates:            {len(all_dates)}")
    print(f"Conflict dates:          {len(conflicts)}")
    print(f"Overload dates (3+):     {len(overload_dates)}")
    if future_dates:
        print(f"Next event:              {future_dates[0]}")
        print(f"Last scheduled event:    {future_dates[-1]}")

    print()


if __name__ == "__main__":
    main()
