---
name: feedback-report
user-invocable: false
description: Compile customer feedback into a report for Product (Dept 12) — themes, quotes, and recommended actions.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Feedback Report Playbook

## Inputs

- $ARGUMENTS — Product, time period, feedback sources
- `data/customers/` — Surveys, support responses, testimonials, churn insights
- `data/product/feedback-themes.md` — Existing feedback themes

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read all available customer feedback data and existing feedback themes
3. Compile feedback:
   - **Volume** — How much feedback collected in the period
   - **Sentiment** — Overall positive/negative/neutral breakdown
   - **Top themes** — Most frequently mentioned topics
   - **Representative quotes** — Best quotes per theme (positive and negative)
   - **Feature requests** — Ranked by frequency
   - **Bugs/issues** — Ranked by severity
   - **Churn signals** — What feedback suggests people might leave
4. Compare to previous period — are things getting better or worse?
5. Recommended actions: top 3 things Product should do based on this feedback
6. Route report to @product-feedback-analyst (Dept 12) for the product improvement loop

## Output

- Write to `data/customers/feedback-report-[product]-[date].md`
- Update your MEMORY.md with feedback compilation patterns
