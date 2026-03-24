---
name: expense-log
user-invocable: false
description: Log and categorize personal expenses — keep a running record for budget tracking.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Expense Log Playbook

## Inputs

- $ARGUMENTS — Expense details to log (amount, what, category, etc.)
- `data/personal/finance/expense-log.md` — Existing expense log

## Steps

1. Read existing expense log from `data/personal/finance/expense-log.md`
2. Add the new entry with all required fields:
   - **Date** — when the expense occurred
   - **Amount** — how much was spent
   - **Category** — groceries, dining, transport, entertainment, shopping, bills, health, education, misc
   - **Description** — what the expense was for
   - **Payment Method** — cash, debit, credit, transfer
3. Use Edit to append the new entry — do NOT overwrite existing entries
4. Calculate and update running totals by category for the current month

## Output

- Update `data/personal/finance/expense-log.md` (living document — Edit append only)
- Update your MEMORY.md with any notable spending patterns observed
