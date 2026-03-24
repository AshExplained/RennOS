---
name: churn-analysis
user-invocable: false
description: Analyze churn patterns — why customers leave, early warning signals, and at-risk identification.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Churn Analysis Playbook

## Inputs

- $ARGUMENTS — Product, time period, any churn data
- `data/customers/churn-insights.md` — Cumulative churn insights
- `data/analytics/kpi-dashboard.md` — Performance metrics
- `data/product/feedback-themes.md` — Feedback themes

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read existing churn insights, KPI dashboard, and feedback themes
4. Research churn benchmarks for the product type via web
5. Analyze churn patterns:
   - **Churn rate** — What % of customers leave per period?
   - **Churn timing** — When do most customers leave? (first week, month 3, renewal?)
   - **Churn reasons** — Why do they leave? (from feedback, cancellation surveys, support data)
   - **Leading indicators** — What behavior predicts churn? (login frequency, engagement, support tickets)
   - **Segment analysis** — Which customer segments churn most/least?
6. Identify at-risk customers based on leading indicators
7. Recommend interventions per risk level:
   - Early warning → proactive outreach
   - Medium risk → special offer or engagement nudge
   - High risk → personal outreach from the user
8. Update `data/customers/churn-insights.md` with new patterns

## Output

- Write to `data/customers/churn-analysis-[date].md`
- Update `data/customers/churn-insights.md` (Edit append — cumulative)
- Update your MEMORY.md with churn patterns
