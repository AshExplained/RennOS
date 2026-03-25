#!/usr/bin/env python3
"""
Deadline Scanner
Scans data/ recursively for files containing date patterns (YYYY-MM-DD).
Flags items within 7 days (urgent) and 30 days (upcoming).
Run from repo root: python3 .claude/skills/ops/deadline-check/scripts/deadline_scanner.py
"""

import os
import re
import sys
from datetime import datetime, timedelta
from scripts.lib.paths import REPO_ROOT, DATA_DIR
TODAY = datetime.now().date()

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")

SKIP_DIRS = {"archive", ".git", "node_modules", "__pycache__"}

DEADLINE_KEYWORDS = [
    "deadline", "due", "deliver", "launch", "release", "publish",
    "submit", "review", "milestone", "ship", "complete", "expire",
    "renewal", "renew", "cancel",
]
def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
def scan_file(filepath):
    """Scan a file for date references and return deadline items."""
    items = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError, UnicodeDecodeError):
        return items

    rel_path = os.path.relpath(filepath, REPO_ROOT)

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("<!--"):
            continue

        dates = DATE_PATTERN.findall(stripped)
        for date_str in dates:
            d = parse_date(date_str)
            if not d:
                continue

            context = stripped.replace(date_str, "").strip(" -|:*#>")
            if not context:
                context = stripped

            line_lower = stripped.lower()
            is_deadline_context = any(kw in line_lower for kw in DEADLINE_KEYWORDS)

            items.append({
                "date": d,
                "context": context[:80],
                "source": rel_path,
                "line_num": i + 1,
                "is_deadline": is_deadline_context,
            })

    return items
def main():
    print("=" * 70)
    print("DEADLINE SCANNER")
    print(f"Generated: {TODAY}")
    print(f"Scanning:  data/ (recursively)")
    print("=" * 70)

    if not os.path.isdir(DATA_DIR):
        print(f"\n[!] Data directory not found: {DATA_DIR}")
        print("    Create data/ and add files with dates in YYYY-MM-DD format.")
        sys.exit(0)

    all_items = []
    file_count = 0

    for root, dirs, files in os.walk(DATA_DIR):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            file_count += 1
            fpath = os.path.join(root, f)
            items = scan_file(fpath)
            all_items.extend(items)

    if file_count == 0:
        print(f"\n[!] No markdown files found in {DATA_DIR}")
        print("    Add files with deadline dates in YYYY-MM-DD format.")
        sys.exit(0)

    print(f"\nScanned {file_count} file(s), found {len(all_items)} date reference(s).\n")

    if not all_items:
        print("[i] No date references (YYYY-MM-DD) found in any data files.")
        print("    Add dates to your files to enable deadline tracking.")
        sys.exit(0)

    overdue = []
    today_items = []
    urgent = []
    upcoming = []
    later = []
    past = []

    for item in all_items:
        d = item["date"]
        delta = (d - TODAY).days

        if delta < 0:
            if item["is_deadline"]:
                overdue.append(item)
            else:
                past.append(item)
        elif delta == 0:
            today_items.append(item)
        elif delta <= 7:
            urgent.append(item)
        elif delta <= 30:
            upcoming.append(item)
        else:
            later.append(item)

    overdue.sort(key=lambda x: x["date"])
    today_items.sort(key=lambda x: x["date"])
    urgent.sort(key=lambda x: x["date"])
    upcoming.sort(key=lambda x: x["date"])

    def print_item(item, show_days=True):
        d = item["date"]
        delta = (d - TODAY).days
        days_str = ""
        if show_days:
            if delta < 0:
                days_str = f" [{-delta}d OVERDUE]"
            elif delta == 0:
                days_str = " [TODAY]"
            else:
                days_str = f" [in {delta}d]"

        deadline_marker = " *" if item["is_deadline"] else ""
        print(f"  {d}  {item['context']:<50}{days_str}")
        print(f"           {item['source']}:{item['line_num']}{deadline_marker}")

    if overdue:
        print(f"!!! OVERDUE ({len(overdue)}) !!!")
        for item in overdue:
            print_item(item)
        print()

    if today_items:
        print(f"*** TODAY ({len(today_items)}) ***")
        for item in today_items:
            print_item(item, show_days=False)
        print()

    if urgent:
        print(f">> URGENT - Next 7 Days ({len(urgent)}) <<")
        for item in urgent:
            print_item(item)
        print()

    if upcoming:
        print(f"-- UPCOMING - Next 30 Days ({len(upcoming)}) --")
        for item in upcoming:
            print_item(item)
        print()

    if later:
        print(f"   LATER ({len(later)} items beyond 30 days, showing first 10)")
        for item in sorted(later, key=lambda x: x["date"])[:10]:
            print_item(item)
        if len(later) > 10:
            print(f"  ... and {len(later) - 10} more")
        print()

    print("--- SUMMARY ---")
    print(f"Overdue (deadline keywords):  {len(overdue)}")
    print(f"Due today:                    {len(today_items)}")
    print(f"Urgent (next 7 days):         {len(urgent)}")
    print(f"Upcoming (next 30 days):      {len(upcoming)}")
    print(f"Later (30+ days):             {len(later)}")
    print(f"Past references:              {len(past)}")

    if overdue:
        print(f"\n[!] ACTION NEEDED: {len(overdue)} overdue deadline(s) detected!")
    if urgent:
        print(f"[!] HEADS UP: {len(urgent)} item(s) due within 7 days.")

    print()
if __name__ == "__main__":
    main()
