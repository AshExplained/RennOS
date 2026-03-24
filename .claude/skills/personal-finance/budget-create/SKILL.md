---
name: budget-create
user-invocable: false
description: Create or update monthly personal budget — income, expenses by category, savings allocation.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Budget Create Playbook

## Inputs

- $ARGUMENTS — Month/year to budget for, any specific notes or constraints
- `data/personal/finance/` — Existing budgets and financial data
- `data/finance/revenue-dashboard.md` — Business income to factor in

## Steps

1. Read existing budgets from `data/personal/finance/` to understand historical patterns
2. Read `data/finance/revenue-dashboard.md` for current business income
3. Structure the budget into clear sections:
   - **Income** — salary, business revenue, side income, passive income
   - **Fixed Expenses** — rent/mortgage, subscriptions, insurance, loan payments
   - **Variable Expenses** — groceries, dining, transport, entertainment, shopping
   - **Savings** — emergency fund, investment contributions, goal-specific savings
   - **Buffer** — unallocated cushion for unexpected expenses
4. Apply the 50/30/20 framework (needs/wants/savings) as default, or custom framework if the user specifies one
5. Compare against last month's budget — flag any significant changes
6. Flag categories likely to go over based on historical spending patterns
7. Present the budget in a clean table format with totals per section

## Output

- Write the budget to `data/personal/finance/budget-[month]-[year].md`
- Update your MEMORY.md with budget highlights and any concerns flagged
