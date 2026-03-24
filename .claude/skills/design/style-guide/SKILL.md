---
name: style-guide
user-invocable: false
description: Create a visual style guide for consistency across all platforms — the practical implementation of visual identity.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Style Guide Playbook

## Inputs

- $ARGUMENTS — "create" or "update"
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system
- `data/brand/style-guide.md` — Current style guide

## Steps

1. Read brand DNA, visual identity, and existing style guide
2. Research style guide best practices via web
3. Create or update the style guide:
   - **Logo usage** — Placement, sizing, clear space, what not to do
   - **Color application** — When to use each color (backgrounds, text, buttons, accents)
   - **Typography application** — Heading styles, body styles, caption styles, link styles
   - **Button styles** — Primary, secondary, ghost — with states (default, hover, active, disabled)
   - **Card/component styles** — Standard patterns for content cards, testimonials, CTAs
   - **Image treatment** — Crop ratios, overlay styles, border radius
   - **Social media templates** — Standard sizes and layouts per platform
   - **Email template** — Standard email layout components
4. Include platform-specific guidelines (Instagram grid, LinkedIn banner, YouTube thumbnail)
5. Keep it practical — designers should be able to follow this without interpretation

## Output

- Update `data/brand/style-guide.md` (living document — overwrite on update)
- Update your MEMORY.md with style guide decisions
