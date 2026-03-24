#!/usr/bin/env python3
"""Read data/finance/ for revenue-related files.

Parses any revenue data found and summarizes by income stream if possible.
Handles the case where no data exists yet.
"""

import re
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]
FINANCE_DIR = REPO_ROOT / "data" / "finance"

# Keywords that identify revenue-related files
REVENUE_KEYWORDS = ["revenue", "income", "earnings", "sales", "invoice", "payment", "billing"]


def find_revenue_files(finance_dir: Path) -> list:
    """Find all files in the finance directory."""
    files = []
    if not finance_dir.exists():
        return files

    for item in finance_dir.rglob("*"):
        if not item.is_file():
            continue
        if item.name in (".gitkeep", ".DS_Store"):
            continue
        files.append(item)

    return sorted(files)


def extract_currency_amounts(text: str) -> list:
    """Extract currency amounts from text, return list of (context, amount)."""
    amounts = []

    # Match patterns like $1,234.56 or $1234 or $1,234
    pattern = r'(?:^|[\s|])([^|\n]{0,50}?)\$\s*([\d,]+(?:\.\d{2})?)'
    for match in re.finditer(pattern, text):
        context = match.group(1).strip().strip("|").strip()
        amount_str = match.group(2).replace(",", "")
        try:
            amount = float(amount_str)
            amounts.append((context, amount))
        except ValueError:
            continue

    return amounts


def parse_markdown_table(content: str) -> list:
    """Parse markdown tables from content."""
    lines = content.split("\n")
    tables = []
    current_header = []
    in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table = False
            continue

        cells = [c.strip() for c in stripped.split("|")]
        cells = [c for i, c in enumerate(cells) if c or (i != 0 and i != len(cells) - 1)]
        cells = [c for c in cells if c]

        if not cells:
            continue

        # Skip separator rows
        if all(re.match(r'^[-:]+$', c) for c in cells):
            continue

        if not in_table:
            current_header = [c.lower() for c in cells]
            in_table = True
            continue

        row = {}
        for i, col in enumerate(current_header):
            row[col] = cells[i] if i < len(cells) else ""
        tables.append(row)

    return tables


def analyze_revenue_file(filepath: Path) -> dict:
    """Analyze a single revenue file and extract what we can."""
    info = {
        "name": filepath.name,
        "path": str(filepath.relative_to(REPO_ROOT)),
        "modified": datetime.fromtimestamp(filepath.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
        "amounts": [],
        "streams": {},
        "tables": [],
    }

    try:
        content = filepath.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return info

    # Extract amounts
    info["amounts"] = extract_currency_amounts(content)

    # Try to parse tables
    table_rows = parse_markdown_table(content)
    info["tables"] = table_rows

    # Try to identify income streams from table data
    for row in table_rows:
        stream_name = ""
        amount = 0.0

        # Look for stream/source column
        for key in row:
            if any(k in key for k in ["stream", "source", "type", "category", "name", "description"]):
                stream_name = row[key]
                break

        # Look for amount column
        for key in row:
            if any(k in key for k in ["amount", "revenue", "total", "income", "value"]):
                val = row[key].replace("$", "").replace(",", "").strip()
                try:
                    amount = float(val)
                except ValueError:
                    continue
                break

        if stream_name and amount > 0:
            info["streams"][stream_name] = info["streams"].get(stream_name, 0) + amount

    return info


def main():
    print("=" * 70)
    print("REVENUE SUMMARY")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    if not FINANCE_DIR.exists():
        print(f"\nFinance directory does not exist: {FINANCE_DIR}")
        print("No revenue data available yet.")
        print("\nTo get started:")
        print("  1. Create the directory: data/finance/")
        print("  2. Add revenue data files (e.g., revenue-history.md, revenue-dashboard.md)")
        print("  3. Run this script again to see a summary")
        return

    all_files = find_revenue_files(FINANCE_DIR)

    if not all_files:
        print("\nNo data files found in data/finance/ (only .gitkeep or empty).")
        print("\nTo get started:")
        print("  1. Add revenue data files to data/finance/")
        print("  2. Use markdown tables with columns like: Stream | Amount | Date")
        print("  3. Run this script again to parse and summarize")
        return

    # Part 1: File inventory
    print(f"\n--- Finance Files ({len(all_files)}) ---")
    print(f"  {'File':<40} {'Modified':<18}")
    print(f"  {'-'*40} {'-'*18}")
    for f in all_files:
        mod = datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
        print(f"  {f.name:<40} {mod:<18}")

    # Part 2: Revenue analysis
    revenue_files = [f for f in all_files if any(kw in f.name.lower() for kw in REVENUE_KEYWORDS)]

    if not revenue_files:
        print("\n--- Revenue Analysis ---")
        print("  No files with revenue-specific names found.")
        print(f"  Looked for files containing: {', '.join(REVENUE_KEYWORDS)}")
        print("  All finance files listed above are available for manual review.")
    else:
        print("\n--- Revenue Analysis ---")
        all_streams: dict[str, float] = {}
        all_amounts = []

        for rf in revenue_files:
            analysis = analyze_revenue_file(rf)

            print(f"\n  File: {analysis['name']}")
            print(f"  Last updated: {analysis['modified']}")

            if analysis["streams"]:
                print("  Income streams found:")
                for stream, amount in sorted(analysis["streams"].items(), key=lambda x: -x[1]):
                    print(f"    - {stream}: ${amount:,.2f}")
                    all_streams[stream] = all_streams.get(stream, 0) + amount
            elif analysis["amounts"]:
                print(f"  Dollar amounts found: {len(analysis['amounts'])}")
                for context, amount in analysis["amounts"][:10]:
                    ctx = context[:40] if context else "(no context)"
                    print(f"    - {ctx}: ${amount:,.2f}")
                all_amounts.extend(analysis["amounts"])
            else:
                print("  No parseable revenue data found in this file.")

        # Grand summary
        if all_streams:
            total = sum(all_streams.values())
            print(f"\n--- Revenue by Income Stream ---")
            print(f"  {'Stream':<30} {'Amount':>15} {'% of Total':>12}")
            print(f"  {'-'*30} {'-'*15} {'-'*12}")
            for stream, amount in sorted(all_streams.items(), key=lambda x: -x[1]):
                pct = amount / total * 100 if total > 0 else 0
                print(f"  {stream:<30} ${amount:>13,.2f} {pct:>10.1f}%")
            print(f"  {'-'*30} {'-'*15}")
            print(f"  {'TOTAL':<30} ${total:>13,.2f}")
        elif all_amounts:
            total = sum(a for _, a in all_amounts)
            print(f"\n  Total dollar amounts found: ${total:,.2f}")
            print("  Note: Could not categorize by stream. Add structured tables for better analysis.")

    print(f"\n{'=' * 70}")


if __name__ == "__main__":
    main()
