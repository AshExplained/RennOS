---
name: hooks
user-invocable: false
description: Generate attention-grabbing opening lines and hooks for content. Batch-produce options to choose from.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Hooks Playbook

## Inputs

- $ARGUMENTS — Topic, content type, platform
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/content/top-performers.md` — Hook patterns that work

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for hook psychology and frameworks
2. Apply the hook types and platform conventions from the reference
3. Read `data/brand/brand-dna.md` and `data/content/top-performers.md` for hook patterns that work
4. Identify the content type and platform context
5. Generate 10-15 hook variants across different styles:
   - Question hooks
   - Contrarian/hot take hooks
   - Story hooks
   - Data/stat hooks
   - "How to" hooks
   - Curiosity gap hooks
6. Rate each hook 1-10 on scroll-stopping power
7. Recommend top 3 with rationale

## Output

- Write the hooks to `data/content/drafts/hooks-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
