---
name: pricing-analysis
user-invocable: false
description: Analyze and recommend pricing for a product, service, or offering — competitive research, value assessment, and recommended price point.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Pricing Analysis Playbook

## Inputs

- $ARGUMENTS — Product/service to price, target audience, competitor examples
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments
- `data/strategy/competitive-landscape.md` — Competitor data
- `data/finance/rate-card.md` — Current rates

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for pricing methodology
2. Apply the pricing frameworks and psychology principles from the reference
3. Read brand DNA, audience personas, competitive landscape, and current rate card
4. Research competitive pricing via web:
   - What do competitors charge for similar offerings?
   - What's the market range (budget → premium)?
   - What pricing models are common? (one-time, subscription, tiered, pay-what-you-want)
5. Assess value factors:
   - What transformation/outcome does the buyer get?
   - How does this compare to alternatives?
   - What's the audience's willingness to pay? (based on persona income, pain severity)
6. Recommend pricing:
   - **Recommended price** — With justification
   - **Pricing model** — One-time vs subscription vs tiered, and why
   - **Tier structure** — If tiered, what goes in each tier
   - **Anchoring strategy** — How to frame the price (vs alternatives, vs value delivered)
   - **Launch pricing** — Any introductory discounts or early-bird pricing?
7. Sensitivity analysis — what happens to conversions if price is 20% higher or lower?

## Output

- Write to `data/finance/pricing-analysis-[product]-[date].md`
- Update your MEMORY.md with pricing patterns
