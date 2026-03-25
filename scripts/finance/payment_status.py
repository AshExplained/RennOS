#!/usr/bin/env python3
"""
Payment Status Scanner
Reads data/finance/ for invoice/payment files and lists outstanding/overdue items.
Run from repo root: python3 .claude/skills/finance/payment-tracker/scripts/payment_status.py
"""

import os
import re
import sys
from datetime import datetime, timedelta
from scripts.lib.paths import REPO_ROOT, FINANCE_DIR
TODAY = datetime.now().date()

DATE_PATTERN = re.compile(r"\b(\d{4}-\d{2}-\d{2})\b")
TABLE_ROW_PATTERN = re.compile(r"^\|(.+)\|$")
SEPARATOR_PATTERN = re.compile(r"^\|[\s\-:]+\|$")
def parse_date(date_str):
    """Parse a YYYY-MM-DD date string, return date or None."""
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None
def scan_file_for_invoices(filepath):
    """Scan a markdown file for invoice/payment table rows."""
    invoices = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError) as e:
        print(f"  [warn] Could not read {filepath}: {e}")
        return invoices

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
            row_data = dict(zip(headers, cells))
            invoices.append(row_data)

    return invoices
def classify_invoice(row):
    """Classify an invoice row as paid, overdue, or outstanding."""
    status = ""
    due_date = None

    for key in row:
        if "status" in key:
            status = row[key].lower()
        if "due" in key:
            due_date = parse_date(row[key])

    if "paid" in status:
        return "paid", due_date

    if due_date and due_date < TODAY:
        return "overdue", due_date
    elif due_date:
        return "outstanding", due_date
    else:
        for key in row:
            d = parse_date(row[key])
            if d:
                due_date = d
                break
        if due_date and due_date < TODAY and "paid" not in status:
            return "overdue", due_date
        return "unknown", due_date
def scan_for_date_references(filepath):
    """Scan file for any date references and associated context lines."""
    items = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except (IOError, OSError):
        return items

    for i, line in enumerate(lines):
        dates = DATE_PATTERN.findall(line)
        for date_str in dates:
            d = parse_date(date_str)
            if d:
                items.append({
                    "date": d,
                    "context": line.strip(),
                    "file": os.path.basename(filepath),
                    "line_num": i + 1,
                })
    return items
def main():
    print("=" * 60)
    print("PAYMENT STATUS REPORT")
    print(f"Generated: {TODAY}")
    print("=" * 60)

    if not os.path.isdir(FINANCE_DIR):
        print(f"\n[!] Finance data directory not found: {FINANCE_DIR}")
        print("    Create data/finance/ and add invoice/payment files to track payments.")
        print("    Expected format: Markdown tables with columns like")
        print("    | Client | Invoice | Amount | Due Date | Status |")
        sys.exit(0)

    md_files = []
    for entry in sorted(os.listdir(FINANCE_DIR)):
        full = os.path.join(FINANCE_DIR, entry)
        if os.path.isfile(full) and entry.endswith(".md"):
            md_files.append(full)

    if not md_files:
        print(f"\n[!] No markdown files found in {FINANCE_DIR}")
        print("    Add invoice or payment tracker files (.md) to get started.")
        sys.exit(0)

    print(f"\nScanning {len(md_files)} file(s) in data/finance/...\n")

    all_invoices = []
    all_date_refs = []

    for fpath in md_files:
        fname = os.path.basename(fpath)
        invoices = scan_file_for_invoices(fpath)
        if invoices:
            for inv in invoices:
                inv["_source"] = fname
            all_invoices.extend(invoices)
        else:
            refs = scan_for_date_references(fpath)
            all_date_refs.extend(refs)

    overdue = []
    outstanding = []
    paid = []
    unknown = []

    for inv in all_invoices:
        classification, due_date = classify_invoice(inv)
        inv["_classification"] = classification
        inv["_due_date"] = due_date
        if classification == "overdue":
            overdue.append(inv)
        elif classification == "outstanding":
            outstanding.append(inv)
        elif classification == "paid":
            paid.append(inv)
        else:
            unknown.append(inv)

    overdue.sort(key=lambda x: x.get("_due_date") or TODAY)
    outstanding.sort(key=lambda x: x.get("_due_date") or TODAY)

    def format_row(inv):
        parts = []
        for key, val in inv.items():
            if key.startswith("_"):
                continue
            parts.append(f"{key}: {val}")
        source = inv.get("_source", "")
        due = inv.get("_due_date")
        days = ""
        if due:
            delta = (TODAY - due).days
            if delta > 0:
                days = f" ({delta} days overdue)"
            elif delta == 0:
                days = " (due today)"
            else:
                days = f" (due in {-delta} days)"
        return f"  [{source}] {' | '.join(parts)}{days}"

    if overdue:
        print(f"--- OVERDUE ({len(overdue)}) ---")
        for inv in overdue:
            print(format_row(inv))
        print()

    if outstanding:
        print(f"--- OUTSTANDING ({len(outstanding)}) ---")
        for inv in outstanding:
            print(format_row(inv))
        print()

    if paid:
        print(f"--- PAID ({len(paid)}) ---")
        for inv in paid:
            print(format_row(inv))
        print()

    if unknown:
        print(f"--- UNCLASSIFIED ({len(unknown)}) ---")
        for inv in unknown:
            print(format_row(inv))
        print()

    if not all_invoices and not all_date_refs:
        print("[i] No invoice tables or date references found in finance files.")
        print("    Add a payment tracker table to data/finance/payment-tracker.md")
        print("    Format: | Client | Invoice # | Amount | Due Date | Status |")
    elif not all_invoices and all_date_refs:
        print(f"[i] No structured invoice tables found, but {len(all_date_refs)} date reference(s) detected:\n")
        for ref in sorted(all_date_refs, key=lambda x: x["date"]):
            status = "PAST" if ref["date"] < TODAY else "FUTURE"
            print(f"  [{status}] {ref['date']} - {ref['context']} ({ref['file']}:{ref['line_num']})")

    total_overdue = len(overdue)
    total_outstanding = len(outstanding)
    print(f"\n--- SUMMARY ---")
    print(f"Overdue:      {total_overdue}")
    print(f"Outstanding:  {total_outstanding}")
    print(f"Paid:         {len(paid)}")
    print(f"Unclassified: {len(unknown)}")
    print(f"Total:        {len(all_invoices)}")

    if total_overdue > 0:
        print(f"\n[!] ACTION NEEDED: {total_overdue} overdue invoice(s) require follow-up.")

    print()
if __name__ == "__main__":
    main()
