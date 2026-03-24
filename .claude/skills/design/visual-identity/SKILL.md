---
name: visual-identity
user-invocable: false
description: Define or update the brand visual system — colors, typography, imagery style, spacing, and design principles.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Visual Identity Playbook

## Inputs

- $ARGUMENTS — "create" or "update", any specific direction
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Current visual identity

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for visual identity methodology
2. Apply the color theory, typography, and spacing frameworks from the reference
3. Read brand DNA and existing visual identity
4. Research visual design trends and competitor visual identities via web
5. Define or update the visual system:
   - **Color palette** — Primary, secondary, accent, neutral colors with hex codes. Include usage rules (when to use each)
   - **Typography** — Heading font, body font, sizes, weights, line heights. Include font pairing rationale
   - **Imagery style** — Photography style, illustration style, icon style. What feels on-brand vs off-brand
   - **Spacing system** — Base unit, margin/padding scale, layout grid
   - **Design principles** — 3-5 guiding principles (e.g., "clean over cluttered", "bold over safe")
   - **Do's and don'ts** — Visual examples of on-brand vs off-brand
6. Ensure visual identity aligns with brand DNA voice (e.g., playful brand = vibrant colors, serious brand = muted palette)
7. Include platform-specific adaptations if needed

## Output

- Update `data/brand/visual-identity.md` (living document — overwrite on update)
- Update your MEMORY.md with visual identity decisions
