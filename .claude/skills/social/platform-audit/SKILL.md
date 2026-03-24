---
name: platform-audit
user-invocable: false
description: Audit presence and performance on a specific platform — profile, content quality, engagement, growth.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Platform Audit Playbook

## Inputs

- $ARGUMENTS — Platform name and profile URL/handle
- `data/brand/brand-dna.md` — Brand identity for alignment check
- `data/strategy/audience-personas.md` — Target audience for audience alignment check

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for platform audit methodology and benchmarks
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Apply the audit dimensions and benchmarks from the reference
4. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
5. Research the profile on the specified platform via web
6. Audit across dimensions:
   - **Profile quality** — Bio, avatar, banner, links, consistency with brand
   - **Content quality** — Recent posts, formats used, voice alignment
   - **Engagement metrics** — Likes, comments, shares, saves relative to follower count
   - **Growth trajectory** — Follower trend, engagement trend
   - **Audience alignment** — Are the followers the right people?
   - **Posting consistency** — Frequency, cadence, gaps
7. Score each dimension 1-10 with specific evidence
8. Identify top 3 strengths and top 3 improvement areas
9. Provide actionable recommendations with priority order

## Output

- Write to `data/social/audit-[platform]-[date].md`
- Update your MEMORY.md with audit findings and benchmarks
