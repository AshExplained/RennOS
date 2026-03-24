---
name: budget-tracker
user-invocable: false
description: Track spending and budget allocation across tools, vendors, ads, and contractors.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Budget Tracker Playbook

## Inputs

- $ARGUMENTS — New expense to log, or "review" for spending summary
- `data/operations/` — Existing budget tracker
- `data/finance/` — Financial data

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read existing budget tracker from `data/operations/` if it exists
3. If logging new expense:
   - Add entry: date, category (tools/vendors/ads/contractors/sponsorships), description, amount, frequency (one-time/monthly/annual), department
   - Use Edit (append) — do NOT overwrite existing entries
4. If reviewing:
   - Summarize spending by category
   - Compare against budget allocation (if defined)
   - Flag overspend categories
   - Calculate total monthly burn rate
   - Identify potential savings (unused tools, overlapping services)
5. Maintain clean table format for easy scanning

## Output

- Update `data/operations/budget-tracker.md` (use Edit to append, Write to create first time)
- Update your MEMORY.md with spending patterns
