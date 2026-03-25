---
name: conflict-check
user-invocable: false
description: Check for scheduling conflicts and resource overlaps across all calendars.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Conflict Check Playbook

## Inputs

- $ARGUMENTS — Time period to check, or specific date/event to check against
- `data/operations/master-calendar.md` — Master calendar
- `data/content/content-calendar.md` — Content schedule
- `data/pr/` — PR calendar files

## Steps

1. Run `python3 -m scripts.ops.calendar_conflict_check` to gather current data
2. Read master calendar, content calendar, and PR calendar files
3. Scan for conflicts:
   - **Date conflicts** — Multiple events/deadlines on the same day that require the user's attention
   - **Resource conflicts** — Same content needed for two purposes simultaneously
   - **Sequence conflicts** — Dependent tasks where prerequisite isn't scheduled before the dependent
   - **Overload days** — Too many deliverables due on one day
4. For each conflict found:
   - What's conflicting
   - Why it's a problem
   - Recommended resolution (reschedule, reprioritize, delegate)
5. If no conflicts found, confirm the schedule is clean

## Output

- Write to `data/operations/conflict-check-[date].md`
- Update your MEMORY.md with conflict patterns
