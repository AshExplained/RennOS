---
name: upsell-plan
user-invocable: false
description: Identify and plan upsell/cross-sell opportunities — how to increase customer lifetime value.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Upsell Plan Playbook

## Inputs

- $ARGUMENTS — Product, customer segment
- `data/brand/brand-dna.md` — Core brand identity
- `data/product/product-roadmap.md` — Product roadmap
- `data/customers/` — Customer data
- `data/strategy/audience-personas.md` — Audience segments

## Steps

1. Read brand DNA, product roadmap, customer data, and audience personas
2. Identify upsell/cross-sell opportunities:
   - **Upsell:** Higher tier of same product (basic → premium)
   - **Cross-sell:** Complementary products (course buyers → community, community → coaching)
   - **Expansion:** Add-ons, advanced modules, bonus content
3. For each opportunity:
   - Target customer segment (who's most likely to buy?)
   - Trigger moment (when are they most receptive?)
   - Offer and pricing
   - Messaging approach (value-first, not pushy)
   - Expected conversion rate and revenue impact
4. Design the upsell journey (when to introduce, how to pitch, follow-up)
5. Keep it genuinely valuable — upsells should solve a real need, not extract money

## Output

- Write to `data/customers/upsell-plan-[product]-[date].md`
- Update your MEMORY.md with upsell patterns
