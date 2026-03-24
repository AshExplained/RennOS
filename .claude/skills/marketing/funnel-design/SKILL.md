---
name: funnel-design
user-invocable: false
description: Design a conversion funnel — from lead magnet through nurture to offer. Maps the full journey from stranger to customer.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Funnel Design Playbook

## Inputs

- $ARGUMENTS — Offer/product, target audience, goal
- `data/brand/brand-dna.md` — Brand identity
- `data/strategy/audience-personas.md` — Audience pain points and desires
- `data/strategy/quarterly-roadmap.md` — Strategic direction

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for funnel methodology and benchmarks
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and roadmap
4. Research conversion funnel patterns and benchmarks via web
5. Design the full funnel:
   - **Top of funnel (TOFU)** — How people discover (SEO, social, ads, referrals)
   - **Lead magnet** — What free value captures their email
   - **Nurture sequence** — Email sequence that builds trust and educates
   - **Middle of funnel (MOFU)** — Webinar, case study, demo, or deeper content
   - **Bottom of funnel (BOFU)** — The offer, sales page, checkout
   - **Post-purchase** — Onboarding, upsell, referral loop
6. For each stage, specify:
   - Content/asset needed
   - Conversion metric to track
   - Expected conversion rate (benchmark)
   - Department/agent responsible
7. Identify bottleneck risks and mitigation strategies

## Output

- Write to `data/marketing/funnel-design-[name]-[date].md`
- Update your MEMORY.md with funnel patterns and conversion benchmarks
