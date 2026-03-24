---
name: budget-review
user-invocable: false
description: Review spending vs budget — where are we over, under, and what to adjust?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Budget Review Playbook

## Inputs

- $ARGUMENTS — Month/year to review, or "latest" for most recent
- `data/personal/finance/budget-[month]-[year].md` — Budget for the period
- `data/personal/finance/expense-log.md` — Actual spending data

## Steps

1. Read the budget for the specified period from `data/personal/finance/`
2. Read the expense log from `data/personal/finance/expense-log.md`
3. Compare actual spending vs budgeted amount for each category
4. Calculate variance (amount and percentage) with trends vs previous months
5. Flag overages — any category exceeding budget by more than 10%
6. Identify savings opportunities — categories consistently under budget
7. Recommend adjustments for next month's budget based on findings
8. Provide an overall verdict:
   - On track / Needs attention / Off track
   - Total spent vs total budgeted
   - Net savings vs savings target

## Output

- Write the review to `data/personal/finance/budget-review-[month]-[year].md`
- Update your MEMORY.md with spending patterns and key takeaways
