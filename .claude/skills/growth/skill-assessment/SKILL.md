---
name: skill-assessment
user-invocable: false
description: Assess current skill level and define a target — where you are vs where you want to be.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Skill Assessment Playbook

## Inputs

- $ARGUMENTS — Skill to assess, and any self-reported context from the user
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/personal/growth/` — Existing assessments and learning plans

## Steps

1. Read existing skill data in `data/personal/growth/` — past assessments, learning plans, milestone checks
2. Assess current level on a clear scale:
   - **Beginner** — Foundational understanding, limited practical experience
   - **Intermediate** — Can apply the skill independently in common scenarios
   - **Advanced** — Deep knowledge, can handle complex/novel situations
   - **Expert** — Mastery, can teach others and innovate in the domain
3. Define evidence for the current level — what specifically demonstrates this level? What can the user do now?
4. Define the target level with specific outcomes — not just "advanced" but what "advanced" looks like in practice (concrete things the user would be able to do)
5. Identify the gap — what specific knowledge, practice, or experience is missing between current and target
6. Estimate timeline — realistic timeframe to close the gap, given typical learning curves and the user's available time

## Output

- Write the assessment to `data/personal/growth/skill-assessment-[skill]-[date].md`
- Update your MEMORY.md with assessment results and identified gaps
