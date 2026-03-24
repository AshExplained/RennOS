---
name: email-template
user-invocable: false
description: Design an email template layout — structure, components, visual direction, and mobile responsiveness.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Email Template Playbook

## Inputs

- $ARGUMENTS — Email type (newsletter/campaign/transactional/welcome), brand context
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system
- `data/brand/style-guide.md` — Style guide

## Steps

1. Read brand DNA, visual identity, and style guide
2. Design the email template:
   - **Header** — Logo placement, navigation links (if any), preheader
   - **Hero section** — Featured image/graphic area, headline treatment
   - **Body sections** — Content blocks, text styling, image-text layout
   - **CTA buttons** — Style, color, sizing, placement
   - **Dividers/spacing** — Section separators, padding
   - **Footer** — Unsubscribe link, social links, contact info, legal text
3. For each section: layout direction, component specs, spacing, color usage
4. Mobile responsiveness notes:
   - Single-column stacking rules
   - Minimum touch target sizes (44px)
   - Font size adjustments for mobile
   - Image scaling behavior
5. Note email client compatibility considerations (Outlook, Gmail, Apple Mail)

## Output

- Write to `data/design/email-template-[type]-[date].md`
- Update your MEMORY.md with email template patterns
