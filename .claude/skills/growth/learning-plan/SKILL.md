---
name: learning-plan
user-invocable: false
description: Create a structured learning plan with milestones — what to learn, how, and by when.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Learning Plan Playbook

## Inputs

- $ARGUMENTS — Skill to learn, target level, and timeline (if specified)
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `vault/personal/goals/` — the user's personal goals and vision
- `data/personal/growth/` — Existing learning plans and skill assessments

## Steps

1. Read the user's profile (`data/brand/brand-dna.md`, `vault/personal/`) to understand context and motivations
2. Read existing learning plans and skill assessments in `data/personal/growth/` to avoid duplication
3. Design the learning plan with full structure:
   - **Skill:** What exactly is being learned
   - **Current level:** Where the user is right now (beginner/intermediate/advanced/expert)
   - **Target level:** Where the user wants to be, with specific outcomes
   - **Timeline:** Start date, end date, total duration
   - **Milestones:** 4-8 milestones with clear success criteria and target dates
   - **Daily/weekly commitment:** How much time per day/week, and when
   - **Resources:** Courses, books, tutorials, practice platforms (top recommendations)
   - **Practice method:** How to apply the skill (projects, exercises, real-world use)
4. Schedule study time — note recommendations for @schedule-manager to block learning sessions
5. Set accountability check-ins — define weekly or biweekly review points to assess progress

## Output

- Write the learning plan to `data/personal/growth/learning-plan-[skill]-[date].md`
- Update your MEMORY.md with the new plan created and key details
