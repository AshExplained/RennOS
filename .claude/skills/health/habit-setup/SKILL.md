---
name: habit-setup
user-invocable: false
description: Define and set up a new habit to track — clear trigger, action, frequency, and success criteria.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Habit Setup Playbook

## Inputs

- $ARGUMENTS — Habit to build, goal, motivation
- `data/personal/health/` — Existing habits

## Steps

1. Read existing habits being tracked
2. Define the new habit:
   - **Habit** — Clear, specific action (not vague)
   - **Trigger** — When/where does this happen? (after coffee, before bed, at gym)
   - **Frequency** — Daily, specific days, weekly
   - **Duration** — How long to track before review (21 days, 30 days, 66 days)
   - **Success criteria** — What counts as "done"?
   - **Minimum viable version** — The smallest version on bad days (1 pushup vs full workout)
3. Add to habit tracker with starting date
4. Suggest a reward/accountability mechanism

## Output

- Update `data/personal/health/habit-tracker.md` (Edit append to add new habit)
- Update your MEMORY.md with habit setup patterns
