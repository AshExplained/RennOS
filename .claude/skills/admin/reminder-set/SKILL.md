---
name: reminder-set
user-invocable: false
description: Set a reminder for something important — captures the thing so the user doesn't have to hold it in memory.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Reminder Set Playbook

## Inputs

- $ARGUMENTS — What to remember, when to be reminded, and any relevant context
- `data/personal/admin/reminders.md` — Existing reminders (if any)

## Steps

1. Read existing reminders from `data/personal/admin/reminders.md` if it exists
2. Add the new reminder with: what, when, and context
3. If time-specific, note for @schedule-manager to integrate into calendar
4. If recurring, note frequency (daily/weekly/monthly/etc.)
5. Use Edit (append) — do NOT overwrite existing reminders

## Output

- Update `data/personal/admin/reminders.md` (living document — use Edit to append/update, Write to create first time)
- Update your MEMORY.md with reminder patterns
