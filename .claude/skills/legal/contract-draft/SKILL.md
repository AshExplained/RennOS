---
name: contract-draft
user-invocable: false
description: Draft a basic contract or agreement — scope, payment, IP, termination, and standard protective clauses.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Contract Draft Playbook

## Inputs

- $ARGUMENTS — Deal type, parties, key terms
- `data/brand/brand-dna.md` — Brand positioning
- `data/partnerships/` — Deal structure

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for contract drafting standards
2. Apply the section templates and plain language principles from the reference
3. Read brand DNA and deal structure from `data/partnerships/`
4. Research standard contract structures for this deal type via web
5. Draft the contract with these sections:
   - **Parties** — Who is involved (names, entities)
   - **Scope of work** — What each party delivers
   - **Timeline** — Start date, milestones, end date
   - **Compensation** — Payment amount, schedule, method
   - **IP rights** — Who owns what (content created, pre-existing IP, usage rights)
   - **Exclusivity** — Any exclusivity terms and their scope/duration
   - **Confidentiality** — What's confidential, for how long
   - **Termination** — How either party can exit, notice period, penalties
   - **Liability** — Limitation of liability, indemnification
   - **Dispute resolution** — How disputes are handled (mediation, arbitration, jurisdiction)
   - **General provisions** — Force majeure, amendments, entire agreement
6. Use plain language — contracts should be understandable, not legalese
7. Mark sections where the user needs to fill in specifics [BRACKETS]

## Output

- Write to `data/legal/contract-draft-[deal-name]-[date].md`
- **Disclaimer:** This is a starting template, not a finalized legal document. Have an attorney review before signing.
- Update your MEMORY.md with contract patterns
