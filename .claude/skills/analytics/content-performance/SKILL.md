---
name: content-performance
user-invocable: false
description: Analyze which content pieces performed best and why — formats, topics, tones, timing patterns.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Content Performance Playbook

## Inputs

- $ARGUMENTS — Time period, platform, or specific content to analyze
- `data/content/top-performers.md` — Top content data
- `data/content/content-calendar.md` — Content history
- `data/social/` — Social performance data
- `data/analytics/kpi-dashboard.md` — Overall metrics

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read top performers, available content data, and KPI dashboard
4. Analyze content performance across dimensions:
   - **By format** — Blog vs social vs thread vs carousel vs video vs newsletter
   - **By topic** — Which themes/subjects get most engagement?
   - **By tone** — Educational vs personal vs controversial vs motivational
   - **By platform** — Where does each format perform best?
   - **By timing** — Day of week, time of day patterns
   - **By length** — Short vs long form engagement differences
5. Identify top 5 performers with specific evidence of why they worked
6. Identify bottom 5 performers with analysis of why they underperformed
7. Extract actionable patterns: "Content about [X] in [format] on [platform] consistently outperforms"

## Output

- Write to `data/analytics/content-performance-[period].md`
- Update `data/content/top-performers.md` with new findings
- Update your MEMORY.md with content patterns
