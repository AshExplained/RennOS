---
name: article
user-invocable: false
description: Write a long-form article or essay — in-depth, well-researched, authority-building.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Article Playbook

## Inputs

- $ARGUMENTS — Topic, thesis, or brief
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles
- `data/strategy/competitive-landscape.md` — Competitive context for positioning

## Steps

1. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and `data/strategy/competitive-landscape.md` for positioning context
2. Research the topic thoroughly via web — data, studies, expert opinions, counterarguments
3. Define a clear thesis/angle that differentiates from existing coverage
4. Outline: introduction (hook + thesis) → body sections (evidence, examples, analysis) → conclusion (synthesis + next steps)
5. Write the full draft with citations/references where appropriate
6. Self-review for depth, accuracy, and brand voice

## Output

- Write the draft to `data/content/drafts/article-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
