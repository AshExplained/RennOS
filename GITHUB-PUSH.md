# RennOS Public GitHub Repo Push Protocol

> This file is gitignored. It exists only on `main` (your working branch) as a reference for Tony and future sessions.

## Branch Architecture

| Branch | Purpose | Contains Personal Data | Pushed to GitHub |
|--------|---------|----------------------|-----------------|
| `main` | Your working branch — full RennOS with personal data | YES | NEVER |
| `template` | Clean public template for other users | NO | YES (as remote `main`) |

## The Rule

**NEVER push `main` to GitHub. It contains personal data.**

When the user says "push to GitHub" or "publish", they mean:
1. Checkout `template` branch
2. Cherry-pick **only system/structural changes** from `main` (scripts, skills, CLAUDE.md, tools.md)
3. **NEVER copy** these files to template:
   - `.claude/agent-memory/*/MEMORY.md` (personal brand context)
   - `.claude/ceo-memory/active_projects.md` (personal project status)
   - `.claude/ceo-memory/user_profile.md` (personal identity)
   - `data/brand/brand-dna.md` (personal brand DNA)
   - `data/strategy/audience-personas.md` (personal audience data)
   - `data/strategy/competitive-landscape.md` (personal competitive data)
   - `data/strategy/quarterly-roadmap.md` (personal roadmap)
   - `vault/` anything (personal second brain)
4. Scrub any hardcoded personal paths (e.g., `/Users/ash/`) — use `<repo-root>/` instead
5. Push template to remote `main`: `git push origin template:main`

## Remote Setup

- **Remote:** `origin` = `https://github.com/AshExplained/RennOS.git`
- **Remote `main`** = local `template` branch content
- **Local `main`** is NOT tracked to any remote (intentional)

## Quick Publish Workflow

```bash
# 1. On main, identify what changed (system-only)
git diff template...main --stat

# 2. Switch to template
git checkout template

# 3. Cherry-pick system files from main
git checkout main -- <system-file-paths>

# 4. Verify no personal data
grep -rn "/Users/ash\|ashexplained\|Asha\b" .claude/ data/ scripts/ CLAUDE.md

# 5. Commit and push
git commit -m "Description of changes"
git push origin template:main
```

## Structural Change Checklist

When main adds new directories, files, or restructures existing ones, template must get the **structure** (not the content). Run this checklist before every publish:

### New directories added on main?
```bash
# Compare directory trees
diff <(cd /tmp && git clone -b template . --quiet 2>/dev/null; find . -type d | sort) <(find . -type d | sort)
# Or simpler: check for new dirs
git diff template...main --stat | grep -E '^\s+\w+/'
```
- If a new `data/<dept>/` folder was added → create it on template with `.gitkeep`
- If a new `vault/<section>/` folder was added → create it on template with `.gitkeep`
- If a new `.claude/agent-memory/<agent>/` folder was added → create it with placeholder MEMORY.md
- If a new `.claude/skills/<dept>/<skill>/` folder was added → copy the full skill (SKILL.md, references/, templates/)
- If a new `scripts/<dept>/` folder was added → copy the folder with `__init__.py` and scripts

### New data files added on main?
- If it's a **placeholder/template file** (empty structure) → copy to template
- If it contains **personal data** (brand DNA, personas, roadmap content) → create an empty placeholder version for template instead

### Files deleted on main?
- Delete them on template too (unless template has a different version of that file)

### Files renamed/moved on main?
- Mirror the rename/move on template

### Key rule: Template should always mirror main's folder structure, but with empty/placeholder content where main has personal data.

## What Counts as "System Changes" (safe for template)

### Core System Files
- `CLAUDE.md` (rules, structure, scripts rule)
- `.gitignore`, `.env.example`, `LICENSE`, `README.md`
- `.claude/settings.json` (project settings)

### Agent & Skill Definitions
- `.claude/agents/*.md` (99 agent definitions)
- `.claude/skills/**/*.md` (230+ skill playbooks, references, templates, examples)
- `.claude/skills/stitch-*/` (Stitch skill packages — scripts stay inside these)

### Scripts
- `scripts/` (shared lib + department scripts)

### CEO Memory (system-only, scrub personal paths)
- `.claude/ceo-memory/tools.md` (tool inventory)
- `.claude/ceo-memory/workflows.md` (operational workflows)
- `.claude/ceo-memory/org-chart.md` (department structure)
- `.claude/ceo-memory/MEMORY.md` (CEO agent memory — template has placeholder)
- `.claude/ceo-memory/decisions.md` (template has placeholder)
- `.claude/ceo-memory/feedback.md` (template has placeholder)
- `.claude/ceo-memory/user_profile.md` (template has "[Set during onboarding]" placeholders)
- `.claude/ceo-memory/active_projects.md` (template has empty placeholder)

### Agent Memory (structure only)
- `.claude/agent-memory/*/MEMORY.md` — template has 4-line placeholder files. NEVER overwrite with personal data from main.

### Data Directory (structure only)
- `data/` — template has placeholder `.md` files with empty structures and `.gitkeep` files. Contains:
  - `data/analytics/`, `data/brand/`, `data/content/`, `data/customers/`
  - `data/design/`, `data/finance/`, `data/legal/`, `data/marketing/`
  - `data/operations/`, `data/partnerships/`, `data/personal/`
  - `data/pr/`, `data/product/`, `data/social/`, `data/strategy/`
  - `data/tech/`, `data/inbox/`, `data/archive/`
- **IMPORTANT:** Template `data/` files have generic/empty content. NEVER overwrite with personal data from main.

### Vault Directory (structure only)
- `vault/` — template has `.gitkeep` files preserving folder structure:
  - `vault/inbox/`, `vault/personal/goals/`, `vault/personal/health/`
  - `vault/personal/journal/`, `vault/personal/relationships/`
  - `vault/professional/ideas/`, `vault/professional/learnings/`
  - `vault/professional/notes/`, `vault/resources/`
- **NEVER copy actual vault content from main.**

### Templates
- `templates/` — clipping.md, daily-note.md, meeting-note.md (Obsidian note templates)

### Docs
- `docs/claude-code-meta.md` (system documentation)

## Files That NEVER Go to Template

| Path | Why |
|------|-----|
| `.claude/agent-memory/*/MEMORY.md` (with real content) | Personal brand context baked in |
| `.claude/ceo-memory/active_projects.md` (from main) | Personal project status |
| `.claude/ceo-memory/user_profile.md` (from main) | Personal identity |
| `data/brand/brand-dna.md` (from main) | Personal brand DNA |
| `data/strategy/audience-personas.md` (from main) | Personal audience data |
| `data/strategy/competitive-landscape.md` (from main) | Personal competitive data |
| `data/strategy/quarterly-roadmap.md` (from main) | Personal roadmap |
| `vault/**/*.md` (actual content) | Personal second brain |
| `.claude/settings.local.json` | Machine-specific, gitignored |
| `GITHUB-PUSH.md` | This file, gitignored |
