---
name: master-calendar
user-invocable: false
description: Maintain the master calendar — sync events, deadlines, and milestones from all department calendars into one unified view.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Master Calendar Playbook

## Inputs

- $ARGUMENTS — New event to add, or "sync" to pull from all department calendars
- `data/operations/master-calendar.md` — Existing master calendar
- `data/content/content-calendar.md` — Content schedule
- `data/pr/` — PR calendar files
- `data/partnerships/` — Event briefs
- `data/strategy/quarterly-roadmap.md` — Strategic milestones

## Steps

1. Run `python3 -m scripts.ops.merge_calendars` to gather current data
2. Read existing master calendar from `data/operations/master-calendar.md`
3. If adding a new event:
   - Add entry: date, event/milestone, department, type (content/PR/launch/event/personal), status
   - Use Edit to append
4. If syncing:
   - Read content calendar, PR calendar files, event briefs, and roadmap milestones
   - Compare against master calendar — find new items not yet synced
   - Add missing items to master calendar
   - Update changed items (date changes, cancellations)
   - Remove past events older than 30 days (archive to keep calendar clean)
5. Sort all entries chronologically
6. Flag the next 7 days as "This Week" at the top

## Output

- Update `data/operations/master-calendar.md` (living document — edit in place)
- Update your MEMORY.md with sync notes
