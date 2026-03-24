---
name: onboarding-design
user-invocable: false
description: Design an onboarding flow for a product — first-use experience, activation milestones, and time-to-value optimization.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Onboarding Design Playbook

## Inputs

- $ARGUMENTS — Product name, product type
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/` — Product spec, course design
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read brand DNA, product spec, and audience personas
3. Design the onboarding flow:
   - **Welcome moment** — First impression (email, in-app, message)
   - **Quick win** — What can the customer achieve in the first 5 minutes?
   - **Activation milestone** — The "aha moment" that makes the product click
   - **Day 1 experience** — Step-by-step first-day journey
   - **Week 1 milestones** — Key actions/progress markers for the first week
   - **Day 30 checkpoint** — Where should the customer be after a month?
4. For each stage: what happens, what the customer sees/receives, what action they take
5. Identify friction points — where might customers drop off?
6. Define success metrics: activation rate, time-to-first-value, day-7 retention, day-30 retention
7. Note handoffs to @email-marketing-manager for automated welcome sequences

## Output

- Write to `data/customers/onboarding-design-[product]-[date].md`
- Update your MEMORY.md with onboarding patterns
