---
name: privacy-policy
user-invocable: false
description: Draft or update a privacy policy for the user's website, app, or service.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Privacy Policy Playbook

## Inputs

- $ARGUMENTS — "create" or "update", what the website/app does, what data is collected
- `data/brand/brand-dna.md` — Brand positioning
- `data/legal/` — Existing privacy policy

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for privacy policy requirements
2. Apply the regulatory requirements and section templates from the reference
3. Read brand DNA and any existing privacy policy
4. Research current privacy requirements via web (GDPR, CCPA, ePrivacy, platform-specific)
5. Draft/update the privacy policy covering:
   - **What data is collected** — Personal info, usage data, cookies, analytics
   - **How data is collected** — Forms, cookies, third-party tools, pixels
   - **Why data is collected** — Purpose for each data type
   - **How data is used** — Marketing, personalization, analytics, service delivery
   - **Data sharing** — Third parties who receive data (analytics, email tools, ad platforms)
   - **Data storage** — Where stored, how long retained, security measures
   - **User rights** — Access, correction, deletion, portability (GDPR/CCPA rights)
   - **Cookies** — What cookies are used, how to opt out
   - **Children's privacy** — COPPA compliance if applicable
   - **Contact** — How to reach the data controller
   - **Changes** — How policy updates are communicated
6. Use plain language — privacy policies should be understandable
7. Note which sections are legally required vs best practice

## Output

- Write to `data/legal/privacy-policy-[date].md`
- **Disclaimer:** This is a template, not a finalized legal document. Have an attorney review before publishing.
- Update your MEMORY.md with privacy regulation patterns
