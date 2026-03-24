---
name: deal-structure
user-invocable: false
description: Structure a partnership or sponsorship deal — terms, deliverables, pricing, timeline, and negotiation strategy.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Deal Structure Playbook

## Inputs

- $ARGUMENTS — Deal type, partner, scope, initial terms if any
- `data/brand/brand-dna.md` — Brand positioning
- `data/finance/rate-card.md` — Pricing benchmarks
- `data/partnerships/` — Partner brief, sponsorship eval

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for deal structure methodology
2. Apply the negotiation frameworks and deal term standards from the reference
3. Read `data/brand/brand-dna.md`, `data/finance/rate-card.md`, and any existing partner/sponsorship data from `data/partnerships/`
4. Research comparable deals and market rates via web
5. Structure the deal:
   - **Deal type** — Sponsorship, collaboration, affiliate, licensing, speaking fee, retainer
   - **Deliverables** — What the user provides (content, mentions, features, access, IP)
   - **Deliverables from partner** — What they provide (payment, exposure, product, access)
   - **Pricing** — Recommended rate with justification (benchmarked against market + rate card)
   - **Timeline** — Start, milestones, end date, renewal terms
   - **Payment terms** — When, how, penalties for late payment
   - **Exclusivity** — Any exclusivity clauses (and their cost)
   - **IP rights** — Who owns what (content created, repurposing rights)
   - **Termination** — Exit clauses, notice period
6. Define negotiation strategy:
   - **Anchor price** — Start higher than target
   - **Walk-away point** — Minimum acceptable terms
   - **Concessions to offer** — What can you give to get what you want?
   - **Non-negotiables** — What the user won't bend on
7. Flag items that need legal review (@contract-reviewer, Dept 9 — future)

## Output

- Write to `data/partnerships/deal-structure-[partner]-[date].md`
- Update your MEMORY.md with deal patterns and market rate findings
