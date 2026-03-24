---
name: keyword-research
user-invocable: false
description: Research and recommend target keywords for content — search volume, difficulty, intent, and opportunity.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Keyword Research Playbook

## Inputs

- $ARGUMENTS — Topic/niche, content type, target audience
- `data/brand/brand-dna.md` — Brand identity and positioning
- `data/strategy/audience-personas.md` — Audience behavior and search intent

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for keyword research methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Apply the intent classification and clustering frameworks from the reference
4. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
5. Research keywords via web:
   - Primary keywords (high intent, direct relevance)
   - Long-tail keywords (lower competition, specific intent)
   - Question-based keywords (what the audience is asking)
   - Competitor keywords (what competitors rank for)
6. For each keyword, assess:
   - Estimated search volume
   - Competition/difficulty (low/medium/high)
   - Search intent (informational, navigational, transactional)
   - Brand fit and relevance
7. Group keywords into clusters by topic/intent
8. Prioritize by opportunity score (volume × relevance ÷ difficulty)
9. Recommend content pieces to target top keyword clusters

## Output

- Write to `data/marketing/keyword-research-[topic]-[date].md`
- Update your MEMORY.md with keyword patterns and search intent insights
