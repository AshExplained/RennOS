---
name: growth-tactics
user-invocable: false
description: Research and recommend engagement and growth strategies tailored to the user's brand, audience, and platforms.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Growth Tactics Playbook

## Inputs

- $ARGUMENTS — Platform focus, specific growth goal, current metrics (if available)
- `data/brand/brand-dna.md` — Brand identity (growth must not compromise this)
- `data/strategy/audience-personas.md` — Audience profiles
- `data/analytics/kpi-dashboard.md` — Performance data (when available)
- `data/content/top-performers.md` — What content works best (when available)

## Steps

1. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and available analytics
2. Research current growth tactics via web:
   - Platform algorithm updates
   - What's working for peers/competitors
   - Emerging engagement formats
   - Community-building strategies
3. For each recommended tactic:
   - What it is and why it works
   - How it aligns with the user's brand (no growth hacking that compromises brand integrity)
   - Expected effort and timeline
   - Expected impact
   - How to measure success
4. Prioritize tactics by impact-to-effort ratio
5. Provide a 30-day growth action plan

## Output

- Write to `data/social/growth-tactics-[date].md`
- Update your MEMORY.md with which growth approaches work and platform algorithm changes
