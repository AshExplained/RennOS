---
name: testimonial-request
user-invocable: false
description: Draft testimonial or review request outreach — timed for when customers are happiest.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Testimonial Request Playbook

## Inputs

- $ARGUMENTS — Customer name/segment, product, trigger moment
- `data/brand/brand-dna.md` — Core brand identity
- `data/customers/` — Customer data

## Steps

1. Read brand DNA and customer data
2. Identify the best moment to ask (after a milestone, positive feedback, or success):
   - Just completed a course module
   - Just had a support interaction resolved positively
   - Just hit a personal goal using the product
   - After 30/60/90 days of active use
3. Draft the request:
   - Personal and warm — acknowledge their specific achievement
   - Make it easy — provide specific prompts ("What was your biggest takeaway?")
   - Offer format options (written quote, video, social post, case study interview)
   - No pressure — frame it as "if you're willing"
4. Provide 2 variants (email and DM)
5. Suggest where to use the testimonial once collected (website, social, landing page, pitch deck)

## Output

- Write to `data/customers/testimonial-request-[date].md`
- **Reminder:** All outreach is DRAFTS. the user sends them manually.
- Update your MEMORY.md with testimonial collection patterns
