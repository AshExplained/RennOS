---
name: user-flow
user-invocable: false
description: Design a user flow for a product or page — step-by-step journey from entry to goal completion.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# User Flow Playbook

## Inputs

- $ARGUMENTS — Product/page, user goal, entry point
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/product-spec-*.md` — Product spec
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read brand DNA, product spec, and audience personas
2. Research UX flow patterns via web for this type of product/page
3. Define the user flow:
   - **Entry point** — How does the user arrive? (landing page, link, search, referral)
   - **Steps to goal** — Each step the user takes, in order
   - **Decision points** — Where users make choices (sign up, skip, upgrade, exit)
   - **Happy path** — The ideal journey from entry to goal
   - **Alternative paths** — Common deviations and where they lead
   - **Error states** — What happens when something goes wrong
   - **Exit points** — Where users might leave (and why)
4. For each step: what the user sees, what action they take, what happens next
5. Identify friction points — steps that are confusing, unnecessary, or slow
6. Recommend simplifications — fewer steps to goal = higher conversion

## Output

- Write to `data/design/user-flow-[product]-[date].md`
- Update your MEMORY.md with flow patterns
