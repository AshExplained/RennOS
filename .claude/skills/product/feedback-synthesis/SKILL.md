---
name: feedback-synthesis
user-invocable: false
description: Collect and synthesize customer feedback into themes — what users love, what frustrates them, what they want next.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Feedback Synthesis Playbook

## Inputs

- $ARGUMENTS — Product name, feedback sources (surveys, reviews, support tickets, social comments)
- `data/product/feedback-themes.md` — Cumulative feedback themes
- `data/customers/` — Testimonials, churn insights

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read existing feedback themes and customer data
3. Analyze all provided feedback:
   - Categorize by sentiment (positive, negative, neutral)
   - Group by theme (feature request, bug, UX issue, pricing, content quality, etc.)
   - Count frequency per theme (how many people mention this?)
   - Extract representative quotes per theme
4. Synthesize into a feedback report:
   - **Top loves** — What users value most (keep doing this)
   - **Top frustrations** — What causes the most friction (fix these)
   - **Top requests** — What users want next (build these)
   - **Surprise insights** — Unexpected feedback that changes perspective
5. Update `data/product/feedback-themes.md` with cumulative theme data
6. Flag critical issues that need immediate attention

## Output

- Write to `data/product/feedback-synthesis-[product]-[date].md`
- Update `data/product/feedback-themes.md` (Edit append — cumulative)
- Update your MEMORY.md with feedback patterns
