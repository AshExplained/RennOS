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
1. Clone: `git clone https://github.com/AshExplained/RennOS.git`
2. Enter: `cd RennOS`
3. Start: `claude`
4. Run: `/wake-up`
5. The CEO agent will interview you and set up the entire system

## Profiles

During onboarding, choose how you want to use RennOS:

| Profile | Departments | Best for |
|---------|------------|----------|
| **Full RennOS** | All 20 | Brand + business + personal life |
| **Brand & Business** | 15 depts | Professional brand management only |
| **Life OS** | 7 depts | Personal life management only |

You can upgrade or switch profiles anytime.

## Updating

When new agents, skills, or features are released:

```bash
node update.js
```

This pulls the latest system files without touching your personal data (profile, brand DNA, memories, vault).

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
- `docs/claude-code-meta.md` — Claude Code feature reference
