---
name: partner-brief
user-invocable: false
description: Create a brief on a specific potential partner — audience overlap, brand fit, reach, content style, and partnership potential.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Partner Brief Playbook

## Inputs

- $ARGUMENTS — Partner name/URL/handle
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Target audience

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
3. Research the potential partner via web:
   - Who they are, what they do, their positioning
   - Audience demographics and size per platform
   - Content style, tone, and frequency
   - Monetization model
   - Past partnerships/collaborations they've done
4. Assess partnership fit:
   - Audience overlap (high/medium/low)
   - Brand alignment (1-10)
   - Reach and influence
   - Potential partnership formats (co-creation, cross-promotion, joint product, event, etc.)
   - Risks and concerns
5. Recommend whether to pursue and suggested approach

## Output

- Write to `data/partnerships/partner-brief-[partner-name]-[date].md`
- Update your MEMORY.md with partner assessment details
