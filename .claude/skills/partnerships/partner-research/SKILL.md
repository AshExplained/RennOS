---
name: partner-research
user-invocable: false
description: Research and identify potential collaboration partners — brands, creators, companies with audience overlap and brand fit.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Partner Research Playbook

## Inputs

- $ARGUMENTS — Industry/niche, partnership type, specific criteria
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Target audience
- `data/strategy/competitive-landscape.md` — Competitive context

## Steps

1. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and `data/strategy/competitive-landscape.md`
2. Research potential partners via web:
   - Brands, creators, companies in the same or adjacent space
   - Who has an audience that overlaps with the user's target?
   - Who shares brand values and tone?
   - Who is at a complementary stage (not a direct competitor)?
3. For each potential partner, assess:
   - Audience size and overlap with the user's audience
   - Brand fit (1-10) — do their values align?
   - Reach and influence in the space
   - What mutual value could a partnership create?
   - Any risks (brand misalignment, controversy, competition)
4. Prioritize partners by fit × reach × mutual value
5. Recommend top 5 partners with rationale

## Output

- Write to `data/partnerships/partner-research-[niche]-[date].md`
- Update your MEMORY.md with research patterns and findings
