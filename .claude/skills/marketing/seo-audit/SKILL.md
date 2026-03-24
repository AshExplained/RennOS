---
name: seo-audit
user-invocable: false
description: Audit content or site pages for SEO improvements — on-page, structure, and optimization opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# SEO Audit Playbook

## Inputs

- $ARGUMENTS — URL or content path to audit
- `data/brand/brand-dna.md` — Brand identity

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for SEO audit methodology and checklists
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Apply the audit checklists and benchmarks from the reference
4. Read the content to audit
5. Research current SERP for the target keywords via web
6. Audit on-page SEO elements:
   - Title tag (length, keyword placement, click-worthiness)
   - Meta description (compelling, keyword-included, correct length)
   - Header structure (H1, H2, H3 hierarchy)
   - Keyword usage (natural placement, density, LSI keywords)
   - Internal/external links
   - Image alt text
   - URL structure
   - Content length vs. competitors
7. Assess content quality for SEO:
   - Does it satisfy search intent?
   - Is it more comprehensive than competing pages?
   - Does it have unique value (original data, perspective, examples)?
8. Score each element and provide specific fix recommendations

## Output

- Write to `data/marketing/seo-audit-[page]-[date].md`
- Update your MEMORY.md with SEO patterns and common issues found
