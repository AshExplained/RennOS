#!/usr/bin/env python3
"""Scan data/content/drafts/ and data/social/ for files ready to schedule.

Lists each file with its name, modification date, and size.
Excludes .gitkeep files.
"""

import sys
from scripts.lib.paths import REPO_ROOT, CONTENT_DIR
from scripts.lib.data_scanner import scan_directory, human_size

SCAN_DIRS = [
    CONTENT_DIR / "drafts",
    REPO_ROOT / "data" / "social",
]
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
            print(f"  {f['name']:<40} {f['modified']:<18} {human_size(f['size']):<10}")
        total_files += len(files)

    print(f"\n{'=' * 70}")
    print(f"Total files available for scheduling: {total_files}")
    if total_files == 0:
        print("Tip: Add content drafts to data/content/drafts/ or adapted posts to data/social/")
    print("=" * 70)
if __name__ == "__main__":
    main()
