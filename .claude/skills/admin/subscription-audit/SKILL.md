---
name: subscription-audit
user-invocable: false
description: Audit all subscriptions — what you're paying for, what you're actually using, and what to cancel.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Subscription Audit Playbook

## Inputs

- $ARGUMENTS — Subscription data, or "review" to audit existing list
- `data/personal/admin/subscription-audit-*.md` — Previous audits (if any)
- `data/personal/admin/renewal-tracker.md` — Renewal dates

## Steps

1. Run `python3 ${CLAUDE_SKILL_DIR}/scripts/subscription_summary.py` to gather current data
2. Read existing subscription data and previous audits if available
3. For each subscription, document:
   - Service name
   - Monthly/annual cost
   - Billing date
   - Usage level (daily/weekly/rarely/never)
   - Value assessment (essential/useful/questionable/waste)
4. Calculate total monthly spend and projected annual spend
5. Recommend action for each: keep / downgrade / cancel
6. Flag any renewals coming up in the next 30 days
7. Feed cost data to @expense-tracker (Dept 19) for budget tracking

## Output

- Write to `data/personal/admin/subscription-audit-[date].md`
- Update your MEMORY.md with subscription patterns and savings identified
