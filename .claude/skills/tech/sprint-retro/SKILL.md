---
name: sprint-retro
user-invocable: false
description: Sprint retrospective — what worked, what didn't, and specific improvements for next sprint.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Sprint Retrospective Playbook

## Inputs

- $ARGUMENTS — Product name, sprint number
- `data/tech/sprint-review-[product]-sprint-[N]-*.md` — Sprint review for this sprint
- `data/tech/sprint-retro-[product]-sprint-[N-1]-*.md` — Previous retro (to track improvement progress)

## Steps

1. Read the sprint review to understand what happened — velocity, blockers, completed/incomplete work
2. Read the previous retro to check whether past improvements were actually implemented
3. Run the retrospective analysis:

   **What went well:**
   - Processes, tools, or practices that helped the team deliver
   - Positive patterns to reinforce and continue

   **What didn't go well:**
   - Bottlenecks, miscommunications, or process failures
   - Stories that slipped and the root causes
   - Blockers that could have been prevented

   **What to try next sprint:**
   - Specific, actionable improvements (not vague goals)
   - Each improvement must have:
     - **Owner** — who is responsible for driving it
     - **Measurement** — how we know it worked
   - Limit to 2-3 improvements to keep focus

4. Keep the tone blameless — focus on process and systems, not individuals
5. Review improvement trends across sprints — are we actually getting better?
6. Flag any systemic issues that need escalation to the CEO agent/user

## Output

- Write to `data/tech/sprint-retro-[product]-sprint-[N]-[date].md` with: what went well, what didn't, improvements with owners and measurements, progress on past improvements, systemic issues
- Update your MEMORY.md with recurring themes and improvement trajectory
