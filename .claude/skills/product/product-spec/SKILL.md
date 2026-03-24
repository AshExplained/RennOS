---
name: product-spec
user-invocable: false
description: Write a product spec/brief for any digital product — requirements, features, user stories, and success metrics.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Product Spec Playbook

## Inputs

- $ARGUMENTS — Product concept, scope
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/product-roadmap.md` — Product roadmap
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read brand DNA, product roadmap, and audience personas
3. Research similar products and UX patterns via web if needed
4. Write the product spec:
   - **Problem statement** — What problem does this solve?
   - **Solution overview** — How does this product solve it?
   - **Target user** — Who is this for? (persona reference)
   - **User stories** — "As a [user], I want to [action] so that [outcome]" (5-10 stories)
   - **Requirements** — Must-have features (MVP scope)
   - **Nice-to-haves** — Features for v2+
   - **Success metrics** — How do we know this product is working?
   - **Technical requirements** — Platform, integrations, dependencies
   - **Timeline** — Estimated milestones from design to launch
   - **Dependencies** — Which departments/agents are involved
5. Keep the spec concise and actionable — this is a building blueprint

## Output

- Write to `data/product/product-spec-[name]-[date].md`
- Update your MEMORY.md with product spec patterns
