---
name: payment-tracker
user-invocable: false
description: Track outstanding payments — who owes what, when it's due, and what's overdue.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Payment Tracker Playbook

## Inputs

- $ARGUMENTS — New payment to log, or "review" for status check
- `data/finance/` — Existing invoices and tracker

## Steps

1. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/payment_status.py` to gather current data
2. Read existing payment tracker from `data/finance/` if it exists
3. If logging a new payment or invoice:
   - Add entry: client, invoice number, amount, date issued, due date, status (pending/paid/overdue)
   - Use Edit (append) — do NOT overwrite existing entries
4. If reviewing:
   - List all outstanding invoices
   - Calculate total outstanding amount
   - Flag overdue items (past due date, not paid)
   - For overdue items: days overdue, recommended action (gentle reminder, firm follow-up, escalate)
   - Calculate average days to payment across clients
5. If a payment is received:
   - Update status to "paid" with payment date
   - Update `data/finance/revenue-history.md` with the income
6. Maintain clean table format

## Output

- Update `data/finance/payment-tracker.md` (use Edit to append/update, Write to create first time)
- Update your MEMORY.md with payment patterns
