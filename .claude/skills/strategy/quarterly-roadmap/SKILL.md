---
name: quarterly-roadmap
user-invocable: false
description: Build a quarterly plan from all department inputs — themes, campaigns, content pillars, milestones, and KPIs.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Quarterly Roadmap Playbook

## Inputs

- $ARGUMENTS — Quarter (e.g., "Q2 2026"), goals, and any constraints
- `data/brand/brand-dna.md` — Brand foundation
- `data/strategy/audience-personas.md` — Target audience
- `data/strategy/competitive-landscape.md` — Competitive context
- Trend scans in `data/strategy/` — Recent trends
- `data/content/content-calendar.md` — Current content schedule
- `data/analytics/kpi-dashboard.md` — Performance metrics

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for planning methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read all input files listed above (skip any that are empty/placeholder)
4. Synthesize key insights:
   - What's working? (from analytics)
   - What does the audience need? (from personas)
   - What are competitors doing? (from landscape)
   - What trends should we ride? (from scans)
5. Define 3-4 quarterly themes that align with brand positioning
6. Map themes to monthly focus areas:
   - Month 1: [theme/focus]
   - Month 2: [theme/focus]
   - Month 3: [theme/focus]
7. Define campaigns per month with:
   - Campaign name
   - Objective
   - Key deliverables
   - Responsible department/agent
8. Set milestones and KPIs for the quarter
9. Identify cross-department dependencies
10. Flag risks and mitigation strategies

## Output

- Write to `data/strategy/quarterly-roadmap.md`
- Update your MEMORY.md with key decisions and rationale
