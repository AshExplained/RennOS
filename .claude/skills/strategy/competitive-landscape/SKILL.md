---
name: competitive-landscape
user-invocable: false
description: Map the broader competitive landscape — positioning matrix, clusters, white space, and strategic opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Competitive Landscape Playbook

## Inputs

- $ARGUMENTS — Industry/niche and optional list of competitors to include
- `data/brand/brand-dna.md` — Brand context
- Existing profiles in `data/strategy/competitors/` (if any)

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for competitive analysis methodology
2. Apply the frameworks from the reference when analyzing the competitive landscape
3. Read `data/brand/brand-dna.md` for brand context
4. Read any existing competitor profiles in `data/strategy/competitors/`
5. Research 5-10 key competitors/peers in the space via web
6. Map competitors on a positioning matrix:
   - X-axis and Y-axis defined by the most relevant differentiators for this space
   - Place each competitor and the user on the matrix
7. Identify clusters and categories of competitors
8. Identify white space — positioning areas no one is claiming
9. Compare content strategies across competitors:
   - Platforms used
   - Content formats
   - Posting frequency
   - Audience engagement levels
10. Summarize key takeaways and strategic implications for the user

## Output

- Write to `data/strategy/competitive-landscape.md`
- Update your MEMORY.md with key findings
