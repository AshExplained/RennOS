#!/usr/bin/env python3
"""Scan data/content/drafts/ and data/social/ for files ready to schedule.

Lists each file with its name, modification date, and size.
Excludes .gitkeep files.
"""

import os
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[5]  # Up from scripts/ -> content-calendar -> social -> skills -> .claude -> RennOS
SCAN_DIRS = [
    REPO_ROOT / "data" / "content" / "drafts",
    REPO_ROOT / "data" / "social",
]


def human_size(size_bytes: int) -> str:
    """Convert bytes to human-readable size."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def scan_directory(directory: Path) -> list[dict]:
    """Recursively scan a directory for schedulable content files."""
    results = []
    if not directory.exists():
        return results
    for item in sorted(directory.rglob("*")):
        if not item.is_file():
            continue
        if item.name == ".gitkeep":
            continue
        stat = item.stat()
        results.append({
            "name": item.name,
            "path": str(item.relative_to(REPO_ROOT)),
            "modified": datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M"),
            "size": human_size(stat.st_size),
        })
    return results


def main():
    print("=" * 70)
    print("AVAILABLE CONTENT FOR SCHEDULING")
    print("=" * 70)

    total_files = 0
    for scan_dir in SCAN_DIRS:
        rel_path = str(scan_dir.relative_to(REPO_ROOT))
        print(f"\n--- {rel_path}/ ---")

        if not scan_dir.exists():
            print(f"  Directory does not exist yet. Create it at: {scan_dir}")
            continue

        files = scan_directory(scan_dir)
        if not files:
            print("  No content files found (empty or only .gitkeep).")
            continue

        # Print table header
        print(f"  {'File':<40} {'Modified':<18} {'Size':<10}")
        print(f"  {'-'*40} {'-'*18} {'-'*10}")
        for f in files:
            print(f"  {f['name']:<40} {f['modified']:<18} {f['size']:<10}")
        total_files += len(files)

    print(f"\n{'=' * 70}")
    print(f"Total files available for scheduling: {total_files}")
    if total_files == 0:
        print("Tip: Add content drafts to data/content/drafts/ or adapted posts to data/social/")
    print("=" * 70)


if __name__ == "__main__":
    main()
