---
name: executive-summary
user-invocable: false
description: Create an executive summary for the user's personal review — high-level business health across all departments.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Executive Summary Playbook

## Inputs

- $ARGUMENTS — Time period: "this month", "Q1", or specific
- `data/analytics/` — All analytics data
- `data/operations/` — Operations data
- `data/finance/` — Financial data
- `data/strategy/quarterly-roadmap.md` — Strategic milestones

## Steps

1. Read all available analytics, operations, finance, and strategy data
2. Create a high-level executive summary:
   - **Business health** — Overall assessment (thriving / growing / stable / at risk)
   - **Revenue** — Current revenue, trend, vs target
   - **Audience growth** — Total reach, growth rate, key platform changes
   - **Content** — Performance summary, what's working
   - **Campaigns** — Active campaigns, status, ROI
   - **Operations** — Projects on track vs at risk, resource utilization
   - **Partnerships** — Active deals, pipeline, revenue from partnerships
   - **Key decisions needed** — What requires the user's input
3. Keep it under 1 page equivalent — this is the 30,000-foot view
4. End with "Top 3 priorities for next period"

## Output

- Write to `data/analytics/executive-summary-[period].md`
- Update your MEMORY.md with business health trends
