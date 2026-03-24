---
name: stack-review
user-invocable: false
description: Review the current tech stack — what tools are in use, costs, overlaps, and optimization opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Stack Review Playbook

## Inputs

- $ARGUMENTS — Scope of review (full stack, specific category, or cost-focused)
- Existing tool inventory or budget docs if available

## Steps

1. Read existing tool inventory, budget documents, and previous stack reviews from `data/tech/`
2. Map the full stack by category:
   - Category (e.g., CMS, analytics, email, hosting, design, automation)
   - Tool name and plan/tier
   - Monthly/annual cost
   - Usage level (daily / weekly / rarely)
   - Key integrations with other stack tools
3. Identify overlaps — multiple tools doing the same job
4. Identify gaps — needs not covered by any current tool
5. Research alternatives via WebSearch for any overlap or underperforming tools
6. For each tool, recommend: **KEEP** / **CONSOLIDATE** / **REPLACE** / **ADD** with reasoning
7. Calculate potential cost savings from consolidations and replacements
8. Flag any tools with upcoming renewals or contract deadlines

## Output

- Write the review to `data/tech/stack-review-[date].md` with: full stack map, cost breakdown, overlap analysis, gap analysis, recommendations per tool, total potential savings
- Update your MEMORY.md with key findings and patterns discovered
