---
name: growth-report
user-invocable: false
description: Track and analyze audience growth patterns — what's driving growth, what's stalling, and projections.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Growth Report Playbook

## Inputs

- $ARGUMENTS — Time period, platform focus
- `data/analytics/kpi-dashboard.md` — Overall metrics
- `data/social/` — Social platform data
- `data/marketing/` — Campaign data

## Steps

1. Read KPI dashboard, social data, and marketing data
2. Research platform growth benchmarks via web
3. Analyze growth metrics:
   - **Follower growth** per platform — absolute numbers and growth rate
   - **Email list growth** — subscribers, growth rate, churn rate
   - **Website traffic growth** — visitors, page views, returning vs new
   - **Revenue growth** — if applicable
4. Identify growth drivers:
   - Which content drives follower spikes?
   - Which channels contribute most new followers?
   - Viral moments or features that drove growth
5. Identify growth blockers:
   - Plateaus or declines — what caused them?
   - Channels that aren't growing despite investment
6. Project growth trajectory — at current rate, where will metrics be in 30/60/90 days?

## Output

- Write to `data/analytics/growth-report-[period].md`
- Update your MEMORY.md with growth patterns
