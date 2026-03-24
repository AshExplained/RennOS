---
name: cashflow-check
user-invocable: false
description: Analyze cash flow — income timing vs expense timing. Flag potential cash crunches before they happen.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Cash Flow Check Playbook

## Inputs

- $ARGUMENTS — Period to analyze, any known upcoming expenses or income
- `data/finance/revenue-dashboard.md` — Current revenue
- `data/finance/revenue-history.md` — Historical revenue data
- `data/operations/budget-tracker.md` — Expense tracking

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for cash flow methodology
2. Apply the analysis framework and warning thresholds from the reference
3. Read revenue dashboard, revenue history, and budget tracker
4. Map cash inflows by timing:
   - When does revenue actually arrive? (payment terms, invoice aging)
   - Any large payments expected? (sponsorship payouts, product launches)
   - Seasonal revenue patterns?
5. Map cash outflows by timing:
   - Fixed monthly expenses (tools, subscriptions, contractors)
   - Variable expenses (ad spend, production costs)
   - Large upcoming expenses (events, product development, legal)
   - Annual/quarterly payments (insurance, taxes, renewals)
6. Calculate net cash position month by month
7. Flag cash crunch risks:
   - Months where outflows exceed inflows
   - Low cash buffer periods
   - Large payment timing mismatches
8. Recommend actions to smooth cash flow (adjust payment terms, time launches, build reserve)

## Output

- Write to `data/finance/cashflow-check-[date].md`
- Update your MEMORY.md with cash flow patterns
