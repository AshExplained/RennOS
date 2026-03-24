---
name: rate-card
user-invocable: false
description: Create or update the user's rate card — standard pricing for sponsorships, consulting, speaking, and other services.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Rate Card Playbook

## Inputs

- $ARGUMENTS — "create" or "update", any new services/rates
- `data/brand/brand-dna.md` — Core brand identity
- `data/finance/rate-card.md` — Current rate card
- `data/analytics/kpi-dashboard.md` — Audience metrics that justify rates

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read brand DNA, existing rate card, and KPI dashboard (audience metrics justify rates)
3. Research market rates via web for each service category
4. Structure the rate card:
   - **Sponsorships** — Packages/tiers (social post, dedicated video, multi-platform bundle), each with deliverables + price
   - **Consulting/Coaching** — Hourly rate, day rate, retainer options
   - **Speaking** — Keynote, panel, workshop, virtual event rates
   - **Content creation** — Guest posts, collaborations, UGC
   - **Licensing** — Content licensing, IP licensing rates
5. For each rate: price, what's included, typical client, minimum commitment
6. Include audience metrics that justify the rates (followers, engagement, reach, demographics)
7. Add effective date and review schedule (quarterly recommended)

## Output

- Update `data/finance/rate-card.md` (living document — overwrite on update)
- Update your MEMORY.md with rate card decisions
