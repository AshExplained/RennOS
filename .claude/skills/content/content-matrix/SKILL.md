---
name: content-matrix
user-invocable: false
description: Map out all derivative content from a single source piece. Plan the full content multiplication strategy.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Content Matrix Playbook

## Inputs

- $ARGUMENTS — Source content or topic
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/content/content-matrix.md` — Existing repurposing map (note: this is the data file, not this skill)
- `data/strategy/audience-personas.md` — Target audience profiles

## Current State
!`ls -1 data/content/drafts/ 2>/dev/null | grep -v '.gitkeep'`

## Steps

1. Run `python3 -m scripts.content.scan_content_inventory` to gather current data
2. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
3. Read existing `data/content/content-matrix.md` for patterns
4. Analyze the source content for repurpose potential
5. Map all possible derivatives:
   | Source Format | Derivative Format | Platform | Effort | Priority |
   |---|---|---|---|---|
6. For each derivative, estimate:
   - Effort level (low/medium/high)
   - Expected impact
   - Priority (now/soon/later)
7. Identify the optimal repurposing sequence (what to create first for maximum compounding)

## Output

- Update `data/content/content-matrix.md` with new entries
- Update your MEMORY.md with key findings and patterns discovered
