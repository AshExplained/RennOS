---
name: performance-report
user-invocable: false
description: Detailed performance report for a specific time period — deeper than the dashboard, with analysis and recommendations.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Performance Report Playbook

## Inputs

- $ARGUMENTS — Time period: "last week", "March 2026", "Q1 2026"
- `data/analytics/kpi-dashboard.md` — Current metrics
- `data/content/top-performers.md` — Content performance
- `data/social/` — Social metrics
- `data/marketing/` — Campaign data

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read dashboard and all available performance data
3. Compile detailed metrics for the specified period:
   - Per-channel breakdown (content, social, email, paid, revenue)
   - Top performers and worst performers with analysis
   - Trends: what's improving, what's declining
4. Analyze patterns:
   - What worked and why
   - What didn't work and why
   - Emerging opportunities
   - Risks or warning signs
5. Provide specific recommendations based on the data
6. Compare against previous period — improvement or regression?

## Output

- Write to `data/analytics/performance-report-[period].md`
- Update your MEMORY.md with performance patterns
