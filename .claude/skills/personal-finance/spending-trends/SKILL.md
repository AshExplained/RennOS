---
name: spending-trends
user-invocable: false
description: Analyze spending trends — where is money going, what's increasing, what patterns emerge?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Spending Trends Playbook

## Inputs

- $ARGUMENTS — Time period to analyze, or specific category to focus on
- `data/personal/finance/expense-log.md` — Expense history
- `data/personal/finance/budget-*.md` — Budget data for comparison

## Steps

1. Read expense log from `data/personal/finance/expense-log.md`
2. Read relevant budgets from `data/personal/finance/budget-*.md`
3. Analyze spending by category:
   - **Highest spend** categories — where is the most money going?
   - **Fastest growing** categories — what's increasing month over month?
4. Month-over-month comparison:
   - Categories **increasing** in spend
   - Categories **decreasing** in spend
   - Net direction of total spending
5. Identify patterns:
   - **Seasonal** — predictable spikes tied to time of year
   - **Emotional** — stress spending, reward spending, impulse patterns
   - **Lifestyle creep** — gradual increases in baseline spending
6. Flag anomalies — unusual one-time charges or unexpected spikes
7. Compare trends against budget targets
8. Flag concerning trends that need attention
9. Identify easy wins — categories where small changes yield meaningful savings
10. Provide specific, actionable recommendations

## Output

- Write the analysis to `data/personal/finance/spending-trends-[date].md`
- Update your MEMORY.md with key trends and recommendations
