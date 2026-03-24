---
name: nutrition-review
user-invocable: false
description: Review diet and suggest improvements — are nutrition goals being met?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Nutrition Review Playbook

## Inputs

- $ARGUMENTS — What the user has been eating, any concerns
- `data/personal/health/` — Meal plan, fitness data

## Steps

1. Read current meal plan and fitness data
2. Assess current diet:
   - Are macro targets being met?
   - Enough protein for training goals?
   - Hydration adequate?
   - Any nutritional gaps (vitamins, minerals, fiber)?
   - Meal timing aligned with workout schedule?
3. Suggest improvements — specific, practical, not overwhelming
4. Flag any concerns worth discussing with a nutritionist

## Output

- Write to `data/personal/health/nutrition-review-[date].md`
- Update your MEMORY.md with diet patterns
