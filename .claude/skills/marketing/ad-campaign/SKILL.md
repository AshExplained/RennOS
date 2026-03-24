---
name: ad-campaign
user-invocable: false
description: Design a paid ad campaign — targeting, budget allocation, creative brief, and funnel structure.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Ad Campaign Playbook

## Inputs

- $ARGUMENTS — Campaign goal, budget, platforms, timeline
- `data/brand/brand-dna.md` — Brand identity
- `data/strategy/audience-personas.md` — Audience profiles
- `data/analytics/kpi-dashboard.md` — Performance data (when available)
- `data/content/top-performers.md` — Top organic content to amplify

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read brand DNA, personas, and available analytics/performance data
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Research platform targeting options and competitor ad strategies via web
5. Design the campaign:
   - **Objective** — Awareness, traffic, leads, conversions
   - **Platforms** — Which platforms and why
   - **Targeting** — Audiences, interests, lookalikes, retargeting
   - **Budget allocation** — How to split across platforms and ad sets
   - **Creative brief** — What visuals/copy are needed (reference existing content to amplify)
   - **Funnel** — Where do clicks go? (landing page, content, offer)
6. Define campaign timeline (launch, optimization windows, end date)
7. Define KPIs and success criteria
8. Recommend content to amplify (top organic performers)

## Output

- Write to `data/marketing/ad-campaign-[name]-[date].md`
- Reminder: All campaigns are DRAFTS. the user approves budget and launches manually.
- Update your MEMORY.md with campaign patterns and platform performance insights
