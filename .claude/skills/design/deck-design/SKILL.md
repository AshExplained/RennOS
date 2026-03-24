---
name: deck-design
user-invocable: false
description: Design a presentation or pitch deck — slide structure, content flow, visual direction, and speaker notes.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Deck Design Playbook

## Inputs

- $ARGUMENTS — Deck purpose (keynote/pitch/sponsor/workshop), topic, audience
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system
- `data/partnerships/` — Speaking pitches, sponsor pitches
- `data/pr/` — Story angles

## Steps

1. Read brand DNA, visual identity, and relevant content (speaking pitch, sponsor pitch, story angles)
2. Design the deck structure:
   - **Title slide** — Title, subtitle, the user's name/brand, visual style
   - **Agenda/overview slide** — What the audience will learn/see
   - **Content slides** (5-15 depending on length):
     - For each slide: headline, key message (1 per slide), visual direction (chart, image, quote, diagram), speaker notes
   - **Transition slides** — Between major sections
   - **CTA/closing slide** — Call to action, contact info, next steps
3. Design principles for slides:
   - One message per slide
   - Minimal text — slides support the speaker, not replace them
   - Strong visuals — every slide should have a visual element
   - Consistent layout patterns (title placement, color usage)
4. Include speaker notes for each slide — what to say, not what to show
5. Note where to use brand colors, fonts, and imagery style

## Output

- Write to `data/design/deck-design-[name]-[date].md`
- Update your MEMORY.md with deck design patterns
