---
name: invoice-draft
user-invocable: false
description: Draft an invoice — all required fields, professional formatting, ready for the user to send.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Invoice Draft Playbook

## Inputs

- $ARGUMENTS — Client name, services, amount, terms
- `data/partnerships/` — Deal structure for details
- `data/finance/rate-card.md` — Standard rates

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read deal structure from `data/partnerships/` if available, and rate card
3. Draft the invoice with required fields:
   - **Invoice number** — Sequential (check existing invoices in `data/finance/` for last number)
   - **Date** — Today's date
   - **Due date** — Based on payment terms (net 15, net 30, etc.)
   - **From** — the user's business name and contact info [FILL IN]
   - **Bill to** — Client name, company, address, email
   - **Line items** — Description, quantity, unit price, total per item
   - **Subtotal**
   - **Tax** — If applicable [SPECIFY RATE]
   - **Total**
   - **Payment terms** — When due, late fee policy, accepted payment methods
   - **Payment instructions** — Bank details, PayPal, Stripe, etc. [FILL IN]
   - **Notes** — Any additional terms or thank-you
4. Mark fields the user needs to fill in with [BRACKETS]
5. Keep formatting clean and professional

## Output

- Write to `data/finance/invoice-[client]-[number]-[date].md`
- **Reminder:** Invoices are DRAFTS. the user sends them manually.
- Update your MEMORY.md with invoice patterns
