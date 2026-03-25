"""Shared data scanning utilities for RennOS.

Consolidates duplicated scan functions from:
- analytics/kpi-dashboard/scripts/aggregate_metrics.py
- ops/status-report/scripts/project_status_scan.py
- analytics/weekly-digest/scripts/compile_weekly_data.py
- social/content-calendar/scripts/list_available_content.py
"""

from __future__ import annotations

from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional

from scripts.lib.paths import REPO_ROOT, DATA_DIR

# Files to always skip when scanning
IGNORED_FILES = {".gitkeep", ".DS_Store"}

# Freshness thresholds (days)
FRESHNESS_THRESHOLDS = {
    "fresh": 3,
    "recent": 7,
    "stale": 30,
}


def freshness_label(days_old: int) -> str:
    """Return a freshness label based on age in days."""
    if days_old <= FRESHNESS_THRESHOLDS["fresh"]:
        return "FRESH"
    elif days_old <= FRESHNESS_THRESHOLDS["recent"]:
        return "RECENT"
    elif days_old <= FRESHNESS_THRESHOLDS["stale"]:
        return "STALE"
    return "OUTDATED"


def file_info(filepath: Path, base: Path | None = None) -> dict:
    """Build a standard file info dict for a single file.

    Args:
        filepath: Absolute path to the file.
        base: Base path for computing relative paths (defaults to REPO_ROOT).
    """
    base = base or REPO_ROOT
    stat = filepath.stat()
    mod_time = datetime.fromtimestamp(stat.st_mtime)
    days_old = (datetime.now() - mod_time).days

    return {
        "name": filepath.name,
        "path": str(filepath.relative_to(base)),
        "modified": mod_time.strftime("%Y-%m-%d %H:%M"),
        "days_old": days_old,
        "freshness": freshness_label(days_old),
        "size": stat.st_size,
    }


def scan_directory(directory: Path, base: Path | None = None) -> list[dict]:
    """Recursively scan a directory for files, returning file info dicts.

    Skips .gitkeep, .DS_Store, and non-files.
    Results sorted by name.
    """
    if not directory.is_dir():
        return []

    results = []
    for item in sorted(directory.rglob("*")):
        if not item.is_file() or item.name in IGNORED_FILES:
            continue
        results.append(file_info(item, base))
    return results


def scan_recent_files(base_dir: Path, days: int = 7) -> dict[str, list[dict]]:
    """Scan for files modified within the last N days, grouped by top-level subdirectory.

    Args:
        base_dir: Directory to scan (typically DATA_DIR).
        days: Look-back window in days.

    Returns:
        Dict mapping subdirectory name -> list of file info dicts, sorted by recency.
    """
    cutoff = datetime.now() - timedelta(days=days)
    departments: dict[str, list[dict]] = {}

    if not base_dir.exists():
        return departments

    for item in base_dir.rglob("*"):
        if not item.is_file() or item.name in IGNORED_FILES:
            continue

        stat = item.stat()
        mod_time = datetime.fromtimestamp(stat.st_mtime)
        if mod_time < cutoff:
            continue

        rel = item.relative_to(base_dir)
        dept = rel.parts[0] if rel.parts else "(root)"

        info = file_info(item)
        departments.setdefault(dept, []).append(info)

    for dept in departments:
        departments[dept].sort(key=lambda x: x["days_old"])

    return departments


def get_most_recent_file(directory: Path) -> dict | None:
    """Find the single most recently modified file in a directory.

    Returns file_info dict with an added 'preview' key (first 3 content lines),
    or None if no files found.
    """
    if not directory.exists():
        return None

    most_recent = None
    most_recent_time = 0

    for item in directory.rglob("*"):
        if not item.is_file() or item.name in IGNORED_FILES:
            continue
        mtime = item.stat().st_mtime
        if mtime > most_recent_time:
            most_recent_time = mtime
            most_recent = item

    if most_recent is None:
        return None

    info = file_info(most_recent)

    # Read first 3 non-empty, non-frontmatter lines as preview
    preview_lines = []
    try:
        with open(most_recent, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                stripped = line.strip()
                if stripped and stripped != "---":
                    preview_lines.append(stripped)
                if len(preview_lines) >= 3:
                    break
    except (OSError, UnicodeDecodeError):
        preview_lines = ["(binary or unreadable file)"]

    info["preview"] = preview_lines
    return info


def list_departments(base_dir: Path | None = None) -> list[str]:
    """List all department subdirectory names under base_dir (defaults to DATA_DIR)."""
    base_dir = base_dir or DATA_DIR
    if not base_dir.exists():
        return []
    return sorted(
        d.name for d in base_dir.iterdir()
        if d.is_dir() and d.name not in IGNORED_FILES
    )


def human_size(size_bytes: int) -> str:
    """Convert bytes to human-readable size string."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"
