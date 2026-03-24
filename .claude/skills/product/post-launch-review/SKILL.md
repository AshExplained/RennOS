---
name: post-launch-review
user-invocable: false
description: Post-launch analysis — results vs targets, what worked, what didn't, and learnings for next launch.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Post-Launch Review Playbook

## Inputs

- $ARGUMENTS — Product name, launch results data
- `data/product/launch-plan-*.md` — Launch plan
- `data/analytics/kpi-dashboard.md` — Performance metrics
- `data/product/` — Product data

## Steps

1. Read launch plan, KPI dashboard, and any available results data
2. Analyze results vs targets:
   - Revenue vs target
   - Units sold / signups vs target
   - Email metrics (open, click, conversion)
   - Social engagement during launch
   - PR coverage achieved
   - Traffic to landing page / sales page
3. Assess each launch phase:
   - Pre-launch: did teaser content build enough anticipation?
   - Launch week: did the multi-channel push work?
   - Post-launch: did follow-up sustain momentum?
4. What worked — with evidence
5. What didn't work — with honest assessment
6. Learnings for next launch — specific, actionable improvements
7. Compare to @quality-assurance post-mortem if one exists

## Output

- Write to `data/product/post-launch-review-[product]-[date].md`
- Update your MEMORY.md with launch learnings
