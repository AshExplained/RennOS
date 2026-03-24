---
name: milestone-check
user-invocable: false
description: Check progress against skill milestones — are you on track?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Milestone Check Playbook

## Inputs

- $ARGUMENTS — Specific skill to check, or "all" for a full dashboard
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/personal/growth/` — Learning plans, skill assessments, past milestone checks

## Steps

1. Read all learning plans and skill assessments in `data/personal/growth/`
2. For each active skill being learned, evaluate:
   - **Current milestone:** Where the user is right now
   - **Expected milestone:** Where the user should be based on the plan's timeline
   - **Status:** On track / Ahead / Behind
   - **Evidence:** What demonstrates the current milestone has (or hasn't) been reached
   - **Blockers:** Anything preventing progress (time, resources, motivation, unclear path)
3. Build an overall progress dashboard — all skills at a glance with status indicators
4. Celebrate wins — explicitly call out progress, completed milestones, and momentum
5. Recommend adjustments for skills that are behind:
   - Revise timeline?
   - Change approach or resources?
   - Increase/decrease commitment?
   - Reprioritize across skills?

## Output

- Write the milestone check to `data/personal/growth/milestone-check-[date].md`
- Update your MEMORY.md with current progress snapshot and any concerns
