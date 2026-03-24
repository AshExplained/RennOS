---
name: opportunity-brief
user-invocable: false
description: Package a trending topic into an actionable brief — what it is, why it matters, how the user can jump in, and suggested timeline.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Opportunity Brief Playbook

## Inputs

- $ARGUMENTS — Trend or topic to brief
- `data/brand/brand-dna.md` — Brand context
- `data/strategy/audience-personas.md` — Audience context

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for opportunity assessment methodology
2. Apply the timeliness and evaluation frameworks from the reference
3. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
4. Research the trend/topic in depth via web:
   - What's driving it?
   - Who's participating?
   - What's the current conversation?
   - What angles are already covered?
5. Assess brand fit:
   - Does this align with the user's positioning?
   - Can the user add a unique perspective?
   - Is there a risk of looking inauthentic?
6. Identify a unique angle — what can the user say that no one else is saying?
7. Propose content formats:
   - Which format(s) would work best for this opportunity?
   - Which platforms should it be published on?
8. Define timeline and urgency:
   - How quickly does the user need to act?
   - What's the shelf life of this opportunity?
9. Define success metrics — how will we know this worked?

## Output

- Write to `data/strategy/opportunity-briefs/[topic]-brief.md` (use lowercase, hyphenated topic name)
- Update your MEMORY.md with key findings
