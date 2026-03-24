---
name: campaign-roi
user-invocable: false
description: Measure ROI on a specific campaign — was it worth the investment? Costs, returns, and learnings.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Campaign ROI Playbook

## Inputs

- $ARGUMENTS — Campaign name, costs, results data
- `data/marketing/` — Campaign data
- `data/operations/budget-tracker.md` — Spend tracking
- `data/analytics/kpi-dashboard.md` — Performance metrics

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for ROI calculation methodology
2. Apply the formulas and attribution models from the reference
3. Read campaign data, budget tracker, and KPI dashboard
4. Calculate campaign costs:
   - Ad spend (if paid)
   - Tool/platform costs
   - Time investment (estimated hours × hourly value)
   - Content production costs
5. Calculate campaign returns:
   - Direct revenue generated (if trackable)
   - Leads/subscribers generated × estimated lead value
   - Engagement generated (reach, impressions, followers gained)
   - Brand value (PR mentions, partnerships triggered)
6. Calculate ROI metrics:
   - **ROAS** — Return on ad spend (revenue ÷ ad spend)
   - **CAC** — Customer acquisition cost (total cost ÷ customers acquired)
   - **Cost per lead** — Total cost ÷ leads generated
   - **Overall ROI** — (return - cost) ÷ cost × 100%
7. Compare against benchmarks and past campaigns
8. Verdict: Was this worth it? Would you do it again? What to change?

## Output

- Write to `data/analytics/campaign-roi-[campaign]-[date].md`
- Update your MEMORY.md with campaign ROI patterns
