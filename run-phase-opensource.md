## RennOS — Open-Source Prep: Make the System Universal

**Goal:** Convert RennOS from Ash's personal system to a universal template anyone can clone and use. Both branches (main + template) get the same structural changes. Only difference: main has Ash's data populated, template has blank placeholders.

**Key principle:** The system adapts to the user, the user doesn't edit system files. User name and CEO agent name are set during onboarding and stored in `user_profile.md`. CLAUDE.md and all agents reference this file instead of hardcoding names.

---

### Before You Start

1. Read `CLAUDE.md` — understand current structure
2. Read `.claude/ceo-memory/user_ash.md` — this becomes `user_profile.md`
3. Read `.claude/skills/wake-up/SKILL.md` — Path A needs to ask for CEO agent name
4. Read `.claude/ceo-memory/org-chart.md` — references "Tony" throughout

---

### Step 1: Rename user_ash.md → user_profile.md

Rename the file:
```bash
mv .claude/ceo-memory/user_ash.md .claude/ceo-memory/user_profile.md
```

Update ALL references to this file across the codebase. Search and replace:
- `user_ash.md` → `user_profile.md`
- `ceo-memory/user_ash.md` → `ceo-memory/user_profile.md`

Files that reference it (at minimum):
- `CLAUDE.md` (memory system section)
- `.claude/ceo-memory/MEMORY.md` (index)
- `.claude/skills/wake-up/SKILL.md` (brain reload + onboarding)
- Multiple agent files (primary data files section)
- Multiple skill files (inputs section)

Run a full grep to find all references:
```bash
grep -rl "user_ash" .claude/ CLAUDE.md
```

---

### Step 2: Make CLAUDE.md Generic

Current line 5:
```
You are **Tony** — the CEO and main orchestrator of Ash's RennOS.
The user is **Ash** — the founder and owner.
```

Replace with:
```
You are the **CEO agent** of RennOS — the main orchestrator.
On wake-up, read `.claude/ceo-memory/user_profile.md` for your name and the user's name. Use those names throughout the session. If user_profile.md is empty, Path A (onboarding) will set them up.
```

Also update line 11:
```
- You report to Ash. No one else.
```
Replace with:
```
- You report to the user. No one else.
```

And any other hardcoded "Ash" references in CLAUDE.md — replace with "the user" or "the owner."

---

### Step 3: Update user_profile.md Structure

Add CEO agent name as a field at the top of the profile. Current content stays (it's Ash's data on main branch).

Add these fields to the top of user_profile.md (above the existing content):
```markdown
## System Config
- **User name:** Ash
- **CEO agent name:** Tony
```

On the template branch, the entire file will be:
```markdown
# User Profile

## System Config
- **User name:** [Set during onboarding]
- **CEO agent name:** [Set during onboarding]

<!-- Everything below is populated during onboarding (/wake-up Path A) -->
```

---

### Step 4: Update Wake-Up Skill — Path A (Onboarding)

Add two new questions at the very START of the interview, before Layer 1:

```markdown
### Step 0: Set Up Identity

Before the interview, ask two quick setup questions:

1. "What should I call you?" → Save as **User name** in user_profile.md
2. "And what would you like to call me? I'm your CEO agent — pick a name that feels right." → Save as **CEO agent name** in user_profile.md

Use these names throughout the rest of the session and all future sessions.
```

Also update Path A's "Save Ash's profile" instruction:
- Current: "Save Ash's profile and preferences to `.claude/ceo-memory/user_ash.md`"
- New: "Save the user's profile and preferences to `.claude/ceo-memory/user_profile.md`, keeping the System Config section (name + CEO name) at the top"

---

### Step 5: Update Wake-Up Skill — Path B (Daily Briefing)

Add to Step 1 (Reload your brain), after reading user_profile.md:

```markdown
After reading user_profile.md, use the **User name** and **CEO agent name** from the System Config section for all interactions this session.
```

---

### Step 6: Generalize Agent Files (99 agents)

All 99 agent files contain hardcoded references to "Ash" in places like:
- "Tony will present them to Ash"
- "Ash approves"
- "Ash sends them manually"
- "Ash's brand"

Do a global find-replace across ALL `.claude/agents/*.md` files:

| Find | Replace with |
|---|---|
| `to Ash` | `to the user` |
| `Ash approves` | `the user approves` |
| `Ash sends` | `the user sends` |
| `Ash's explicit` | `the user's explicit` |
| `Ash's brand` | `the user's brand` |
| `Ash (Sponsor)` | `the user (Sponsor)` |
| `presents to Ash` | `presents to the user` |
| `Ash reviews` | `the user reviews` |
| `Ash tests` | `the user tests` |
| `Ash says` | `the user says` |
| `for Ash` | `for the user` |

**Do NOT replace:**
- "Ash" inside data files (brand-dna.md, personas, roadmap) — that's Ash's personal data, stays on main
- "Ash" inside agent memory files — that's onboarding output
- "Ash" inside the wake-up interview questions — those are prompts, not hardcoded names

**Also replace "Tony" in:**
- `.claude/ceo-memory/org-chart.md` — "Tony's routing guide" → "CEO routing guide"
- `.claude/ceo-memory/workflows.md` — "Tony is Product Owner" → "the CEO agent is Product Owner", "Tony presents" → "the CEO agent presents"
- Agent files where "Tony" appears — "Reports to Tony" → "Reports to the CEO agent", "Tony will present" → "the CEO agent will present"

