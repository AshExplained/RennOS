---
name: learning-review
user-invocable: false
description: Review learning progress and adjust the plan — what's working, what's not, what to change.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Learning Review Playbook

## Inputs

- $ARGUMENTS — Skill to review, or "all" for a full review
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/personal/growth/` — Learning plans, assessments, and past reviews

## Steps

1. Read the learning plan for the specified skill in `data/personal/growth/`
2. Read any progress notes, milestone checks, and past reviews
3. Assess progress across key dimensions:
   - **Milestones:** Which have been hit, which are pending, which are overdue
   - **Schedule adherence:** Is the committed time actually happening?
   - **Consistency:** How regular has practice been?
4. Identify what's working — methods, resources, or habits that are producing results
5. Identify what's not working — blockers, ineffective resources, schedule conflicts, motivation gaps
6. Adjust the plan:
   - Revise timeline if needed
   - Swap out ineffective resources
   - Modify daily/weekly commitment if unrealistic
   - Add or remove milestones based on progress
7. Set next goals — define what "good" looks like for the next review period

## Output

- Write the review to `data/personal/growth/learning-review-[skill]-[date].md`
- Update your MEMORY.md with review findings and adjustments made
