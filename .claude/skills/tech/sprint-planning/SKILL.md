---
name: sprint-planning
user-invocable: false
description: Plan a sprint — pull from backlog, estimate effort, assign to dev team agents, set sprint goal.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Sprint Planning Playbook

## Inputs

- $ARGUMENTS — Product name, sprint number, and any priority overrides
- `data/tech/product-spec-[product].md` — Product specification
- `data/tech/backlog-[product].md` — Product backlog (prioritized)
- `data/tech/sprint-review-[product]-sprint-[N-1]-*.md` — Previous sprint review (for velocity reference)
- Team capacity and availability constraints if provided

## Steps

1. Read the product spec to understand the product context and goals
2. Read the backlog to see all available stories, ordered by priority
3. Read the previous sprint review to extract velocity data (committed vs completed story points)
4. Calculate team capacity for the upcoming sprint based on available developers and sprint duration
5. Select stories from the top of the backlog that fit within capacity, accounting for:
   - Priority (product owner's ordering)
   - Dependencies between stories (pull prerequisites first)
   - Team skill distribution (balance frontend/backend/infra work)
6. For each selected story, define:
   - Acceptance criteria (clear, testable)
   - Effort estimate (story points)
   - Assignment to dev team agent (@full-stack-developer, @ux-designer, etc.)
   - Dependencies (blocked by / blocks)
7. Write the sprint goal — one sentence that captures what this sprint delivers
8. Set sprint start and end dates (typically 2-week cadence)
9. Validate: committed points should not exceed average velocity by more than 10%
10. Create Asana tasks for each story with acceptance criteria, estimate, and assignee

**Note:** Asana tasks are created for each story so the team can track progress in real time.

## Output

- Write to `data/tech/sprint-plan-[product]-sprint-[N]-[date].md` with: sprint goal, selected stories (with acceptance criteria, effort, assignment, dependencies), capacity vs committed summary, start/end dates
- Update your MEMORY.md with sprint goal, committed velocity, and any planning decisions made
