---
name: wireframe
user-invocable: false
description: Create wireframe specs for a page or feature — layout, components, hierarchy, and interaction notes.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Wireframe Playbook

## Inputs

- $ARGUMENTS — Page/feature, purpose, key content
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system
- `data/product/product-spec-*.md` — Product spec

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read brand DNA, visual identity, and product spec
3. Research layout patterns via web for this type of page
4. Create the wireframe spec:
   - **Page purpose** — What this page should accomplish
   - **Layout structure** — Sections from top to bottom with hierarchy
   - For each section:
     - **Component type** — Hero, nav, text block, form, CTA, testimonial, FAQ, footer
     - **Content** — What goes here (headline, body, image, button)
     - **Visual weight** — Primary, secondary, or supporting
     - **Interaction** — Click, scroll, hover, expand, submit
   - **Responsive notes** — How layout changes on mobile vs desktop
   - **Accessibility** — ARIA labels, contrast, keyboard navigation notes
5. Prioritize above-the-fold content — most important info first
6. Note which components are reusable across pages

## Output

- Write to `data/design/wireframe-[page]-[date].md`
- Update your MEMORY.md with wireframe patterns
