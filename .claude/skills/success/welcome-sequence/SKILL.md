---
name: welcome-sequence
user-invocable: false
description: Create a welcome email/message sequence for new customers — the first touchpoints after purchase.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Welcome Sequence Playbook

## Inputs

- $ARGUMENTS — Product name, customer type, sequence length
- `data/brand/brand-dna.md` — Core brand identity
- `data/customers/onboarding-design-*.md` — Onboarding design
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read brand DNA, onboarding design, and audience personas
2. Design the welcome sequence (typically 5-7 messages over 14 days):
   - **Email 1 (immediate):** Welcome + access instructions + quick win guide
   - **Email 2 (day 1-2):** Key feature/module to try first + success story
   - **Email 3 (day 3-5):** Check-in — any questions? + helpful resource
   - **Email 4 (day 7):** Milestone check — have you hit [activation point]?
   - **Email 5 (day 10):** Deeper value — advanced tip or hidden feature
   - **Email 6 (day 14):** Community invitation / next steps / upsell nudge
3. For each email: subject line (3 variants), preview text, body copy, CTA
4. Tone: warm, helpful, personal — not corporate onboarding
5. Include behavioral triggers — if customer hasn't activated by day 3, send a nudge
6. Hand off to @email-marketing-manager (Dept 5) for implementation

## Output

- Write to `data/customers/welcome-sequence-[product]-[date].md`
- **Reminder:** All emails are DRAFTS for the user to review.
- Update your MEMORY.md with welcome sequence patterns
