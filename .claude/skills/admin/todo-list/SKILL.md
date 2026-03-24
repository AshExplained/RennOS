---
name: todo-list
user-invocable: false
description: Create or update personal to-do list — tasks, priorities, and due dates.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# To-Do List Playbook

## Inputs

- $ARGUMENTS — Tasks to add, tasks to update, or "review" for daily planning
- `data/personal/admin/todo-list.md` — Existing to-do list (if any)

## Steps

1. Read existing to-do list from `data/personal/admin/todo-list.md` if it exists
2. If adding tasks:
   - Add each task with priority (P0-P3), due date, and category
   - Use Edit (append) — do NOT overwrite existing entries
3. If updating tasks:
   - Mark tasks as done, change priority, or reschedule due dates
4. If reviewing:
   - List all open tasks grouped by priority
   - Flag overdue tasks (due date passed, not done)
   - Suggest today's focus tasks based on priority and due dates
5. Maintain clean, scannable format throughout

## Output

- Update `data/personal/admin/todo-list.md` (living document — use Edit to append/update, Write to create first time)
- Update your MEMORY.md with task patterns and priorities
