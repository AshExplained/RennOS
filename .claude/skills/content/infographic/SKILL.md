---
name: infographic
user-invocable: false
description: Structure an infographic — data points, layout flow, copy, and visual direction.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Infographic Playbook

## Inputs

- $ARGUMENTS — Topic, data/stats to include
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/brand/visual-identity.md` — Visual brand guidelines

## Steps

1. Read `data/brand/brand-dna.md` and `data/brand/visual-identity.md`
2. Define the infographic story arc (what insight should the viewer walk away with?)
3. Structure sections top-to-bottom:
   - Title / headline
   - Key stat or hook
   - Supporting data points (3-5)
   - Comparison or progression
   - Conclusion / CTA
4. For each section, specify:
   - Copy text
   - Data visualization type (bar chart, pie, icon array, timeline, etc.)
   - Layout direction and visual notes
5. Keep copy scannable — infographics are glanced, not read

## Output

- Write the infographic brief to `data/content/drafts/infographic-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
