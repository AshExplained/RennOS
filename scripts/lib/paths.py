"""Central path constants for RennOS.

Single source of truth — all scripts import from here instead of
computing REPO_ROOT with fragile .parents[N] chains.
"""

from pathlib import Path

# Repository root — works regardless of where the calling script lives
REPO_ROOT = Path(__file__).resolve().parents[2]

# Core directories
DATA_DIR = REPO_ROOT / "data"
VAULT_DIR = REPO_ROOT / "vault"
SCRIPTS_DIR = REPO_ROOT / "scripts"

# CEO + Agent memory
CEO_MEMORY_DIR = REPO_ROOT / ".claude" / "ceo-memory"
AGENT_MEMORY_DIR = REPO_ROOT / ".claude" / "agent-memory"
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"

# Common data subdirectories
BRAND_DIR = DATA_DIR / "brand"
STRATEGY_DIR = DATA_DIR / "strategy"
CONTENT_DIR = DATA_DIR / "content"
FINANCE_DIR = DATA_DIR / "finance"
INBOX_DIR = DATA_DIR / "inbox"
ARCHIVE_DIR = DATA_DIR / "archive"

# Vault subdirectories
VAULT_INBOX_DIR = VAULT_DIR / "inbox"
VAULT_PERSONAL_DIR = VAULT_DIR / "personal"
VAULT_PROFESSIONAL_DIR = VAULT_DIR / "professional"
