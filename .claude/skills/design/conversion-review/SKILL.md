---
name: conversion-review
user-invocable: false
description: Review a landing page for conversion optimization — layout, visual hierarchy, CTA effectiveness, and friction.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Conversion Review Playbook

## Inputs

- $ARGUMENTS — URL or page description
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for conversion optimization methodology
2. Apply Cialdini's principles and the CRO checklist from the reference
3. Read brand DNA and visual identity
4. Research conversion optimization best practices via web
5. Review the page for conversion:
   - **Above the fold** — Is the value proposition + CTA visible without scrolling?
   - **Visual hierarchy** — Does the eye flow naturally to the CTA?
   - **CTA design** — Is the button prominent? Contrasting color? Clear text?
   - **Social proof placement** — Is it near the CTA? Is it credible?
   - **Friction points** — Long forms, unclear pricing, missing trust signals
   - **Distractions** — Navigation links, competing CTAs, unnecessary content
   - **Mobile experience** — Does the layout work on small screens?
   - **Loading perceived speed** — Does the page feel fast?
6. For each issue: what's wrong, impact on conversion (high/medium/low), recommended fix
7. Score conversion potential: 1-10 with breakdown
8. Provide 3 highest-impact changes to make

## Output

- Write to `data/design/conversion-review-[page]-[date].md`
- Update your MEMORY.md with conversion patterns
