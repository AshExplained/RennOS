---
name: improvement-plan
user-invocable: false
description: Turn feedback into a prioritized improvement plan — what to fix, what to add, what to cut.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Improvement Plan Playbook

## Inputs

- $ARGUMENTS — Product name, focus area or "general"
- `data/product/feedback-themes.md` — Cumulative feedback themes
- `data/product/product-roadmap.md` — Product roadmap
- `data/product/feedback-synthesis-*.md` — Latest feedback synthesis

## Steps

1. Read feedback themes, product roadmap, and latest feedback synthesis
2. Prioritize improvements:
   - For each feedback theme: impact (how many users affected) × severity × effort to fix
3. Create the improvement plan:
   - **Critical fixes** (do now) — Bugs, broken features, major UX issues
   - **High-impact improvements** (do next) — Frequently requested, high effort-to-impact ratio
   - **Nice-to-have enhancements** (do later) — Good ideas, lower priority
   - **Won't do** (with explanation) — Requests that don't align with product direction
4. For each improvement: what, why, effort estimate, expected impact, assigned to (which dept/agent)
5. Align with product roadmap — slot improvements into the timeline
6. Feed high-priority items into @product-designer for design iteration

## Output

- Write to `data/product/improvement-plan-[product]-[date].md`
- Update your MEMORY.md with improvement patterns
