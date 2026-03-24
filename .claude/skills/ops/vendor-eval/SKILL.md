---
name: vendor-eval
user-invocable: false
description: Evaluate and compare vendors, tools, or services — features, pricing, integration, and recommendation.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Vendor Evaluation Playbook

## Inputs

- $ARGUMENTS — Vendor/tool name, category, or "compare [A] vs [B]"
- `data/brand/brand-dna.md` — Brand context and needs

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read brand DNA for context on needs and standards
3. Research the vendor/tool via web:
   - Features and capabilities
   - Pricing (tiers, free plan, enterprise)
   - Integration options (APIs, Zapier, native integrations)
   - Reputation (reviews, uptime, support quality)
   - Security and privacy (data handling, compliance)
4. If comparing multiple vendors:
   - Create comparison table across all dimensions
   - Identify clear winner per dimension
   - Weight dimensions by importance to the user's needs
5. Provide recommendation:
   - **Best overall** — Considering all factors
   - **Best value** — Best for the budget
   - **Best for growth** — Scales with the user's business
6. Include migration/setup effort estimate

## Output

- Write to `data/operations/vendor-eval-[tool-or-category]-[date].md`
- Update your MEMORY.md with vendor findings
