---
name: seo-optimize
user-invocable: false
description: Optimize a piece of content for search — rewrite elements, add keywords, improve structure for ranking.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# SEO Optimize Playbook

## Inputs

- $ARGUMENTS — Path to content, target keywords
- `data/brand/brand-dna.md` — Brand identity and voice
- Relevant keyword research from `data/marketing/`

## Steps

1. Read `data/brand/brand-dna.md` and the content to optimize
2. Read relevant keyword research from `data/marketing/`
3. Research SERP competitors for the target keywords
4. Optimize the content:
   - Rewrite title for keyword + click-through
   - Rewrite meta description
   - Restructure headers for keyword targeting and readability
   - Add/adjust keyword usage naturally throughout
   - Add internal link suggestions
   - Add FAQ section targeting question-based keywords
   - Suggest image alt text
5. Preserve brand voice — SEO optimization must not make content robotic
6. Track changes made (before/after for each element)

## Output

- Write optimized content to `data/content/drafts/[name]-seo-optimized.md` (or edit in place if instructed)
- Update your MEMORY.md with optimization patterns and what changes had impact
