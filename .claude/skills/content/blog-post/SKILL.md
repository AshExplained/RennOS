---
name: blog-post
user-invocable: false
description: Draft a blog post from a topic, brief, or outline. Research-backed, brand-aligned, audience-aware.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Blog Post Playbook

## Inputs

- $ARGUMENTS — Topic, brief, or outline for the blog post
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Research the topic via web if needed (stats, examples, quotes)
5. Outline the post: hook → problem → insight → actionable takeaway → CTA
6. Write the full draft in brand voice
7. Include suggested meta title, meta description, and tags
8. Self-review against brand voice before saving

## Output

- Write the draft to `data/content/drafts/blog-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
