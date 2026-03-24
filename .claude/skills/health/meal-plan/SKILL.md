---
name: meal-plan
user-invocable: false
description: Create a meal plan based on goals — nutrition targets, preferences, and schedule.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Meal Plan Playbook

## Inputs

- $ARGUMENTS — Goals, dietary preferences, restrictions, budget
- `data/personal/health/` — Existing health data
- `.claude/ceo-memory/user_profile.md` — Health goals

## Steps

1. Read `references/best-practices.md` for nutrition frameworks (TDEE calculation, macros by goal), meal timing, dietary guidelines, meal structure templates, and meal prep strategies
2. Read the user's health profile, fitness goals, and any dietary preferences
3. Research meal ideas and nutrition facts via web
4. Design the meal plan:
   - **Duration** — Weekly plan with daily breakdown
   - **Macro targets** — Protein, carbs, fats aligned with fitness goals
   - **For each day:** Breakfast, lunch, dinner, snacks
   - **For each meal:** What to eat, approximate macros, prep time
   - **Meal prep tips** — Batch cooking suggestions for efficiency
   - **Shopping list** — Consolidated ingredients for the week
5. Accommodate dietary restrictions (vegetarian, allergies, preferences)
6. Keep it practical — the user needs to actually cook and eat this

## Output

- Write to `data/personal/health/meal-plan-[date].md`
- Update your MEMORY.md with meal preferences
