"""Shared report formatting utilities for RennOS.

Used by revenue dashboard, weekly digest, status report, KPI dashboard,
and any agent that produces structured terminal output.
"""

from datetime import datetime


def section_header(title: str, width: int = 70) -> str:
    """Return a formatted section header."""
    return f"\n{'=' * width}\n{title}\n{'=' * width}"


def sub_header(title: str) -> str:
    """Return a formatted sub-section header."""
    return f"\n--- {title} ---"


def table_row(columns: list[tuple[str, int]], values: list[str], indent: int = 2) -> str:
    """Format a single table row with fixed-width columns.

    Args:
        columns: List of (header_name, width) tuples.
        values: List of values matching the columns.
        indent: Number of leading spaces.
    """
    prefix = " " * indent
    parts = []
    for i, (_, width) in enumerate(columns):
        val = values[i] if i < len(values) else ""
        parts.append(f"{val:<{width}}")
    return prefix + " ".join(parts)


def table_header(columns: list[tuple[str, int]], indent: int = 2) -> str:
    """Format a table header row with separator line."""
    prefix = " " * indent
    header_parts = []
    sep_parts = []
    for name, width in columns:
        header_parts.append(f"{name:<{width}}")
        sep_parts.append("-" * width)
    header = prefix + " ".join(header_parts)
    separator = prefix + " ".join(sep_parts)
    return f"{header}\n{separator}"


def summary_block(title: str, items: dict[str, str], width: int = 70) -> str:
    """Format a summary block with key-value pairs.

    Args:
        title: Block title.
        items: Dict of label -> value pairs.
        width: Total width for the border.
    """
    lines = [f"\n{'=' * width}", title, f"{'=' * width}"]
    for label, value in items.items():
        lines.append(f"  {label}: {value}")
    lines.append(f"{'=' * width}")
    return "\n".join(lines)


def timestamp_line(label: str = "Generated") -> str:
    """Return a formatted timestamp line."""
    return f"{label}: {datetime.now().strftime('%Y-%m-%d %H:%M')}"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Generate a markdown-formatted table string.

    Useful when agents write output to markdown files in data/.
    """
    if not headers:
        return ""

    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))

    # Build table
    lines = []
    header_line = "| " + " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)) + " |"
    sep_line = "| " + " | ".join("-" * widths[i] for i in range(len(headers))) + " |"
    lines.append(header_line)
    lines.append(sep_line)

    for row in rows:
        cells = []
        for i in range(len(headers)):
            val = str(row[i]) if i < len(row) else ""
            cells.append(val.ljust(widths[i]))
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)
