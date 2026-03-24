---
name: feedback-survey
user-invocable: false
description: Design a customer feedback survey — questions, format, and distribution strategy.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Feedback Survey Playbook

## Inputs

- $ARGUMENTS — Product, survey goal (NPS/satisfaction/feature feedback/churn exit)
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/` — Product context
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read brand DNA, product context, and audience personas
2. Design the survey based on goal:
   - **NPS survey:** "How likely are you to recommend [product]?" + open-ended follow-up
   - **Satisfaction survey:** Rate experience across dimensions + improvement suggestions
   - **Feature feedback:** Rank priority of potential features + open-ended wishes
   - **Churn exit survey:** Why are you leaving? What would bring you back?
3. Survey design rules:
   - Keep it short — max 5-7 questions (completion rate drops after that)
   - Mix question types (rating, multiple choice, open-ended)
   - Start easy, end with the important open-ended question
   - Mobile-friendly format
4. Define distribution strategy: when to send, who to send to, follow-up for non-responders
5. Define what to do with results → route to @product-feedback-analyst (Dept 12)

## Output

- Write to `data/customers/feedback-survey-[product]-[date].md`
- Update your MEMORY.md with survey design patterns
