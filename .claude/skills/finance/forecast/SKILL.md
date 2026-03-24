---
name: forecast
user-invocable: false
description: Revenue forecast for upcoming quarter or year — based on historical data, current pipeline, and growth projections.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Revenue Forecast Playbook

## Inputs

- $ARGUMENTS — Forecast period, assumptions, any known upcoming deals
- `data/finance/revenue-history.md` — Historical revenue data
- `data/finance/revenue-dashboard.md` — Current dashboard
- `data/partnerships/` — Pipeline data
- `data/strategy/quarterly-roadmap.md` — Planned launches/campaigns

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for forecasting methodology
2. Apply the forecasting methods and scenario planning from the reference
3. Read revenue history, current dashboard, pipeline, and roadmap
4. Build the forecast:
   - **Base case** — Current run-rate projected forward (no new initiatives)
   - **Growth case** — Accounting for planned launches, campaigns, and pipeline deals
   - **Conservative case** — Base minus risk factors (lost clients, market changes)
5. For each case, project month by month:
   - Revenue by stream
   - Total revenue
   - Key assumptions underlying each projection
6. Identify key drivers that make the difference between cases:
   - Which deals need to close?
   - Which launches need to succeed?
   - What audience growth is assumed?
7. Flag risks to the forecast and mitigation strategies
8. Define monthly check-in points to validate forecast accuracy

## Output

- Write to `data/finance/forecast-[period].md`
- Update your MEMORY.md with forecast assumptions and accuracy
