---
name: content-recommendations
user-invocable: false
description: Recommend content types, topics, and formats based on performance data — what should we create more of?
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Content Recommendations Playbook

## Inputs

- $ARGUMENTS — Focus area or "general"
- `data/content/top-performers.md` — Top content data
- `data/analytics/` — Content performance analyses
- `data/strategy/audience-personas.md` — Audience context
- `data/strategy/quarterly-roadmap.md` — Strategic direction

## Steps

1. Read top performers, content analyses, audience personas, and roadmap
2. Cross-reference what performs well with what the audience wants and what the roadmap prioritizes
3. Generate recommendations:
   - **Do more of:** Formats/topics/tones that consistently work
   - **Stop doing:** Formats/topics that consistently underperform
   - **Experiment with:** Untested formats/topics that data suggests could work
   - **Repurpose:** High performers that haven't been repurposed yet
   - **Optimize:** Medium performers that could be improved
4. For each recommendation: what, why (data evidence), expected impact, effort level
5. Prioritize by expected impact × low effort

## Output

- Write to `data/analytics/content-recommendations-[date].md`
- Update your MEMORY.md with recommendation patterns
