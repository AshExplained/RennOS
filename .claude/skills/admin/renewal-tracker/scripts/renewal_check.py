#!/usr/bin/env python3
"""
Renewal Checker
Reads data/personal/admin/ for subscription/renewal data.
Flags renewals due within 7 days (urgent) and 30 days (upcoming).
Run from repo root: python3 .claude/skills/admin/renewal-tracker/scripts/renewal_check.py
"""

import os
import re
import sys
from datetime import datetime, timedelta

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
TODAY = datetime.now().date()

SEARCH_DIRS = [
    os.path.join(REPO_ROOT, "data", "personal", "admin"),
    os.path.join(REPO_ROOT, "data", "operations", "admin"),
    os.path.join(REPO_ROOT, "data", "admin"),
]

RENEWAL_FILES = [
    os.path.join(REPO_ROOT, "data", "personal", "admin", "renewal-tracker.md"),
    os.path.join(REPO_ROOT, "data", "operations", "admin", "renewal-tracker.md"),
]

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[\s\-:]+\|$")
COST_PATTERN = re.compile(r"\$?\s*([\d,]+(?:\.\d{1,2})?)")


def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def parse_cost(s):
    m = COST_PATTERN.search(s)
    if m:
        return float(m.group(1).replace(",", ""))
    return None


def scan_file_for_renewals(filepath):
    """Parse markdown file for renewal/subscription table rows."""
    renewals = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError) as e:
        print(f"  [warn] Could not read {filepath}: {e}")
        return renewals

    headers = []
    in_table = False
    rel_path = os.path.relpath(filepath, REPO_ROOT)

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
            row["_source"] = rel_path
            renewals.append(row)

    return renewals


def scan_file_for_date_refs(filepath):
    """Scan file for lines with dates and renewal-related keywords."""
    items = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError):
        return items

    rel_path = os.path.relpath(filepath, REPO_ROOT)
    renewal_keywords = ["renew", "subscription", "cancel", "expire", "billing", "auto"]

    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("<!--"):
            continue
        ll = stripped.lower()
        if any(kw in ll for kw in renewal_keywords):
            dates = DATE_PATTERN.findall(stripped)
            for ds in dates:
                d = parse_date(ds)
                if d:
                    items.append({
                        "date": d,
                        "context": stripped[:80],
                        "source": rel_path,
                        "line_num": i + 1,
                    })

    return items


def extract_renewal_info(row):
    """Extract service name, renewal date, cost, and auto-renew from a row."""
    name = None
    renewal_date = None
    cost = None
    auto_renew = None
    cancel_deadline = None

    for key, val in row.items():
        if key.startswith("_"):
            continue
        kl = key.lower()

        if any(w in kl for w in ["name", "service", "subscription", "provider", "tool"]):
            name = val
        if any(w in kl for w in ["renewal", "renew", "next"]):
            d = parse_date(val)
            if d:
                renewal_date = d
        if any(w in kl for w in ["cost", "price", "amount", "fee"]):
            cost = parse_cost(val)
        if "auto" in kl:
            auto_renew = val.lower() in ("yes", "true", "y", "on")
        if "cancel" in kl:
            d = parse_date(val)
            if d:
                cancel_deadline = d

    if not name:
        for key, val in row.items():
            if key.startswith("_"):
                continue
            if val and val.strip():
                name = val
                break

    if not renewal_date:
        for key, val in row.items():
            if key.startswith("_"):
                continue
            d = parse_date(val)
            if d:
                renewal_date = d
                break

    return name, renewal_date, cost, auto_renew, cancel_deadline


