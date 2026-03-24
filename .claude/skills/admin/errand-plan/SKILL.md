---
name: errand-plan
user-invocable: false
description: Plan and prioritize errands for the day or week — route optimization and batching.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Errand Plan Playbook

## Inputs

- $ARGUMENTS — List of errands, time window, or "plan today/this week"
- `data/personal/admin/todo-list.md` — Existing to-do list (errand items)

## Steps

1. Read to-do list from `data/personal/admin/todo-list.md` and extract errand-type tasks
2. Group errands by location/area for efficient batching
3. Prioritize by urgency and deadline
4. Estimate time required for each errand (including travel)
5. Suggest optimal route to minimize backtracking
6. Identify errands that can be done online instead of in-person
7. Fit all errands into the available time window

## Output

- Write to `data/personal/admin/errand-plan-[date].md`
- Update your MEMORY.md with errand patterns and preferences
