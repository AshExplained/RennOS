---
name: habit-review
user-invocable: false
description: Review habit streaks and accountability — what's sticking, what's slipping, and how to adjust.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Habit Review Playbook

## Inputs

- $ARGUMENTS — Review period, specific habits, or "all"
- `data/personal/health/habit-tracker.md` — Habit tracking data

## Steps

1. Read habit tracker data
2. For each habit:
   - Current streak length
   - Completion rate (% of target days completed)
   - Trend (improving, stable, declining)
   - Longest streak achieved
3. Identify:
   - **Strong habits** — Consistent, well-established
   - **Struggling habits** — Low completion, breaking streaks
   - **New habits** — Too early to judge
4. For struggling habits: suggest adjustments (make smaller, change trigger, change time)
5. Celebrate wins — acknowledge consistency

## Output

- Write to `data/personal/health/habit-review-[date].md`
- Update your MEMORY.md with habit patterns
