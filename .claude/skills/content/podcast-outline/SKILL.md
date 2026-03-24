---
name: podcast-outline
user-invocable: false
description: Create a podcast episode outline — structure, talking points, questions, and flow.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Podcast Outline Playbook

## Inputs

- $ARGUMENTS — Topic, format (solo/interview/panel), guest info if applicable
- `data/brand/brand-dna.md` — Brand voice and positioning

## Steps

1. Read `data/brand/brand-dna.md`
2. Research the topic and guest (if interview format)
3. Define episode structure:
   - Cold open / teaser
   - Intro (topic framing, why it matters)
   - Segments (3-4 main segments with transitions)
   - Listener Q&A / engagement prompt
   - Outro / CTA
4. For each segment, write:
   - Key talking points (bullets, not full script)
   - Transition lines between segments
   - Questions (for interview format)
5. Estimate episode length

## Output

- Write the outline to `data/content/drafts/script-podcast-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