def main():
    print("=" * 60)
    print("RENEWAL CHECK")
    print(f"Generated: {TODAY}")
    print("=" * 60)

    active_dirs = []
    for d in SEARCH_DIRS:
        if os.path.isdir(d):
            active_dirs.append(d)

    specific_files = []
    for rf in RENEWAL_FILES:
        if os.path.isfile(rf):
            specific_files.append(rf)

    if not active_dirs and not specific_files:
        print(f"\n[!] No renewal data directories or files found.")
        print("    Searched:")
        for d in SEARCH_DIRS:
            print(f"      {os.path.relpath(d, REPO_ROOT)}")
        print("\n    Create data/personal/admin/renewal-tracker.md with a table like:")
        print("    | Service | Renewal Date | Cost | Auto-Renew | Cancel Deadline |")
        sys.exit(0)

    md_files = set()
    for rf in specific_files:
        md_files.add(rf)
    for d in active_dirs:
        for entry in sorted(os.listdir(d)):
            full = os.path.join(d, entry)
            if os.path.isfile(full) and entry.endswith(".md"):
                md_files.add(full)

    md_files = sorted(md_files)

    if not md_files:
        print(f"\n[!] No markdown files found in data directories.")
        print("    Add renewal tracker files (.md) to get started.")
        sys.exit(0)

    print(f"\nScanning {len(md_files)} file(s)...\n")

    all_renewals = []
    unstructured = []

    for fpath in md_files:
        renewals = scan_file_for_renewals(fpath)
        if renewals:
            all_renewals.extend(renewals)
        else:
            refs = scan_file_for_date_refs(fpath)
            unstructured.extend(refs)

    if all_renewals:
        urgent = []
        upcoming = []
        later = []
        past_due = []
        no_date = []

        for row in all_renewals:
            name, renewal_date, cost, auto_renew, cancel_deadline = extract_renewal_info(row)

            entry = {
                "name": name or "Unknown",
                "date": renewal_date,
                "cost": cost,
                "auto_renew": auto_renew,
                "cancel_deadline": cancel_deadline,
                "source": row.get("_source", ""),
            }

            if not renewal_date:
                no_date.append(entry)
                continue

            days_until = (renewal_date - TODAY).days

            if days_until < 0:
                entry["days"] = days_until
                past_due.append(entry)
            elif days_until <= 7:
                entry["days"] = days_until
                urgent.append(entry)
            elif days_until <= 30:
                entry["days"] = days_until
                upcoming.append(entry)
            else:
                entry["days"] = days_until
                later.append(entry)

        urgent.sort(key=lambda x: x["date"])
        upcoming.sort(key=lambda x: x["date"])
        past_due.sort(key=lambda x: x["date"])
        later.sort(key=lambda x: x["date"])

        def format_entry(entry):
            cost_str = f"${entry['cost']:.2f}" if entry["cost"] else "N/A"
            auto_str = ""
            if entry["auto_renew"] is not None:
                auto_str = " [AUTO-RENEW]" if entry["auto_renew"] else " [MANUAL]"
            cancel_str = ""
            if entry["cancel_deadline"]:
                cancel_days = (entry["cancel_deadline"] - TODAY).days
                if cancel_days <= 0:
                    cancel_str = " !! CANCEL DEADLINE PASSED !!"
                elif cancel_days <= 7:
                    cancel_str = f" ! Cancel by {entry['cancel_deadline']} ({cancel_days}d left)"
            days_str = ""
            if "days" in entry:
                d = entry["days"]
                if d < 0:
                    days_str = f" ({-d}d overdue)"
                elif d == 0:
                    days_str = " (TODAY)"
                else:
                    days_str = f" (in {d}d)"

            return (f"  {entry['name']:<25} {str(entry['date'] or 'N/A'):<12} "
                    f"{cost_str:>10}{auto_str}{cancel_str}{days_str}")

        if past_due:
            print(f"!!! PAST DUE ({len(past_due)}) !!!")
            for e in past_due:
                print(format_entry(e))
            print()

        if urgent:
            print(f">> URGENT - Renewing Within 7 Days ({len(urgent)}) <<")
            for e in urgent:
                print(format_entry(e))
            print()

        if upcoming:
            print(f"-- UPCOMING - Renewing Within 30 Days ({len(upcoming)}) --")
            for e in upcoming:
                print(format_entry(e))
            print()

        if later:
            print(f"   LATER ({len(later)} renewal(s) beyond 30 days)")
            for e in later[:10]:
                print(format_entry(e))
            if len(later) > 10:
                print(f"  ... and {len(later) - 10} more")
            print()

        if no_date:
            print(f"[?] NO DATE ({len(no_date)} renewal(s) missing dates)")
            for e in no_date:
                cost_str = f"${e['cost']:.2f}" if e["cost"] else "N/A"
                print(f"  {e['name']:<25} {'N/A':<12} {cost_str:>10}")
            print()

        print("--- SUMMARY ---")
        print(f"Past due:     {len(past_due)}")
        print(f"Urgent (7d):  {len(urgent)}")
        print(f"Upcoming:     {len(upcoming)}")
        print(f"Later:        {len(later)}")
        print(f"No date:      {len(no_date)}")
        print(f"Total:        {len(all_renewals)}")

        if urgent:
            print(f"\n[!] ACTION NEEDED: {len(urgent)} renewal(s) due within 7 days!")
        if past_due:
            print(f"[!] {len(past_due)} renewal(s) appear past due -- verify status.")

    elif unstructured:
        print(f"[i] No structured renewal tables found, but {len(unstructured)} "
              f"renewal-related reference(s) detected:\n")
        for ref in sorted(unstructured, key=lambda x: x["date"]):
            delta = (ref["date"] - TODAY).days
            if delta < 0:
                label = f"PAST ({-delta}d ago)"
            elif delta <= 7:
                label = f"URGENT (in {delta}d)"
            elif delta <= 30:
                label = f"UPCOMING (in {delta}d)"
            else:
                label = f"LATER (in {delta}d)"
            print(f"  [{label}] {ref['date']} - {ref['context']}")
            print(f"           {ref['source']}:{ref['line_num']}")
    else:
        print("[i] No renewal data found in any scanned files.")
        print("    Create data/personal/admin/renewal-tracker.md with a table like:")
        print("    | Service | Renewal Date | Cost | Auto-Renew | Cancel Deadline |")

    print()


if __name__ == "__main__":
    main()
