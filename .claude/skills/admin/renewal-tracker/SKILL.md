---
name: renewal-tracker
user-invocable: false
description: Track upcoming subscription renewals and cancellation deadlines — never miss a cancellation window.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Renewal Tracker Playbook

## Inputs

- $ARGUMENTS — Subscription to add/update, or "review" for upcoming renewals
- `data/personal/admin/renewal-tracker.md` — Existing tracker (if any)

## Steps

1. Run `python3 -m scripts.admin.renewal_check` to gather current data
2. Read existing renewal tracker from `data/personal/admin/renewal-tracker.md` if it exists
3. If adding a subscription:
   - Log: service name, renewal date, cost, auto-renew (yes/no), cancellation deadline
   - Use Edit (append) — do NOT overwrite existing entries
4. If reviewing:
   - List renewals coming up in 7 days, 14 days, and 30 days
   - Flag cancellation deadlines that are approaching
   - Highlight services previously marked for cancellation (from subscription audits)
5. Maintain clean, scannable table format

## Output

- Update `data/personal/admin/renewal-tracker.md` (living document — use Edit to append/update, Write to create first time)
- Update your MEMORY.md with renewal patterns and upcoming deadlines
