---
name: weekly-digest
user-invocable: false
description: Compile a weekly digest of key metrics, highlights, and action items — the CEO agent reads this every Monday.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Weekly Digest Playbook

## Inputs

- $ARGUMENTS — Week ending date, or "current week"
- `data/analytics/kpi-dashboard.md` — Current metrics
- `data/content/top-performers.md` — Content performance
- `data/social/` — Social data
- `data/operations/` — Project status
- `data/inbox/` — Any reports from the week

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for digest structure, metric selection, executive summary writing, and formatting standards
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/compile_weekly_data.py` to gather current data
4. Read KPI dashboard, top performers, and latest data from all departments
5. Compile the digest with consistent sections (same format every week):
   - **Week overview** — One-line summary of the week
   - **Key metrics** — Top 5-7 KPIs with this week vs last week
   - **Wins** — What went well (top content, milestones hit, growth spikes)
   - **Concerns** — What underperformed or needs attention
   - **Content performance** — Top 3 posts of the week with metrics
   - **Growth snapshot** — Follower/subscriber changes per platform
   - **Active projects** — Status of in-flight work (from operations data)
   - **Action items** — What needs to happen next week
6. Keep it scannable — the CEO agent should be able to read this in 2 minutes
7. Use consistent formatting so week-over-week comparison is easy

## Output

- Write to `data/analytics/weekly-digest-[date].md`
- For scheduled runs: `data/inbox/weekly-digest-YYYY-MM-DD.md`
- Update your MEMORY.md with weekly trends
