#!/usr/bin/env bash
#
# RennOS Update Script
# Pulls latest system files from GitHub without touching your personal data.
#
# Usage: ./update.sh
#

set -euo pipefail

REPO_URL="https://github.com/AshExplained/RennOS.git"
REMOTE_NAME="rennos-upstream"
TEMP_BRANCH="rennos-update-temp"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

info()  { echo -e "${CYAN}[INFO]${NC} $1"; }
ok()    { echo -e "${GREEN}[OK]${NC} $1"; }
warn()  { echo -e "${YELLOW}[WARN]${NC} $1"; }
error() { echo -e "${RED}[ERROR]${NC} $1"; }

# ---------------------------------------------------------------------------
# Files/dirs that are ALWAYS safe to overwrite (system files)
# ---------------------------------------------------------------------------
SYSTEM_FILES=(
  "CLAUDE.md"
  ".gitignore"
  ".env.example"
  "LICENSE"
  "README.md"
  ".claude/settings.json"
)

SYSTEM_DIRS=(
  ".claude/agents"
  ".claude/skills"
  "scripts"
  "templates"
  "docs"
)

# CEO memory files safe to overwrite (structural, not personal)
CEO_SYSTEM_FILES=(
  ".claude/ceo-memory/org-chart.md"
  ".claude/ceo-memory/tools.md"
  ".claude/ceo-memory/workflows.md"
)

