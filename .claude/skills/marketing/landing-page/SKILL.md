---
name: landing-page
user-invocable: false
description: Write landing page copy and structure — headline, subhead, sections, social proof, and CTA.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Landing Page Playbook

## Inputs

- $ARGUMENTS — Offer, target audience, funnel stage
- `data/brand/brand-dna.md` — Brand identity and voice
- `data/strategy/audience-personas.md` — Audience pain points

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for landing page methodology
2. Apply the copywriting frameworks and conversion principles from the reference
3. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
4. Research high-converting landing page patterns via web
5. Write the landing page structure:
   - **Hero section** — Headline (benefit-driven), subheadline, primary CTA
   - **Problem section** — Agitate the pain point
   - **Solution section** — Present the offer as the solution
   - **Features/benefits** — What they get (features → benefits translation)
   - **Social proof** — Testimonials, logos, numbers, case studies
   - **FAQ** — Address common objections
   - **Final CTA** — Urgency, summary of value, clear action
6. Write all copy in brand voice
7. Include notes for visual layout direction
8. Provide A/B test suggestions (headline variants, CTA variants)

## Output

- Write to `data/marketing/landing-page-[offer]-[date].md`
- Update your MEMORY.md with landing page patterns and conversion insights
