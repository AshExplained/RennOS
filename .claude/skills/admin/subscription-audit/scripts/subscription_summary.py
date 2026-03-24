#!/usr/bin/env python3
"""
Subscription Summary
Reads data/personal/admin/ and data/operations/ for subscription data.
Lists all subscriptions with name, cost, renewal date, and calculates total monthly spend.
Run from repo root: python3 .claude/skills/admin/subscription-audit/scripts/subscription_summary.py
"""

import os
import re
import sys
from datetime import datetime

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../.."))
TODAY = datetime.now().date()

SEARCH_DIRS = [
    os.path.join(REPO_ROOT, "data", "personal", "admin"),
    os.path.join(REPO_ROOT, "data", "operations", "admin"),
    os.path.join(REPO_ROOT, "data", "operations"),
    os.path.join(REPO_ROOT, "data", "admin"),
]

TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[\s\-:]+\|$")
COST_PATTERN = re.compile(r"\$?\s*([\d,]+(?:\.\d{1,2})?)")
DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")


def parse_date(s):
    try:
        return datetime.strptime(s.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def parse_cost(s):
    """Extract a numeric cost from a string like '$9.99' or '29.99/mo'."""
    m = COST_PATTERN.search(s)
    if m:
        return float(m.group(1).replace(",", ""))
    return None


def normalize_to_monthly(cost, raw_text):
    """Attempt to normalize a cost to monthly based on context clues."""
    raw = raw_text.lower()
    if cost is None:
        return None
    if "year" in raw or "annual" in raw or "/yr" in raw or "/y" in raw:
        return round(cost / 12, 2)
    return cost


def scan_file_for_subscriptions(filepath):
    """Parse a markdown file for subscription table data."""
    subscriptions = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError) as e:
        print(f"  [warn] Could not read {filepath}: {e}")
        return subscriptions

    headers = []
    in_table = False

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
            row["_source"] = os.path.basename(filepath)
            subscriptions.append(row)

    return subscriptions


def extract_sub_fields(row):
    """Extract name, cost, and renewal date from a subscription row."""
    name = None
    cost_str = None
    cost_val = None
    renewal_date = None
    raw_cost_text = ""

    for key, val in row.items():
        if key.startswith("_"):
            continue
        kl = key.lower()
        if any(w in kl for w in ["name", "service", "subscription", "provider", "tool"]):
            name = val
        if any(w in kl for w in ["cost", "price", "amount", "fee", "rate"]):
            cost_str = val
            raw_cost_text = val
        if any(w in kl for w in ["renewal", "renew", "billing", "next", "date", "due"]):
            d = parse_date(val)
            if d:
                renewal_date = d

    if not name:
        for key, val in row.items():
            if key.startswith("_"):
                continue
            if val and val.strip():
                name = val
                break

    if cost_str:
        cost_val = parse_cost(cost_str)
        cost_val = normalize_to_monthly(cost_val, raw_cost_text)

    if not renewal_date:
        for key, val in row.items():
            if key.startswith("_"):
                continue
            d = parse_date(val)
            if d:
                renewal_date = d
                break

    return name, cost_val, renewal_date, cost_str


def scan_for_subscription_keywords(filepath):
    """Scan file for lines mentioning subscriptions with costs."""
    items = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError):
        return items

    for i, line in enumerate(lines):
        ll = line.lower()
        if any(kw in ll for kw in ["subscription", "renewal", "monthly", "annual", "$"]):
            cost = parse_cost(line)
            dates = DATE_PATTERN.findall(line)
            items.append({
                "line": line.strip(),
                "line_num": i + 1,
                "cost": cost,
                "dates": dates,
                "file": os.path.basename(filepath),
            })
    return items


def main():
    print("=" * 60)
    print("SUBSCRIPTION SUMMARY")
    print(f"Generated: {TODAY}")
    print("=" * 60)

    active_dirs = []
    for d in SEARCH_DIRS:
        if os.path.isdir(d):
            active_dirs.append(d)

    if not active_dirs:
        print(f"\n[!] No subscription data directories found.")
        print("    Searched:")
        for d in SEARCH_DIRS:
            print(f"      {os.path.relpath(d, REPO_ROOT)}")
        print("\n    Create one of these directories and add subscription data files.")
        print("    Expected format: Markdown table with columns like")
        print("    | Service | Cost | Billing Date | Renewal Date | Status |")
        sys.exit(0)

    md_files = []
    for d in active_dirs:
        for entry in sorted(os.listdir(d)):
            full = os.path.join(d, entry)
            if os.path.isfile(full) and entry.endswith(".md"):
                md_files.append(full)

    if not md_files:
        print(f"\n[!] No markdown files found in subscription data directories.")
        print("    Add subscription tracker files (.md) to get started.")
        sys.exit(0)

    print(f"\nScanning {len(md_files)} file(s) across {len(active_dirs)} director(y/ies)...\n")

    all_subs = []
    unstructured_refs = []

    for fpath in md_files:
        subs = scan_file_for_subscriptions(fpath)
        if subs:
            all_subs.extend(subs)
        else:
            refs = scan_for_subscription_keywords(fpath)
            unstructured_refs.extend(refs)

    if all_subs:
        total_monthly = 0.0
        known_cost_count = 0

        print(f"{'Service':<30} {'Monthly Cost':>12}   {'Renewal Date':<12}   Source")
        print("-" * 80)

        for sub in all_subs:
            name, cost, renewal, raw_cost = extract_sub_fields(sub)
            display_name = (name or "Unknown")[:30]
            display_cost = f"${cost:.2f}" if cost is not None else (raw_cost or "N/A")
            display_date = str(renewal) if renewal else "N/A"
            source = sub.get("_source", "")

            flag = ""
            if renewal:
                days_until = (renewal - TODAY).days
                if 0 <= days_until <= 7:
                    flag = " [RENEWING SOON]"
                elif days_until < 0:
                    flag = " [PAST DUE]"

            print(f"  {display_name:<28} {display_cost:>12}   {display_date:<12}   {source}{flag}")

            if cost is not None:
                total_monthly += cost
                known_cost_count += 1

        print()
        print(f"--- SPEND SUMMARY ---")
        print(f"Subscriptions found:  {len(all_subs)}")
        print(f"With known costs:     {known_cost_count}")
        print(f"Total monthly spend:  ${total_monthly:.2f}")
        print(f"Projected annual:     ${total_monthly * 12:.2f}")

        if known_cost_count < len(all_subs):
            print(f"\n[!] {len(all_subs) - known_cost_count} subscription(s) missing cost data.")

    elif unstructured_refs:
        print(f"[i] No structured subscription tables found, but {len(unstructured_refs)} "
              f"subscription-related reference(s) detected:\n")
        for ref in unstructured_refs:
            cost_info = f" (${ref['cost']:.2f})" if ref["cost"] else ""
            print(f"  [{ref['file']}:{ref['line_num']}] {ref['line']}{cost_info}")
    else:
        print("[i] No subscription data found in any scanned files.")
        print("    Add a subscription tracker to data/personal/admin/renewal-tracker.md")
        print("    Format: | Service | Monthly Cost | Renewal Date | Auto-Renew | Status |")

    print()


if __name__ == "__main__":
    main()
