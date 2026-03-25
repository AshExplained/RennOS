#!/usr/bin/env python3
"""Read data/pr/outreach-tracker.md, parse the tracker table, and calculate stats.

Outputs: total pitches, response rate, pending follow-ups,
status breakdown (sent/responded/declined/no-response).
"""

import re
import sys
from datetime import datetime, timedelta
from pathlib import Path
from scripts.lib.paths import REPO_ROOT

TRACKER_PATH = REPO_ROOT / "data" / "pr" / "outreach-tracker.md"
FOLLOWUP_THRESHOLD_DAYS = 7
def parse_table_rows(content: str) -> list[dict]:
    """Parse markdown table rows into list of dicts.

    Looks for tables with columns that include status-like headers.
    Handles various table formats flexibly.
    """
    lines = content.split("\n")
    rows = []
    header_cols = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table and header_cols:
                # Table ended, but there might be another table
                in_table = False
            continue

        cells = [c.strip() for c in stripped.split("|")]
        # Remove empty first/last cells from leading/trailing pipes
        cells = [c for c in cells if c or cells.index(c) not in (0, len(cells) - 1)]
        if not cells:
            continue

        # Skip separator rows (e.g., |---|---|---|)
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue

        if not in_table:
            # This is a header row
            header_cols = [c.lower().strip() for c in cells]
            in_table = True
            continue

        # Data row
        row = {}
        for i, col in enumerate(header_cols):
            row[col] = cells[i] if i < len(cells) else ""
        rows.append(row)

    return rows
def find_status_column(rows: list[dict]) -> str:
    """Find which column contains status information."""
    status_keywords = ["status", "state", "result", "response"]
    if not rows:
        return ""
    for key in rows[0]:
        for keyword in status_keywords:
            if keyword in key:
                return key
    return ""
def find_date_column(rows: list[dict]) -> str:
    """Find which column contains date information."""
    date_keywords = ["date", "pitched", "sent", "when"]
    if not rows:
        return ""
    for key in rows[0]:
        for keyword in date_keywords:
            if keyword in key:
                return key
    return ""
def parse_date(date_str: str):
    """Try to parse a date string in common formats."""
    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%B %d, %Y", "%b %d, %Y",
               "%Y-%m-%d %H:%M", "%m/%d/%y"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    return None
def main():
    print("=" * 70)
    print("OUTREACH TRACKER STATISTICS")
    print("=" * 70)

    if not TRACKER_PATH.exists():
        print(f"\nOutreach tracker not found at: {TRACKER_PATH}")
        print("No outreach data to analyze yet.")
        print("Tip: Create the tracker by running the outreach-tracker skill to log your first pitch.")
        return

    content = TRACKER_PATH.read_text(encoding="utf-8")
    if not content.strip():
        print("\nOutreach tracker file is empty.")
        print("Tip: Use the outreach-tracker skill to log your first pitch.")
        return

    rows = parse_table_rows(content)
    if not rows:
        print("\nNo table data found in outreach tracker.")
        print("Expected a markdown table with columns like: Journalist | Outlet | Date | Status")
        return

    status_col = find_status_column(rows)
    date_col = find_date_column(rows)

    # Normalize statuses
    status_counts: dict[str, int] = {}
    pending_followups = []
    now = datetime.now()

    for row in rows:
        raw_status = row.get(status_col, "unknown").strip().lower() if status_col else "unknown"

        # Normalize common status variations
        if raw_status in ("sent", "pitched", "emailed"):
            status = "sent"
        elif raw_status in ("responded", "reply", "replied", "response"):
            status = "responded"
        elif raw_status in ("declined", "rejected", "pass", "passed"):
            status = "declined"
        elif raw_status in ("no response", "no-response", "noreply", "no reply", "pending"):
            status = "no-response"
        elif raw_status in ("accepted", "yes", "confirmed", "published", "featured"):
            status = "accepted"
        elif raw_status in ("follow-up", "followed up", "followup"):
            status = "follow-up sent"
        else:
            status = raw_status if raw_status else "unknown"

        status_counts[status] = status_counts.get(status, 0) + 1

        # Check for pending follow-ups (sent but no response, older than threshold)
        if status in ("sent", "no-response") and date_col:
            date_str = row.get(date_col, "")
            pitch_date = parse_date(date_str)
            if pitch_date and (now - pitch_date).days >= FOLLOWUP_THRESHOLD_DAYS:
                journalist = ""
                for key in row:
                    if any(k in key for k in ["journalist", "contact", "name", "who"]):
                        journalist = row[key]
                        break
                if not journalist:
                    # Use first column as fallback
                    first_key = list(row.keys())[0]
                    journalist = row[first_key]
                pending_followups.append({
                    "contact": journalist,
                    "date": date_str,
                    "days_ago": (now - pitch_date).days,
                })

    total = len(rows)
    responded = status_counts.get("responded", 0) + status_counts.get("accepted", 0)
    response_rate = (responded / total * 100) if total > 0 else 0

    # Print summary
    print(f"\n  Total pitches:       {total}")
    print(f"  Response rate:       {response_rate:.1f}% ({responded}/{total})")
    print(f"  Pending follow-ups:  {len(pending_followups)}")

    print(f"\n  --- Status Breakdown ---")
    for status, count in sorted(status_counts.items(), key=lambda x: -x[1]):
        pct = count / total * 100 if total > 0 else 0
        bar = "#" * int(pct / 2)
        print(f"  {status:<18} {count:>3} ({pct:5.1f}%) {bar}")

    if pending_followups:
        print(f"\n  --- Pending Follow-ups (>{FOLLOWUP_THRESHOLD_DAYS} days, no response) ---")
        print(f"  {'Contact':<30} {'Pitched':<14} {'Days Ago'}")
        print(f"  {'-'*30} {'-'*14} {'-'*8}")
        for item in sorted(pending_followups, key=lambda x: -x["days_ago"]):
            print(f"  {item['contact']:<30} {item['date']:<14} {item['days_ago']} days")

    print(f"\n{'=' * 70}")
if __name__ == "__main__":
    main()
