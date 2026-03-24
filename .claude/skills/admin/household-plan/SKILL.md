---
name: household-plan
user-invocable: false
description: Plan household tasks and chores — weekly cleaning, organization projects, and home improvement.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Household Plan Playbook

## Inputs

- $ARGUMENTS — Tasks to plan, time period (week), or specific projects
- `data/personal/admin/maintenance-schedule.md` — Recurring maintenance tasks
- `data/personal/admin/todo-list.md` — Existing to-do list (household items)

## Steps

1. Read existing household data and to-do list from `data/personal/admin/` if available
2. Plan tasks in two categories:
   - Weekly recurring chores (cleaning, laundry, groceries, etc.)
   - One-time projects (organization, repairs, improvements)
3. Assign priority and time estimates to each task
4. Distribute tasks across the week for manageable daily loads
5. Flag tasks that require supplies to purchase or professional help to hire

## Output

- Write to `data/personal/admin/household-plan-[date].md`
- Update your MEMORY.md with household preferences and routines
