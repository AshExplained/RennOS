---
name: social-post
user-invocable: false
description: Craft a single platform post — optimized for the target platform's format, tone, and audience expectations.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Social Post Playbook

## Inputs

- $ARGUMENTS — Topic, platform, and any specific angle
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles
- `data/content/top-performers.md` — Patterns that work

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Read `data/content/top-performers.md` for patterns that work
3. Identify the platform (LinkedIn, X, Instagram, etc.) and adapt format accordingly
4. Write the post: hook line → value/insight → CTA or conversation starter
5. Provide 3 variants with different angles or hooks
6. Suggest relevant hashtags if platform-appropriate

## Output

- Write the draft to `data/content/drafts/post-[platform]-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
