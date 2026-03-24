---
name: gap-analysis
user-invocable: false
description: Identify gaps competitors are missing that the user can own — cross-references competitive landscape with audience needs.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Gap Analysis Playbook

## Inputs

- $ARGUMENTS — Specific area to analyze or "general" for a broad scan
- `data/strategy/competitive-landscape.md` — Competitive context
- `data/strategy/audience-personas.md` — Audience needs
- `data/brand/brand-dna.md` — Brand positioning

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for gap analysis methodology
2. Apply the scoring rubric from the reference when evaluating gaps
3. Read `data/brand/brand-dna.md`, `data/strategy/competitive-landscape.md`, and `data/strategy/audience-personas.md`
4. Cross-reference the competitive landscape with audience needs:
   - What does the audience want that competitors aren't providing?
   - What topics are under-covered?
   - What formats are missing?
   - What platforms are underserved?
5. Identify unaddressed pain points from persona data
6. For each gap found, assess:
   - **Opportunity size** — How many people would this serve?
   - **Brand fit** — Does this align with the user's positioning?
   - **Difficulty** — How hard would it be to fill this gap?
   - **Urgency** — Is there a time-sensitive window?
7. Rank gaps by combined opportunity score (size × fit × feasibility)
8. Provide specific recommendations for the top 3-5 gaps

## Output

- Write to `data/strategy/gap-analysis-[date].md` (use today's date in YYYY-MM-DD format)
- Update your MEMORY.md with key findings
