---
name: monetization-plan
user-invocable: false
description: Create a monetization plan for a specific asset — audience, content, IP, or expertise.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Monetization Plan Playbook

## Inputs

- $ARGUMENTS — Asset to monetize, target audience, constraints
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments
- `data/content/top-performers.md` — Top-performing content

## Steps

1. Read brand DNA, audience personas, and top-performing content
2. Research monetization approaches for this type of asset via web
3. Design the monetization plan:
   - **Asset** — What exactly is being monetized
   - **Target customer** — Which persona segment (and their willingness to pay)
   - **Product format** — How to package the asset (course, template, membership, etc.)
   - **Pricing** — Recommended price point with justification
   - **Launch strategy** — How to bring it to market (timeline, channels, launch sequence)
   - **Revenue projection** — Conservative, realistic, optimistic estimates
   - **Costs** — Production costs, ongoing costs, tools needed
   - **Break-even** — When does this become profitable?
4. Identify existing content/IP that accelerates production (don't build from scratch)
5. Define validation steps before full production

## Output

- Write to `data/finance/monetization-plan-[asset]-[date].md`
- Update your MEMORY.md with monetization patterns
