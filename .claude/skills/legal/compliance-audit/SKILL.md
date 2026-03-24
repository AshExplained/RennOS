---
name: compliance-audit
user-invocable: false
description: Audit current practices against regulations — GDPR, CAN-SPAM, FTC, CCPA, and platform policies.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Compliance Audit Playbook

## Inputs

- $ARGUMENTS — Scope: "full audit" or specific area like "email" or "social"
- `data/brand/brand-dna.md` — Brand positioning
- `data/marketing/` — Campaign and email data
- `data/content/` — Content data
- `data/social/` — Social data
- `data/legal/` — Past compliance checks

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for regulatory requirements
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read all relevant data across departments
4. Research current regulatory requirements via web:
   - FTC endorsement guidelines
   - GDPR requirements (if EU audience)
   - CAN-SPAM Act requirements (email)
   - CCPA requirements (if California audience)
   - Platform-specific policies
5. Audit each area:
   - **Email marketing** — CAN-SPAM compliance (unsubscribe, physical address, honest subject lines)
   - **Sponsored content** — FTC disclosure across all platforms
   - **Data collection** — GDPR/CCPA consent, privacy policy, cookie notice
   - **Social media** — Platform ToS compliance across all active platforms
   - **Advertising** — Truthful claims, proper disclosures, targeting restrictions
6. For each area: compliant / partially compliant / non-compliant
7. For non-compliant items: what's wrong, risk level, how to fix, priority
8. Overall compliance score and action plan

## Output

- Write to `data/legal/compliance-audit-[date].md`
- Update your MEMORY.md with compliance patterns
