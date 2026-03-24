---
name: sponsor-pitch
user-invocable: false
description: Create an outbound sponsorship pitch — targeting a brand the user wants to work with.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Sponsor Pitch Playbook

## Inputs

- $ARGUMENTS — Target sponsor/brand, why they're a fit
- `data/brand/brand-dna.md` — Brand positioning
- `data/partnerships/` — Media kit
- `data/strategy/audience-personas.md` — Target audience

## Steps

1. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and media kit from `data/partnerships/`
2. Research the target sponsor via web (their marketing, current sponsorships, audience)
3. Write the pitch:
   - **Hook** — Why this partnership makes sense for THEM
   - **Audience match** — Show audience overlap (demographics, interests, buying behavior)
   - **What the user offers** — Sponsorship packages/options (reference media kit tiers)
   - **Proof** — Past sponsor results, engagement metrics, testimonials
   - **Packages** — 2-3 tier options (basic, standard, premium) with pricing
   - **Next steps** — Clear CTA
4. Keep it concise and value-first — lead with what they get
5. Provide email pitch version (short) and deck-ready version (longer with sections)

## Output

- Write to `data/partnerships/sponsor-pitch-[brand]-[date].md`
- **Reminder:** Pitches are DRAFTS. the user sends them manually.
- Update your MEMORY.md with pitch approach details
