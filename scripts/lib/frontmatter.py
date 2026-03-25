"""YAML frontmatter parsing and writing for markdown files.

Used by process-inbox, content agents, and vault operations.
Handles the --- delimited YAML block at the top of markdown files.
"""

import re
from pathlib import Path

# Regex to match YAML frontmatter block
_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown text.

    Returns (metadata_dict, body_text). If no frontmatter found,
    returns ({}, original_text).

    Uses simple key: value parsing — no PyYAML dependency.
    Handles: strings, lists (bracket and dash syntax), booleans, numbers.
    """
    match = _FRONTMATTER_RE.match(text)
    if not match:
        return {}, text

    raw = match.group(1)
    body = text[match.end():]
    metadata = _parse_yaml_simple(raw)
    return metadata, body


def _parse_yaml_simple(raw: str) -> dict:
    """Simple YAML parser for frontmatter — no external deps.

    Supports:
      key: value
      key: [item1, item2]
      key:
        - item1
        - item2
      key: true/false
      key: 123
    """
    result = {}
    lines = raw.split("\n")
    current_key = None
    current_list = None

    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Check for list continuation (  - item)
        if stripped.startswith("- ") and current_key is not None:
            if current_list is None:
                current_list = []
            current_list.append(_cast_value(stripped[2:].strip()))
            result[current_key] = current_list
            continue

        # New key: value pair
        if ":" in stripped:
            # Save any pending list
            current_list = None

            colon_idx = stripped.index(":")
            key = stripped[:colon_idx].strip()
            value = stripped[colon_idx + 1:].strip()

            current_key = key

            if not value:
                # Value might be a list on following lines
                result[key] = None
                current_list = []
                continue

            # Bracket list: [item1, item2]
            if value.startswith("[") and value.endswith("]"):
                items = [_cast_value(v.strip().strip('"').strip("'"))
                         for v in value[1:-1].split(",") if v.strip()]
                result[key] = items
                current_list = None
            else:
                result[key] = _cast_value(value)
                current_list = None

    # Clean up None values that never got list items
    for k, v in result.items():
        if v is None:
            result[k] = ""

    return result


def _cast_value(value: str):
    """Cast a string value to the appropriate Python type."""
    if not isinstance(value, str):
        return value

    # Strip quotes
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]

    # Booleans
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False

    # Numbers
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass

    return value


def write_frontmatter(metadata: dict, body: str) -> str:
    """Combine metadata dict and body text into a markdown string with frontmatter."""
    if not metadata:
        return body

    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, list):
            lines.append(f"{key}: [{', '.join(str(v) for v in value)}]")
        elif isinstance(value, bool):
            lines.append(f"{key}: {'true' if value else 'false'}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    lines.append("")

    return "\n".join(lines) + body


def update_frontmatter_field(text: str, key: str, value) -> str:
    """Update a single frontmatter field in a markdown string.

    If frontmatter exists, updates or adds the key.
    If no frontmatter exists, creates it with just this key.
    """
    metadata, body = parse_frontmatter(text)
    metadata[key] = value
    return write_frontmatter(metadata, body)


def read_file_frontmatter(filepath: Path) -> tuple[dict, str]:
    """Read a file and return its (frontmatter, body)."""
    text = filepath.read_text(encoding="utf-8")
    return parse_frontmatter(text)
