---
name: income-report
user-invocable: false
description: Detailed income report for a specific time period — full breakdown by stream, source, and trend.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Income Report Playbook

## Inputs

- $ARGUMENTS — Time period, any specific revenue data
- `data/finance/revenue-history.md` — Historical revenue data
- `data/finance/revenue-dashboard.md` — Current dashboard

## Steps

1. Read revenue history and dashboard
2. Compile detailed report for the specified period:
   - Revenue by stream with amounts and percentages
   - Revenue by client/source (for consulting, sponsorships)
   - Comparison to previous period (MoM, QoQ, YoY as applicable)
   - Highest-value transactions
   - New revenue sources (first-time income from a stream)
3. Analyze the period:
   - What drove revenue growth?
   - What caused any declines?
   - Seasonal patterns?
4. Update `data/finance/revenue-history.md` with new period data

## Output

- Write to `data/finance/income-report-[period].md`
- Scheduled runs: Write to `data/inbox/revenue-report-YYYY-MM.md`
- **Scheduled:** Monthly 1st 8am → writes to `data/inbox/` (requires `/loop` or scheduler — currently on-demand only)
- Update your MEMORY.md with revenue trends
