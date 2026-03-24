---
name: budget-plan
user-invocable: false
description: Create a budget plan aligned with revenue goals — how to allocate money across departments and initiatives.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Budget Plan Playbook

## Inputs

- $ARGUMENTS — Budget period, total budget, priorities
- `data/finance/revenue-dashboard.md` — Current revenue
- `data/finance/forecast-*.md` — Latest forecast
- `data/operations/budget-tracker.md` — Current spending
- `data/strategy/quarterly-roadmap.md` — Planned initiatives

## Steps

1. Read revenue dashboard, latest forecast, current spending, and roadmap
2. Define budget allocation:
   - **Tools & platforms** — Software, hosting, subscriptions
   - **Paid advertising** — Ad spend budget per platform
   - **Content production** — Freelancers, design, video production
   - **Events & travel** — Conference attendance, speaking engagements
   - **Product development** — Course creation, community platform costs
   - **Legal & professional** — Attorney, accountant, insurance
   - **Reserve** — Emergency fund / buffer (recommend 10-15% of budget)
3. Align spending with roadmap priorities — fund what matters most
4. Compare against current spending in budget tracker — where are we over/under?
5. Set spending limits per category with trigger points for review
6. Define monthly budget review cadence

## Output

- Write to `data/finance/budget-plan-[period].md`
- Update your MEMORY.md with budget allocation patterns
