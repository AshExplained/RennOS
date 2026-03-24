---
name: maintenance-schedule
user-invocable: false
description: Create or review home maintenance schedule — seasonal tasks, recurring maintenance, and repair tracking.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Maintenance Schedule Playbook

## Inputs

- $ARGUMENTS — Tasks to add, "review" for what's due, or "create" for initial setup
- `data/personal/admin/maintenance-schedule.md` — Existing schedule (if any)

## Steps

1. Read existing maintenance data from `data/personal/admin/maintenance-schedule.md` if it exists
2. If creating initial schedule:
   - Build seasonal maintenance schedule with tasks at each frequency:
     - Monthly (filters, basic cleaning)
     - Quarterly (HVAC, gutters, deep clean)
     - Semi-annual (safety checks, seasonal prep)
     - Annual (major systems, inspections)
3. If reviewing:
   - Check what tasks are currently due
   - Flag overdue tasks
4. Track completed tasks with completion dates
5. Note recurring tasks for @schedule-manager to integrate into calendar

## Output

- Update `data/personal/admin/maintenance-schedule.md` (living document — use Edit to append/update, Write to create first time)
- Update your MEMORY.md with maintenance patterns and home details
