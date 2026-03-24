---
name: carousel
user-invocable: false
description: Design slide-by-slide carousel content — text, layout direction, and visual notes for each slide.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Carousel Playbook

## Inputs

- $ARGUMENTS — Topic, platform, number of slides
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/brand/visual-identity.md` — Visual brand guidelines

## Steps

1. Read `data/brand/brand-dna.md` and `data/brand/visual-identity.md`
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Define carousel arc: hook slide → educational/value slides → CTA slide
4. For each slide, specify:
   - Headline text
   - Body text (if any)
   - Visual direction (layout, imagery, icons)
   - Color/style notes aligned with visual identity
5. Keep text concise — carousels are visual-first
6. Ensure the first slide stops the scroll (strong hook)
7. Last slide has clear CTA (follow, save, share, link)

## Output

- Write the carousel brief to `data/content/drafts/carousel-[platform]-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
