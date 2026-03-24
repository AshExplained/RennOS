---
name: sprint-review
user-invocable: false
description: Sprint review — what was completed, what wasn't, demo results, and velocity tracking.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Sprint Review Playbook

## Inputs

- $ARGUMENTS — Product name, sprint number
- `data/tech/sprint-plan-[product]-sprint-[N]-*.md` — Sprint plan for this sprint
- Asana task statuses for all sprint stories
- `data/tech/code-review-PR-*.md` — Code review records from this sprint
- Previous sprint reviews for velocity trend data

## Steps

1. Read the sprint plan to get the sprint goal, committed stories, and estimates
2. Check Asana task statuses for each story — Done, In Progress, or Not Started
3. Compile completed stories:
   - Story name and description
   - PR link(s) associated with each
   - Story points delivered
4. Compile incomplete stories:
   - Story name
   - Why it wasn't completed (blocked, underestimated, scope creep, etc.)
   - Current status and remaining work
5. Evaluate sprint goal: Was it met? Partially met? Not met?
6. Calculate velocity:
   - Committed story points
   - Completed story points
   - Velocity trend over last 3-5 sprints (if historical data exists)
7. Document blockers encountered during the sprint
8. Present results summary to the CEO agent for relay to the user
9. Move incomplete stories back to the top of the backlog for next sprint prioritization

## Output

- Write to `data/tech/sprint-review-[product]-sprint-[N]-[date].md` with: sprint goal assessment, completed stories with PR links, incomplete stories with reasons, velocity (committed vs completed), blockers, backlog updates
- Update your MEMORY.md with velocity data and any patterns observed
