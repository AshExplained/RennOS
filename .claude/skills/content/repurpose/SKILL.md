---
name: repurpose
user-invocable: false
description: Take one content piece and transform it into multiple formats for different platforms.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Repurpose Playbook

## Inputs

- $ARGUMENTS — Path to source content, target formats/platforms
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Read the source content thoroughly
3. Identify the core insights/value (what's the essence that translates across formats?)
4. For each target format, create a derivative:
   - Blog → Thread: extract key points, rewrite for thread format
   - Blog → Social posts: pull 3-5 standalone insights as individual posts
   - Blog → Carousel: distill into visual slide structure
   - Blog → Newsletter section: summarize with personal angle
   - Video script → Blog: expand spoken content into written form
   - (adapt based on $ARGUMENTS)
5. Ensure each derivative stands alone (doesn't require reading the original)
6. Adapt voice/tone for each platform while staying on-brand

## Output

- Write multiple files to `data/content/drafts/` named `repurposed-[format]-[source-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
