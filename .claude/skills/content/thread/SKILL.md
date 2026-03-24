---
name: thread
user-invocable: false
description: Write a multi-part thread for X, LinkedIn, or similar — structured for engagement and readability.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Thread Playbook

## Inputs

- $ARGUMENTS — Topic, key points, platform
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Define the thread structure: how many posts, what arc
3. Write the hook (post 1) — must stop the scroll
4. Write body posts — one idea per post, clear progression
5. Write the closer — summary, CTA, or invitation to engage
6. Keep each post within platform character limits
7. Provide the full thread numbered (1/N format)

## Output

- Write the draft to `data/content/drafts/thread-[platform]-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
