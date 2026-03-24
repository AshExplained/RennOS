#!/usr/bin/env python3
"""
Calendar Merger
Scans for calendar files across all departments in data/*/.
Merges dates into a single chronological list.
Run from repo root: python3 .claude/skills/ops/master-calendar/scripts/merge_calendars.py
"""

import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
DATA_DIR = os.path.join(REPO_ROOT, "data")
TODAY = datetime.now().date()

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[\s\-:]+\|$")


def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def find_calendar_files(data_dir):
    """Recursively find files with 'calendar' in the name under data/."""
    calendar_files = []
    if not os.path.isdir(data_dir):
        return calendar_files

    for root, dirs, files in os.walk(data_dir):
        dirs[:] = [d for d in dirs if d not in ("archive", ".git")]
        for f in files:
            if "calendar" in f.lower() and f.endswith(".md"):
                calendar_files.append(os.path.join(root, f))

    return sorted(calendar_files)


def extract_events_from_table(filepath):
    """Extract events from markdown tables in a file."""
    events = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError) as e:
        print(f"  [warn] Could not read {filepath}: {e}")
        return events

    headers = []
    in_table = False
    rel_path = os.path.relpath(filepath, REPO_ROOT)
    dept = os.path.relpath(filepath, DATA_DIR).split(os.sep)[0]

    for line in lines:
        line = line.strip()
        if not line:
            in_table = False
            headers = []
            continue

        row_match = TABLE_ROW_PATTERN.match(line)
        if not row_match:
            in_table = False
            headers = []
            continue

        if SEPARATOR_PATTERN.match(line):
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
                events.append({
                    "date": event_date,
                    "description": event_desc or "(no description)",
                    "department": dept,
                    "source": rel_path,
                })

    return events


def extract_events_from_lines(filepath):
    """Extract date-referenced events from non-table content."""
    events = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError):
        return events

    rel_path = os.path.relpath(filepath, REPO_ROOT)
    dept = os.path.relpath(filepath, DATA_DIR).split(os.sep)[0]

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("<!--"):
            continue
        dates = DATE_PATTERN.findall(stripped)
        for ds in dates:
            d = parse_date(ds)
            if d:
                desc = stripped.replace(ds, "").strip(" -|:")
                events.append({
                    "date": d,
                    "description": desc or stripped,
                    "department": dept,
                    "source": rel_path,
                })

    return events


def main():
    print("=" * 70)
    print("MERGED CALENDAR VIEW")
    print(f"Generated: {TODAY}")
    print("=" * 70)

    if not os.path.isdir(DATA_DIR):
        print(f"\n[!] Data directory not found: {DATA_DIR}")
        print("    Create data/ and add department calendar files to merge.")
        sys.exit(0)

    calendar_files = find_calendar_files(DATA_DIR)

    if not calendar_files:
        print(f"\n[!] No calendar files found in {DATA_DIR}")
        print("    Calendar files should have 'calendar' in the filename (e.g., content-calendar.md)")
        print("    Add calendar files to department subdirectories under data/")
        sys.exit(0)

    print(f"\nFound {len(calendar_files)} calendar file(s):\n")
    for cf in calendar_files:
        print(f"  {os.path.relpath(cf, REPO_ROOT)}")

    all_events = []
    for cf in calendar_files:
        table_events = extract_events_from_table(cf)
        if table_events:
            all_events.extend(table_events)
        else:
            line_events = extract_events_from_lines(cf)
            all_events.extend(line_events)

    if not all_events:
        print(f"\n[i] Calendar files found but no dated events detected.")
        print("    Add events with dates in YYYY-MM-DD format to your calendar files.")
        print("    Table format works best:")
        print("    | Date | Event | Department | Status |")
        sys.exit(0)

    all_events.sort(key=lambda e: e["date"])

    past = [e for e in all_events if e["date"] < TODAY]
    today_events = [e for e in all_events if e["date"] == TODAY]
    future = [e for e in all_events if e["date"] > TODAY]

    def print_event(event):
        date_str = str(event["date"])
        dept = event["department"]
        desc = event["description"][:50]
        print(f"  {date_str}  [{dept:<12}] {desc}")

    if today_events:
        print(f"\n--- TODAY ({TODAY}) ---")
        for e in today_events:
            print_event(e)

    if future:
        print(f"\n--- UPCOMING ({len(future)} events) ---")
        for e in future[:30]:
            print_event(e)
        if len(future) > 30:
            print(f"  ... and {len(future) - 30} more")

    if past:
        print(f"\n--- PAST ({len(past)} events, showing last 10) ---")
        for e in past[-10:]:
            print_event(e)

    depts = {}
    for e in all_events:
        depts.setdefault(e["department"], 0)
        depts[e["department"]] += 1

    print(f"\n--- DEPARTMENT BREAKDOWN ---")
    for dept, count in sorted(depts.items()):
        print(f"  {dept:<20} {count} event(s)")

    print(f"\nTotal events across all calendars: {len(all_events)}")
    print()


if __name__ == "__main__":
    main()
