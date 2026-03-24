---
name: contract-review
user-invocable: false
description: Review a contract or agreement — flag risks, missing terms, unfavorable clauses, and red flags.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Contract Review Playbook

## Inputs

- $ARGUMENTS — Contract text or path to contract file
- `data/brand/brand-dna.md` — Brand positioning
- `data/finance/rate-card.md` — Pricing benchmarks
- `data/partnerships/` — Deal structure context

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for contract review methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read brand DNA and rate card for context
4. Read the contract thoroughly
5. Research comparable contract terms via web for the deal type
6. Review clause by clause, flagging:
   - **Red flags** — Clauses that are unusually unfavorable or exploitative
   - **Missing terms** — Important clauses that should be there but aren't (termination, IP rights, payment terms, liability limits, exclusivity scope)
   - **Unfavorable terms** — Clauses that tilt too far against the user's interests
   - **Ambiguous language** — Clauses that could be interpreted multiple ways
   - **Compliance issues** — Terms that conflict with regulations (FTC, GDPR)
7. For each flagged item: quote the clause, explain the risk, recommend a fix
8. Rate overall contract risk: LOW / MEDIUM / HIGH
9. Provide a summary: sign as-is / negotiate these points / walk away

## Output

- Write to `data/legal/contract-review-[deal-name]-[date].md`
- **Disclaimer:** This is advisory guidance, not legal advice. Consult an attorney for significant contracts.
- Update your MEMORY.md with contract risk patterns
