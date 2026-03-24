---
name: ad-copy
user-invocable: false
description: Write ad copy for a specific platform — headline, body, CTA, tailored to platform and audience.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Ad Copy Playbook

## Inputs

- $ARGUMENTS — Platform, offer/product, target audience, ad format
- `data/brand/brand-dna.md` — Brand identity and voice
- `data/strategy/audience-personas.md` — Audience profiles

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Research ad best practices for the target platform via web
3. Write ad copy variants (minimum 3 per element):
   - **Headlines** (3-5 variants) — Short, punchy, benefit-driven
   - **Body copy** (2-3 variants) — Problem → solution → proof → CTA
   - **CTA text** (2-3 variants) — Action-oriented, specific
4. Adapt to platform specs:
   - Google Ads: character limits per field, keyword insertion
   - Meta/Instagram: visual-first, casual tone, social proof
   - LinkedIn: professional, value-driven, industry-specific
5. Include targeting notes (audience, interests, demographics)
6. Suggest A/B test variations

## Output

- Write to `data/marketing/ad-copy-[platform]-[offer]-[date].md`
- Update your MEMORY.md with ad copy patterns and platform-specific insights
