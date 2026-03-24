---
name: savings-goal
user-invocable: false
description: Set up a savings goal — target amount, timeline, monthly contribution, and progress tracking.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Savings Goal Playbook

## Inputs

- $ARGUMENTS — Goal name, target amount, deadline, and any constraints
- `data/personal/finance/` — Existing savings goals and budget data

## Steps

1. Read existing savings goals from `data/personal/finance/` to understand current commitments
2. Define the goal with all required fields:
   - **Name** — clear, descriptive goal name
   - **Target Amount** — total amount needed
   - **Deadline** — target completion date
   - **Monthly Contribution Needed** — calculated from target and timeline
   - **Current Progress** — starting balance toward this goal
   - **Priority** — high / medium / low relative to other goals
3. Check if the monthly contribution is realistic given the current budget
4. If not realistic, suggest adjustments:
   - Extend the timeline
   - Reduce the target
   - Identify budget categories to cut
   - Combine with other goals
5. Set check-in reminders — monthly review milestones with expected progress markers

## Output

- Write the goal to `data/personal/finance/savings-goal-[name].md`
- Update your MEMORY.md with the new goal and how it fits the overall savings picture
