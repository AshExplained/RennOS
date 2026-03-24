---
name: task-tracker
user-invocable: false
description: Create or update task lists and track progress across departments — what's done, in progress, and blocked.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Task Tracker Playbook

## Inputs

- $ARGUMENTS — New tasks to add, tasks to update, or "review" for status check
- `.claude/ceo-memory/active_projects.md` — Current project status
- `data/operations/` — Existing task tracker
- `data/strategy/quarterly-roadmap.md` — Strategic milestones

## Steps

1. Read active projects and existing task tracker from `data/operations/` if it exists
2. If adding new tasks:
   - Log each task: description, assigned department/agent, deadline, priority (P0/P1/P2/P3), status (not started/in progress/blocked/done)
   - Use Edit (append) — do NOT overwrite existing entries
3. If updating tasks:
   - Find the task entry and update status, add notes, mark completion date
4. If reviewing:
   - Scan all tasks, group by status
   - Flag overdue items (deadline passed, not done)
   - Flag blocked items with recommended unblock actions
   - Summarize: total tasks, done, in progress, blocked, overdue
5. Maintain clean, scannable table format

## Output

- Update `data/operations/task-tracker.md` (use Edit to append/update, Write to create first time)
- Update your MEMORY.md with task patterns and blockers
