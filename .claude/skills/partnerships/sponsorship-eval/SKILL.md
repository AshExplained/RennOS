---
name: sponsorship-eval
user-invocable: false
description: Evaluate an inbound sponsorship opportunity — brand fit, audience alignment, value, and risk assessment.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Sponsorship Evaluation Playbook

## Inputs

- $ARGUMENTS — Sponsor name, offer details, deliverables requested
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Target audience
- `data/finance/rate-card.md` — Pricing benchmarks

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for sponsorship evaluation methodology
2. Apply the scorecard rubric and benchmarks from the reference
3. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and `data/finance/rate-card.md`
4. Research the sponsor via web:
   - Who are they? What do they sell?
   - What's their reputation? Any controversies?
   - Who is their audience?
   - Have they sponsored similar creators/brands?
5. Evaluate the opportunity:
   - **Brand fit** (1-10) — Does this sponsor align with the user's brand values?
   - **Audience alignment** (1-10) — Would the user's audience genuinely benefit from this product/service?
   - **Value** (1-10) — Is the compensation fair for the deliverables requested? (compare to rate card)
   - **Risk** (1-10, lower is better) — Any reputation risk? Controversy? Competitor conflict?
   - **Strategic fit** — Does this align with current goals and roadmap?
6. Calculate overall score and provide clear ACCEPT / NEGOTIATE / DECLINE recommendation
7. If NEGOTIATE: specify what terms to push for
8. If DECLINE: draft a polite decline message

## Output

- Write to `data/partnerships/sponsorship-eval-[sponsor]-[date].md`
- Update your MEMORY.md with sponsor evaluation patterns
