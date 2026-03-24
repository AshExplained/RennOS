---
name: optimal-timing
user-invocable: false
description: Analyze and recommend best posting times per platform based on audience behavior and engagement data.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Optimal Timing Playbook

## Inputs

- $ARGUMENTS — Platform (or "all platforms") and any available engagement data
- `data/strategy/audience-personas.md` — Audience behavior patterns
- `data/analytics/kpi-dashboard.md` — Engagement metrics (when available)
- `data/content/top-performers.md` — Top performing content timing patterns (when available)

## Steps

1. Read `data/strategy/audience-personas.md` (where does the audience hang out, when are they active?)
2. Read any available engagement/analytics data
3. Read top performers for timing patterns
4. For each platform, recommend:
   - Best days of the week to post
   - Best times of day
   - Worst times to avoid
   - Reasoning based on audience behavior
5. If engagement data exists, cross-reference recommendations with actual performance
6. Provide a weekly posting schedule template

## Output

- Write to `data/social/optimal-timing-[date].md`
- Update your MEMORY.md with timing insights and what works
