---
name: market-validation
user-invocable: false
description: Validate product-market fit before building — demand testing, competitor analysis, and willingness-to-pay assessment.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Market Validation Playbook

## Inputs

- $ARGUMENTS — Product concept to validate
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments
- `data/strategy/competitive-landscape.md` — Competitor data

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for market validation methodology
2. Apply the validation frameworks and testing methods from the reference
3. Read brand DNA, audience personas, and competitive landscape
4. Research the market via web:
   - Who else offers this? How well does it sell?
   - What's the market size for this type of product?
   - What do reviews say about competitor products? (gaps = opportunity)
5. Assess demand signals:
   - **Content engagement** — Do related topics perform well?
   - **Direct requests** — Have people asked for this?
   - **Search volume** — Are people searching for this?
   - **Competitor validation** — Do competitors sell this successfully?
   - **Audience fit** — Does the target persona actually want/need this?
6. Assess willingness to pay:
   - What do alternatives cost?
   - What's the persona's price sensitivity?
   - What transformation/outcome justifies the price?
7. Validation verdict: STRONG FIT / NEEDS MORE TESTING / WEAK FIT
8. If STRONG: recommend next steps (MVP scope, pre-sale test, waitlist)
9. If WEAK: explain why and suggest pivots

## Output

- Write to `data/product/market-validation-[product]-[date].md`
- Update your MEMORY.md with validation patterns
