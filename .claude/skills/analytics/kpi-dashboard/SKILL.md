---
name: kpi-dashboard
user-invocable: false
description: Generate a KPI snapshot across all channels — the single most important data file in the system.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# KPI Dashboard Playbook

## Inputs

- $ARGUMENTS — Metrics data, platform stats, or "update from available data"
- `data/analytics/kpi-dashboard.md` — Existing dashboard
- `data/content/top-performers.md` — Content performance
- `data/social/` — Social metrics
- `data/marketing/` — Campaign data

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for KPI definitions and benchmarks
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Run `python3 -m scripts.analytics.aggregate_metrics` to gather current data
4. Read existing KPI dashboard and all available department data
5. If metrics data provided in $ARGUMENTS, use that. Otherwise, compile from available files.
6. Update the dashboard with current metrics organized by category:
   - **Content:** Posts published, total reach, avg engagement rate, top performer
   - **Social:** Followers per platform, follower growth rate, engagement rate per platform
   - **Email:** List size, growth rate, avg open rate, avg click rate
   - **Website:** Traffic (if available), top pages, bounce rate
   - **Revenue:** Total revenue, revenue by stream, MoM change
   - **Campaigns:** Active campaigns, performance vs KPIs
7. For each metric: current value, previous period, change (↑/↓/→), trend
8. Flag metrics that are significantly above or below target
9. Add date stamp so the dashboard shows when it was last updated

## Output

- Update `data/analytics/kpi-dashboard.md` (living document — overwrite with current snapshot)
- For scheduled runs: write to `data/inbox/daily-metrics-YYYY-MM-DD.md`
- Update your MEMORY.md with metric trends
