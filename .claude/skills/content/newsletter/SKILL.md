---
name: newsletter
user-invocable: false
description: Write a newsletter edition — intro, main content, links, CTA. Conversational and value-packed.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Newsletter Playbook

## Inputs

- $ARGUMENTS — Topic/theme, key points, or content to reference
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles
- Recent content in `data/content/drafts/` — For cross-referencing

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Define the newsletter theme and key takeaway
5. Write sections: personal opener → main insight/story → actionable advice → links/resources → CTA
6. Keep tone conversational — newsletters are personal
7. Suggest subject line options (3-5 variants)

## Output

- Write the draft to `data/content/drafts/newsletter-[date-or-topic].md`
- Update your MEMORY.md with key findings and patterns discovered
