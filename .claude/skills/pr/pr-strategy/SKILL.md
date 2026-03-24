---
name: pr-strategy
user-invocable: false
description: Develop an overall PR strategy — positioning narrative, target media, key story themes, and communication approach.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# PR Strategy Playbook

## Inputs

- $ARGUMENTS — Goals, time period, any specific focus
- `data/brand/brand-dna.md` — Brand identity
- `data/strategy/quarterly-roadmap.md` — Strategic direction
- `data/strategy/audience-personas.md` — Target audience
- `data/strategy/competitive-landscape.md` — Competitive positioning

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read brand DNA, roadmap, personas, and competitive landscape
3. Research current media landscape via web:
   - What narratives are trending in the industry?
   - What are journalists covering?
   - What story angles have legs right now?
4. Define the PR strategy:
   - **Positioning narrative** — The overarching story about the user and the brand
   - **Key themes** (3-5) — Story themes to push consistently
   - **Target media tiers** — Tier 1 (major press), Tier 2 (trade/niche), Tier 3 (blogs/podcasts)
   - **Target outlets** per tier — Specific publications/shows to pursue
   - **Communication approach** — Tone, frequency, proactive vs. reactive balance
5. Align with quarterly roadmap milestones — what PR moments map to planned launches/campaigns?
6. Identify PR opportunities: speaking engagements, awards, guest features, thought leadership

## Output

- Write to `data/pr/pr-strategy-[period].md`
- Update your MEMORY.md with media landscape trends and strategic direction