---

### Step 7: Update CEO Memory Files

**org-chart.md:**
- Title: "Tony's routing guide" → "CEO Agent Routing Guide"
- All "Tony" references → "the CEO agent"

**workflows.md:**
- "Tony is Product Owner" → "the CEO agent is Product Owner"
- "Tony presents" → "the CEO agent presents"
- All "Ash (Sponsor)" → "the user (Sponsor)"

**MEMORY.md (index):**
- Update `user_ash.md` → `user_profile.md` entry

**tools.md:**
- "Ash checks from phone" → "the user checks from phone"
- "Ash and Tony" → "the user and CEO agent"

---

### Step 8: Update Skill Files

Skills that hardcode "Ash" in their instructions (not data references):

Do global find-replace across ALL `.claude/skills/**/SKILL.md`:

| Find | Replace with |
|---|---|
| `to Ash` | `to the user` |
| `Ash's` | `the user's` |
| `for Ash` | `for the user` |
| `Ash sends` | `the user sends` |
| `Ash approves` | `the user approves` |
| `presents to Ash` | `presents to the user` |

Same principle: replace in instructions, NOT in data content or interview prompts.

---

### Step 9: Move Non-Runtime Files to docs/

```bash
mkdir -p docs/archive
mv brainstorm.md docs/archive/
mv claude-code-meta.md docs/
mv run-phase-quality-upgrade.md docs/archive/
```

Update CLAUDE.md Key Paths table:
- Remove brainstorm.md row (or update path to `docs/archive/brainstorm.md`)

---

### Step 10: Add Open-Source Files

**`README.md`** — Create in project root:
```markdown
# RennOS — AI-Powered Life & Brand Operating System

A personal brand management + life management system powered by Claude Code.
99 AI agents across 20 departments, orchestrated by a CEO agent who reports to you.

## What It Does
- Manages your personal brand (strategy, content, social, PR, marketing, partnerships)
- Handles life admin (health, relationships, growth, finances, tasks)
- Builds software products (Scrum dev team with Asana + GitHub)
- Creates video content (Remotion + Stitch integration)
- Processes your Obsidian vault (web clippings, journal, knowledge management)

## Quick Start
1. Clone: `git clone https://github.com/[you]/rennos.git`
2. Enter: `cd rennos`
3. Start: `claude`
4. Run: `/wake-up`
5. The CEO agent will interview you and set up the entire system

## Requirements
- Claude Code CLI (with Claude Pro/Max subscription)
- Node.js (for Remotion, Stitch skills)
- Python 3 (for data scripts)
- Optional: Obsidian (vault management), Asana (project management), GitHub CLI

## Architecture
- 20 departments, 99 agents, 230+ skills
- CEO agent orchestrates everything via delegation
- 3 modes: Subagent (simple), Chaining (multi-step), Agent Teams (complex)
- All agents produce drafts — the user approves before anything goes live

## Docs
- `docs/ARCHITECTURE.md` — System design
- `docs/claude-code-meta.md` — Claude Code feature reference
```

**`LICENSE`** — MIT or your preferred license.

---

### Step 11: Create Template Branch

```bash
git init  # if not already a git repo
git add -A
git commit -m "RennOS v1.0 — full system with personal data"

# Create template branch
git checkout -b template

# On template branch: reset personal data files to placeholders
```

On the template branch, replace these 9 files with blank placeholders:
1. `.claude/ceo-memory/user_profile.md` → blank template with System Config section only
2. `data/brand/brand-dna.md` → comment placeholder
3. `data/strategy/audience-personas.md` → comment placeholder
4. `data/strategy/competitive-landscape.md` → comment placeholder
5. `data/strategy/quarterly-roadmap.md` → comment placeholder
6. `.claude/agent-memory/brand-strategist/MEMORY.md` → blank
7. `.claude/agent-memory/audience-researcher/MEMORY.md` → blank
8. `.claude/agent-memory/competitive-intel-analyst/MEMORY.md` → blank
9. `.claude/agent-memory/strategy-planner/MEMORY.md` → blank

Also blank the `.env` file (remove any real keys, keep placeholders).

```bash
git add -A
git commit -m "RennOS template — ready for new users"
git checkout main  # back to your personal branch
```

---

### Testing Checklist

- [ ] `/wake-up` Path A asks for user name and CEO agent name
- [ ] CEO agent uses the chosen name throughout the session
- [ ] No hardcoded "Ash" or "Tony" in agent instructions or CLAUDE.md
- [ ] `user_profile.md` stores both names in System Config section
- [ ] All 99 agent files say "the user" not "Ash"
- [ ] org-chart says "CEO Agent" not "Tony"
- [ ] Template branch has blank data files
- [ ] Main branch still has all of Ash's data intact
- [ ] README.md exists with setup instructions
- [ ] `docs/` contains reference material moved from root

---

### What NOT to Change

- **Skill playbook content** — Steps, methodology, frameworks are universal already
- **Reference files** — best-practices.md files are domain knowledge, not personal
- **Templates** — Output formats are universal
- **Scripts** — Python scripts work for anyone
- **Agent frontmatter** — names, tools, models, skills are universal
- **Settings.json** — env vars and permissions are universal
- **Stitch skills** — Google's skills work for everyone
