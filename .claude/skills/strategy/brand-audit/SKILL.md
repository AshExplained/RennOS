---
name: brand-audit
user-invocable: false
description: Analyze current brand presence across platforms and identify gaps between intended and actual brand positioning.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Brand Audit Playbook

## Inputs

- $ARGUMENTS — Profiles, links, or platforms to audit
- `data/brand/brand-dna.md` — Current brand identity and positioning

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for audit methodology and scoring rubric
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read `data/brand/brand-dna.md` to understand intended brand positioning
4. Scan the provided profiles/links via web search and fetch
5. Score the brand across 8 dimensions:
   - Voice consistency
   - Visual identity
   - Messaging clarity
   - Audience alignment
   - Platform presence
   - Content quality
   - Engagement quality
   - Differentiation
6. For each dimension, rate 1-10 with specific evidence
7. Identify gaps between intended positioning (from Brand DNA) and actual presence
8. Provide specific, actionable recommendations for each gap

## Output

- Write the full audit report to `data/brand/latest-audit.md`
- Update your MEMORY.md with key findings and patterns discovered
