---
name: media-kit
user-invocable: false
description: Create or update the brand media kit — audience stats, reach, offerings, testimonials, and contact info.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Media Kit Playbook

## Inputs

- $ARGUMENTS — "create" or "update", any new metrics to include
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Target audience
- `data/analytics/kpi-dashboard.md` — Current metrics
- `data/content/top-performers.md` — Top content examples

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for media kit standards
2. Apply the structure and metrics guidance from the reference
3. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and available analytics
4. If updating, read existing media kit from `data/partnerships/media-kit.md`
5. Research current platform metrics via web if needed (follower counts, engagement rates)
6. Structure the media kit:
   - **About** — Who the user is, positioning statement, mission (from brand DNA)
   - **Audience** — Demographics, size per platform, engagement rates, psychographics
   - **Reach** — Total reach across platforms, email list size, website traffic
   - **Content** — Types of content produced, top-performing examples
   - **Offerings** — Sponsorship packages/tiers with pricing
   - **Past partners** — Logos, testimonials, case studies (if available)
   - **Contact** — How to get in touch
7. Keep it scannable — sponsors skim media kits, they don't read them
8. Include the most current metrics — stale numbers kill credibility

## Output

- Write to `data/partnerships/media-kit.md` (single living document, overwrite on update)
- Update your MEMORY.md with metrics snapshot for future comparison
