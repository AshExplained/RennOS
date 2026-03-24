---
name: onboarding-audit
user-invocable: false
description: Audit existing onboarding for drop-off points — where are new customers getting stuck or leaving?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Onboarding Audit Playbook

## Inputs

- $ARGUMENTS — Product name, any drop-off data or customer feedback
- `data/customers/` — Customer data, existing onboarding designs
- `data/product/feedback-themes.md` — Feedback themes
- `data/analytics/kpi-dashboard.md` — Performance metrics

## Steps

1. Read existing onboarding design, customer feedback, and available analytics
2. Analyze the current onboarding experience:
   - Where do customers drop off? (registration → first use → activation → retention)
   - How long does it take to reach the "aha moment"?
   - What questions do new customers ask most? (from support data)
   - What feedback do they give about the onboarding? (from surveys/reviews)
3. Identify friction points:
   - Confusing steps
   - Too many steps before value
   - Missing guidance
   - Technical issues
4. Score current onboarding: activation rate, time-to-value, day-7 retention
5. Recommend specific improvements, prioritized by impact

## Output

- Write to `data/customers/onboarding-audit-[product]-[date].md`
- Update your MEMORY.md with onboarding friction patterns
