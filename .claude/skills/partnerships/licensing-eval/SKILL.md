---
name: licensing-eval
user-invocable: false
description: Evaluate a licensing opportunity — is it worth licensing the user's content, brand, or IP to a third party?
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Licensing Evaluation Playbook

## Inputs

- $ARGUMENTS — Licensing offer details, who's asking, what they want to license
- `data/brand/brand-dna.md` — Brand positioning
- `data/finance/rate-card.md` — Pricing benchmarks

## Steps

1. Read `data/brand/brand-dna.md` and `data/finance/rate-card.md`
2. Research the requesting party via web (reputation, reach, how they'd use the IP)
3. Evaluate the opportunity:
   - **IP being licensed** — What specifically? (content, brand name, methodology, templates)
   - **Licensee fit** — Do they align with the user's brand? (1-10)
   - **Market value** — What's this IP worth? (research comparable licensing deals)
   - **Revenue potential** — One-time fee vs royalties vs hybrid
   - **Risk** — Brand dilution, loss of control, misuse, competitive concerns
   - **Exclusivity impact** — Would this limit the user's ability to use their own IP?
   - **Term and territory** — Duration and geographic/platform scope
4. Provide ACCEPT / NEGOTIATE / DECLINE recommendation with rationale
5. If ACCEPT/NEGOTIATE: suggest key terms to include
6. Flag items needing legal review

## Output

- Write to `data/partnerships/licensing-eval-[name]-[date].md`
- Update your MEMORY.md with licensing patterns and market benchmarks
