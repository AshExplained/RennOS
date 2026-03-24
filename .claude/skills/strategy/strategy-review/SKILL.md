---
name: strategy-review
user-invocable: false
description: Review progress against the quarterly roadmap — what's on track, what's at risk, and recommended adjustments.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Strategy Review Playbook

## Inputs

- $ARGUMENTS — Review period and any specific concerns to address
- `data/strategy/quarterly-roadmap.md` — Current roadmap and milestones
- `data/analytics/kpi-dashboard.md` — Performance metrics
- `data/analytics/insights-log.md` — Accumulated insights
- `data/content/top-performers.md` — Top-performing content

## Current State
!`cat data/strategy/quarterly-roadmap.md 2>/dev/null`

## Steps

1. Read the current roadmap and all analytics data
2. For each milestone in the roadmap, assess status:
   - **On Track** — Progressing as planned
   - **At Risk** — Behind schedule or underperforming
   - **Behind** — Significantly off target
3. Analyze what worked:
   - Which campaigns/content hit their KPIs?
   - What surprised us (positive)?
4. Analyze what didn't work:
   - Which initiatives underperformed?
   - What were the root causes?
5. Identify strategic pivots needed:
   - Should any themes be adjusted?
   - Should resource allocation change?
   - Are there new opportunities since the roadmap was set?
6. Recommend specific adjustments with rationale

## Output

- Write review to `data/strategy/strategy-review-[date].md` (use today's date in YYYY-MM-DD format)
- If adjustments are approved by the CEO agent/user, update `data/strategy/quarterly-roadmap.md`
- Update your MEMORY.md with key findings
