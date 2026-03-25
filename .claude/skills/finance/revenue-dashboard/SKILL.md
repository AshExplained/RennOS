---
name: revenue-dashboard
user-invocable: false
description: Generate a revenue snapshot across all income streams — the financial equivalent of the KPI dashboard.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Revenue Dashboard Playbook

## Inputs

- $ARGUMENTS — Period or "current month", any new revenue data to log
- `data/finance/revenue-history.md` — Historical revenue data
- `data/finance/revenue-dashboard.md` — Current dashboard
- `data/partnerships/` — Deal data

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Run `python3 -m scripts.finance.revenue_summary` to gather current data
3. Read existing revenue dashboard and revenue history
4. If new revenue data provided in $ARGUMENTS, incorporate it
5. Update the dashboard:
   - **Total revenue** — Current period + YTD
   - **Revenue by stream** — Each stream with amount, % of total, trend
   - **Month-over-month change** — Growth or decline with %
   - **Year-over-year comparison** — If historical data exists
   - **Outstanding invoices** — Total owed, days outstanding
   - **Pipeline** — Deals in negotiation with estimated value
6. Flag significant changes (>20% swing in any stream)
7. Add date stamp for currency

## Output

- Update `data/finance/revenue-dashboard.md` (living document — overwrite with current snapshot)
- Update your MEMORY.md with revenue patterns
