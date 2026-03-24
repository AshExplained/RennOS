---
name: workout-plan
user-invocable: false
description: Create or update a workout plan based on fitness goals, schedule, and available equipment.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Workout Plan Playbook

## Inputs

- $ARGUMENTS — Goals, schedule, equipment, experience level
- `data/personal/health/` — Existing fitness data
- `.claude/ceo-memory/user_profile.md` — Health goals from onboarding

## Steps

1. Read `references/best-practices.md` for exercise programming principles (FITT, progressive overload, periodization), training splits, workout structure, volume guidelines, and deload protocols
2. Read the user's health profile and existing workout data
3. Design the workout plan:
   - **Goal** — Strength, cardio, flexibility, weight loss, general fitness
   - **Schedule** — Days per week, time per session, preferred times
   - **Split** — Full body, upper/lower, push/pull/legs, or custom
   - **For each workout day:**
     - Exercises (name, sets, reps or duration, rest period)
     - Warm-up and cool-down
     - Progression plan (when to increase weight/reps)
   - **Rest days** — Active recovery suggestions
4. Account for available equipment and experience level
5. Include progressive overload plan (how to advance over 4-8 weeks)
6. Note when to deload and when to reassess

## Output

- Write to `data/personal/health/workout-plan-[date].md`
- Update your MEMORY.md with workout patterns
