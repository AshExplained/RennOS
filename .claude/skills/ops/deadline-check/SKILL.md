---
name: deadline-check
user-invocable: false
description: Check upcoming deadlines across all departments and flag at-risk items.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Deadline Check Playbook

## Inputs

- $ARGUMENTS — Time window: "next 7 days", "next 30 days", or specific
- `data/operations/task-tracker.md` — Task tracking data
- `data/operations/master-calendar.md` — Master calendar
- `data/content/content-calendar.md` — Content schedule
- `data/pr/` — PR calendar files

## Steps

1. Run `python3 -m scripts.ops.deadline_scanner` to gather current data
2. Read task tracker, master calendar, content calendar, and PR calendar files
3. Extract all items with deadlines within the specified time window
4. Categorize:
   - **Overdue** — Deadline passed, not complete
   - **Due today** — Deadline is today
   - **Due this week** — Within 7 days
   - **Upcoming** — Within the specified window
5. For each item: task/event, deadline, assigned department/agent, status, risk level
6. Flag at-risk items — not started or behind schedule with deadline approaching
7. Recommend actions for overdue and at-risk items

## Output

- Write to `data/operations/deadline-check-[date].md`
- Update your MEMORY.md with deadline patterns
