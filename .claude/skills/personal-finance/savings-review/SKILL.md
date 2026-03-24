---
name: savings-review
user-invocable: false
description: Review progress toward savings goals — on track or falling behind?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Savings Review Playbook

## Inputs

- $ARGUMENTS — Specific goal to review, or "all" for full review
- `data/personal/finance/savings-goal-*.md` — All active savings goals

## Steps

1. Read all savings goals from `data/personal/finance/savings-goal-*.md`
2. For each goal, assess:
   - **Current balance** vs **expected balance** at this point in time
   - **Status** — on track / ahead / behind
   - **Months remaining** until deadline
   - **Monthly contribution needed** to stay on track (recalculated if behind)
3. If behind on any goal, recommend catch-up strategies:
   - Increase monthly contribution
   - Reallocate from lower-priority goals
   - Identify one-time savings opportunities
   - Adjust timeline if catch-up is unrealistic
4. Celebrate goals that are ahead of schedule — acknowledge the wins
5. Provide overall savings health summary:
   - Total across all goals vs total target
   - Number of goals on track / ahead / behind
   - Biggest risk and biggest win

## Output

- Write the review to `data/personal/finance/savings-review-[date].md`
- Update your MEMORY.md with progress snapshots and any goals needing attention
