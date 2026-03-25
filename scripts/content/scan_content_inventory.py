#!/usr/bin/env python3
"""Scan data/content/ for all content pieces.

Lists each with filename, format (inferred from name/extension),
and checks if derivatives exist in data/social/ or other data/content/ subdirs.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from scripts.lib.paths import REPO_ROOT, CONTENT_DIR

SOCIAL_DIR = REPO_ROOT / "data" / "social"

# Map extensions to format labels
FORMAT_MAP = {
    ".md": "Markdown/Article",
    ".txt": "Plain Text",
    ".html": "HTML",
    ".pdf": "PDF Document",
    ".doc": "Word Document",
    ".docx": "Word Document",
    ".json": "JSON Data",
    ".yaml": "YAML Config",
    ".yml": "YAML Config",
    ".csv": "CSV Data",
    ".png": "Image (PNG)",
    ".jpg": "Image (JPEG)",
    ".jpeg": "Image (JPEG)",
    ".gif": "Image (GIF)",
    ".svg": "Image (SVG)",
    ".mp4": "Video",
    ".mov": "Video",
    ".mp3": "Audio",
    ".wav": "Audio",
}

# Keywords in filenames that hint at format/type
TYPE_HINTS = {
    "thread": "Twitter/X Thread",
    "carousel": "Carousel Post",
    "newsletter": "Newsletter",
    "blog": "Blog Post",
    "linkedin": "LinkedIn Post",
    "tweet": "Tweet",
    "reel": "Reel/Short Video",
    "story": "Story",
    "email": "Email",
    "script": "Script",
    "outline": "Outline",
    "draft": "Draft",
}
def infer_format(filepath: Path) -> str:
    """Infer content format from file extension and name."""
    name_lower = filepath.stem.lower().replace("-", " ").replace("_", " ")

    # Check filename hints first (more specific)
    for keyword, label in TYPE_HINTS.items():
        if keyword in name_lower:
            return label

    # Fall back to extension
    ext = filepath.suffix.lower()
    return FORMAT_MAP.get(ext, f"Unknown ({ext})" if ext else "Unknown")
def find_derivatives(source_stem: str, all_files: list[Path]) -> list[str]:
    """Check if derivatives of a source content piece exist elsewhere."""
    derivatives = []
    stem_lower = source_stem.lower().replace("-", "").replace("_", "")

    for f in all_files:
        f_stem = f.stem.lower().replace("-", "").replace("_", "")
        # Check if the other file's name contains the source stem (loose match)
        if stem_lower in f_stem and f.stem != source_stem:
            derivatives.append(str(f.relative_to(REPO_ROOT)))

    return derivatives
def main():
    print("=" * 70)
    print("CONTENT INVENTORY SCAN")
    print("=" * 70)

    if not CONTENT_DIR.exists():
        print(f"\nContent directory does not exist yet: {CONTENT_DIR}")
        print("Create it and add content files to get started.")
        return

    # Collect all files across content and social dirs for derivative checking
    all_content_files = []
    all_social_files = []

    for f in CONTENT_DIR.rglob("*"):
        if f.is_file() and f.name != ".gitkeep":
            all_content_files.append(f)

    if SOCIAL_DIR.exists():
        for f in SOCIAL_DIR.rglob("*"):
            if f.is_file() and f.name != ".gitkeep":
                all_social_files.append(f)

    all_files = all_content_files + all_social_files

    if not all_content_files:
        print("\nNo content files found in data/content/ (only .gitkeep or empty).")
        print("Tip: Add content pieces to data/content/ and subdirectories.")
        return

    # Group by subdirectory
    subdirs: dict[str, list[Path]] = {}
    for f in sorted(all_content_files):
        rel = f.relative_to(CONTENT_DIR)
        subdir = str(rel.parent) if str(rel.parent) != "." else "(root)"
        subdirs.setdefault(subdir, []).append(f)

    total = 0
    total_with_derivatives = 0

    for subdir, files in sorted(subdirs.items()):
        print(f"\n--- data/content/{subdir}/ ---")
        print(f"  {'File':<35} {'Format':<22} {'Derivatives'}")
        print(f"  {'-'*35} {'-'*22} {'-'*30}")

        for f in files:
            fmt = infer_format(f)
            derivatives = find_derivatives(f.stem, all_files)
            deriv_str = ", ".join(derivatives[:3]) if derivatives else "None found"
            if len(derivatives) > 3:
                deriv_str += f" (+{len(derivatives) - 3} more)"

            print(f"  {f.name:<35} {fmt:<22} {deriv_str}")
            total += 1
            if derivatives:
                total_with_derivatives += 1

    print(f"\n{'=' * 70}")
    print(f"Total content pieces: {total}")
    print(f"Pieces with derivatives: {total_with_derivatives}")
    print(f"Social adaptations found: {len(all_social_files)}")
    if total > 0 and total_with_derivatives == 0:
        print("Tip: No derivatives detected. Consider repurposing source content into social posts.")
    print("=" * 70)
if __name__ == "__main__":
    main()
