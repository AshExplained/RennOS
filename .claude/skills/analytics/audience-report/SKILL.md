---
name: audience-report
user-invocable: false
description: Deep dive into audience demographics, behavior, and engagement patterns — the quantitative companion to persona research.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Audience Report Playbook

## Inputs

- $ARGUMENTS — Platform focus or "all platforms", any analytics data
- `data/strategy/audience-personas.md` — Audience personas (qualitative)
- `data/analytics/kpi-dashboard.md` — Overall metrics
- `data/social/` — Social platform data

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read audience personas, KPI dashboard, and social data
3. Research platform demographic benchmarks via web for context
4. Analyze audience data:
   - **Demographics** — Age, location, gender, profession (per platform)
   - **Behavior** — When are they active? How do they engage? (likes vs comments vs shares vs saves)
   - **Growth** — Where are new followers coming from? What's driving growth?
   - **Engagement quality** — Are engaged followers the right people? (persona match)
   - **Platform distribution** — Where is the audience concentrated?
5. Compare against audience personas — does the data match who we think our audience is?
6. Flag mismatches between persona assumptions and actual data
7. Recommend persona refinements based on quantitative evidence

## Output

- Write to `data/analytics/audience-report-[date].md`
- Update your MEMORY.md with audience data insights