# ---------------------------------------------------------------------------
# Files that are NEVER overwritten (personal data)
# ---------------------------------------------------------------------------
PROTECTED_PATTERNS=(
  ".claude/ceo-memory/user_profile.md"
  ".claude/ceo-memory/active_projects.md"
  ".claude/ceo-memory/decisions.md"
  ".claude/ceo-memory/feedback.md"
  ".claude/ceo-memory/MEMORY.md"
  ".claude/settings.local.json"
  "data/brand/brand-dna.md"
  "data/strategy/audience-personas.md"
  "data/strategy/competitive-landscape.md"
  "data/strategy/quarterly-roadmap.md"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

is_protected() {
  local file="$1"
  for pattern in "${PROTECTED_PATTERNS[@]}"; do
    if [[ "$file" == "$pattern" ]]; then
      return 0
    fi
  done
  return 1
}

is_agent_memory() {
  [[ "$1" == .claude/agent-memory/*/MEMORY.md ]]
}

is_data_file() {
  [[ "$1" == data/* ]] && [[ "$1" != data/*/.gitkeep ]]
}

is_vault_file() {
  [[ "$1" == vault/* ]] && [[ "$1" != vault/*/.gitkeep ]]
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

echo ""
echo "=========================================="
echo "  RennOS Updater"
echo "=========================================="
echo ""

# Check we're in a git repo
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  error "Not inside a git repository. Run this from your RennOS root."
  exit 1
fi

# Check for uncommitted changes
if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
  warn "You have uncommitted changes. Commit or stash them first."
  echo ""
  git status --short
  echo ""
  read -p "Continue anyway? (y/N) " -n 1 -r
  echo
  if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    info "Aborted. Commit your changes and try again."
    exit 0
  fi
fi

# Add upstream remote if not present
if ! git remote get-url "$REMOTE_NAME" &>/dev/null; then
  info "Adding upstream remote: $REPO_URL"
  git remote add "$REMOTE_NAME" "$REPO_URL"
fi

# Fetch latest
info "Fetching latest from RennOS upstream..."
git fetch "$REMOTE_NAME" main --quiet 2>/dev/null || {
  error "Failed to fetch from $REPO_URL"
  error "Check your internet connection and try again."
  exit 1
}

ok "Fetched latest version"

# Get list of files in upstream
UPSTREAM_FILES=$(git ls-tree -r --name-only "$REMOTE_NAME/main")

# Track changes
UPDATED=()
CREATED=()
SKIPPED=()
NEW_AGENT_MEMORIES=()

echo ""
info "Comparing with upstream..."
echo ""

# Process each upstream file
while IFS= read -r file; do
  # Skip empty lines
  [[ -z "$file" ]] && continue

  # --- PROTECTED: Never overwrite ---
  if is_protected "$file"; then
    SKIPPED+=("$file (protected — personal data)")
    continue
  fi

  # --- AGENT MEMORY: Only create new, never overwrite ---
  if is_agent_memory "$file"; then
    if [[ ! -f "$file" ]]; then
      # New agent — create placeholder memory
      mkdir -p "$(dirname "$file")"
      git show "$REMOTE_NAME/main:$file" > "$file"
      NEW_AGENT_MEMORIES+=("$file")
    fi
    # Existing agent memory — skip silently
    continue
  fi

  # --- DATA FILES: Only create new dirs/gitkeeps, never overwrite content ---
  if is_data_file "$file"; then
    if [[ ! -f "$file" ]]; then
      # New data file from upstream — check if it's a placeholder
      local_dir="$(dirname "$file")"
      mkdir -p "$local_dir"
      # Only copy if file doesn't exist locally
      git show "$REMOTE_NAME/main:$file" > "$file"
      CREATED+=("$file (new data placeholder)")
    else
      SKIPPED+=("$file (existing data — preserved)")
    fi
    continue
  fi

  # --- VAULT: Only create structure, never overwrite ---
  if is_vault_file "$file"; then
    SKIPPED+=("$file (vault — preserved)")
    continue
  fi

  # --- SYSTEM FILES & DIRS: Always overwrite ---
  mkdir -p "$(dirname "$file")"

  if [[ -f "$file" ]]; then
    # Check if file actually changed
    local_hash=$(git hash-object "$file" 2>/dev/null || echo "none")
    upstream_hash=$(git rev-parse "$REMOTE_NAME/main:$file" 2>/dev/null || echo "none")

    if [[ "$local_hash" != "$upstream_hash" ]]; then
      git show "$REMOTE_NAME/main:$file" > "$file"
      UPDATED+=("$file")
    fi
  else
    # New file
    git show "$REMOTE_NAME/main:$file" > "$file"
    CREATED+=("$file")
  fi

done <<< "$UPSTREAM_FILES"

# Also handle .gitkeep files in vault/ and data/ for new directories
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if [[ "$file" == */.gitkeep ]] && [[ ! -f "$file" ]]; then
    mkdir -p "$(dirname "$file")"
    touch "$file"
    CREATED+=("$file (new directory)")
  fi
done <<< "$UPSTREAM_FILES"

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

echo ""
echo "=========================================="
echo "  Update Summary"
echo "=========================================="
echo ""

if [[ ${#UPDATED[@]} -gt 0 ]]; then
  ok "Updated (${#UPDATED[@]} files):"
  for f in "${UPDATED[@]}"; do
    echo "    $f"
  done
  echo ""
fi

if [[ ${#CREATED[@]} -gt 0 ]]; then
  ok "Created (${#CREATED[@]} files):"
  for f in "${CREATED[@]}"; do
    echo "    $f"
  done
  echo ""
fi

if [[ ${#NEW_AGENT_MEMORIES[@]} -gt 0 ]]; then
  ok "New agents (${#NEW_AGENT_MEMORIES[@]}):"
  for f in "${NEW_AGENT_MEMORIES[@]}"; do
    agent=$(basename "$(dirname "$f")")
    echo "    $agent"
  done
  echo ""
fi

if [[ ${#UPDATED[@]} -eq 0 ]] && [[ ${#CREATED[@]} -eq 0 ]] && [[ ${#NEW_AGENT_MEMORIES[@]} -eq 0 ]]; then
  ok "Already up to date! No changes needed."
fi

echo ""
info "Your personal data was not touched:"
info "  - user_profile.md, active_projects.md, decisions.md, feedback.md"
info "  - Agent memories (existing), data/ content, vault/ content"
echo ""
echo "=========================================="
echo "  Done!"
echo "=========================================="
echo ""
