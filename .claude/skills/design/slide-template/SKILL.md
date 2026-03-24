---
name: slide-template
user-invocable: false
description: Create reusable slide templates — standard layouts for common slide types that can be used across presentations.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Slide Template Playbook

## Inputs

- $ARGUMENTS — Template types needed, or "full set"
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system

## Steps

1. Read brand DNA and visual identity
2. Design reusable slide templates:
   - **Title slide** — For opening slides (logo, title, subtitle, date)
   - **Section divider** — For transitioning between topics (bold text, brand color background)
   - **Content + image** — Text on one side, image on the other
   - **Key stat** — Large number/stat with supporting context
   - **Quote slide** — Featured quote with attribution
   - **Comparison** — Two-column or table layout for comparing options
   - **Process/timeline** — Steps or chronological flow
   - **Team/about** — Photo + bio layout
   - **CTA/closing** — Call to action with contact info
3. For each template: layout description, component placement, color usage, typography, spacing
4. Ensure all templates follow the visual identity system
5. Note which templates are essential (use always) vs optional (use when needed)

## Output

- Write to `data/design/slide-templates-[date].md`
- Update your MEMORY.md with slide template patterns
