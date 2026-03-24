---
name: fitness-review
user-invocable: false
description: Review fitness progress and adjust the plan — what's working, what needs to change.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Fitness Review Playbook

## Inputs

- $ARGUMENTS — Progress notes, any metrics
- `data/personal/health/` — Workout plan, exercise logs

## Steps

1. Read current workout plan and exercise logs
2. Assess progress:
   - Are workouts being completed consistently?
   - Is progressive overload happening? (weights/reps increasing)
   - Any pain, injury, or fatigue patterns?
   - Energy levels and recovery quality
3. Recommend adjustments:
   - Exercises to swap (boredom, plateau, equipment change)
   - Volume or intensity changes
   - Schedule adjustments based on lifestyle
4. Set goals for next review period

## Output

- Write to `data/personal/health/fitness-review-[date].md`
- Update your MEMORY.md with progress patterns
