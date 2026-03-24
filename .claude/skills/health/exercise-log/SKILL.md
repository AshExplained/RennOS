---
name: exercise-log
user-invocable: false
description: Log and track workouts — exercises, sets, reps, weights, and notes.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Exercise Log Playbook

## Inputs

- $ARGUMENTS — Workout details to log
- `data/personal/health/` — Existing exercise log

## Steps

1. Read existing exercise log from `data/personal/health/`
2. Add today's workout entry:
   - Date
   - Workout type (push, pull, legs, cardio, etc.)
   - For each exercise: name, sets × reps, weight, notes (felt easy/hard, pain, PR)
   - Duration
   - Overall energy/mood rating (1-5)
3. Use Edit (append) — do NOT overwrite existing entries
4. Flag personal records (PRs)

## Output

- Update `data/personal/health/exercise-log.md` (living document — Edit append)
- Update your MEMORY.md with PR tracking
