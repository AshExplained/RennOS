---
name: data-audit
user-invocable: false
description: Audit what data the user collects, how it's stored, who has access, and whether practices comply with regulations.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Data Audit Playbook

## Inputs

- $ARGUMENTS — Scope: "full audit" or specific tool/platform
- `data/legal/` — Privacy policy
- `data/marketing/` — Email list strategy

## Steps

1. Read existing privacy policy and marketing data
2. Research current data protection requirements via web
3. Audit data practices:
   - **Data inventory** — What personal data is collected, where, and in what tools
   - **Consent** — Is proper consent obtained for each data type?
   - **Storage** — Where is data stored? Is it encrypted? Who has access?
   - **Retention** — How long is data kept? Is there a deletion schedule?
   - **Third-party sharing** — Which tools/services receive personal data? Are DPAs in place?
   - **Rights fulfillment** — Can you respond to access/deletion requests?
   - **Breach readiness** — Is there a breach notification plan?
4. For each area: compliant / partially compliant / non-compliant / unknown
5. Risk assessment: what's the exposure if current practices are audited?
6. Action plan: priority fixes ordered by risk level

## Output

- Write to `data/legal/data-audit-[date].md`
- Update your MEMORY.md with data practice patterns
