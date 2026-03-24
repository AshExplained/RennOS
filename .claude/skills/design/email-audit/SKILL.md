---
name: email-audit
user-invocable: false
description: Audit email templates for visual consistency, brand alignment, and mobile responsiveness.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Email Audit Playbook

## Inputs

- $ARGUMENTS — Email template or campaign to audit
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system
- `data/brand/style-guide.md` — Style guide

## Steps

1. Read brand DNA, visual identity, and style guide
2. Audit the email template:
   - **Brand alignment** — Colors, fonts, imagery match visual identity?
   - **Layout consistency** — Does it follow the established email template structure?
   - **Readability** — Font sizes, line heights, contrast, paragraph length
   - **CTA visibility** — Is the button prominent and above the fold?
   - **Mobile responsiveness** — Does it stack properly? Touch targets adequate?
   - **Image handling** — Alt text present? Reasonable file sizes? Fallback for images-off?
   - **Footer compliance** — Unsubscribe link, physical address (CAN-SPAM), social links
3. Score each dimension 1-10
4. For each issue: what's wrong, severity, recommended fix
5. Overall verdict: ON-BRAND / NEEDS ADJUSTMENTS / OFF-BRAND

## Output

- Write to `data/design/email-audit-[template]-[date].md`
- Update your MEMORY.md with email audit patterns
