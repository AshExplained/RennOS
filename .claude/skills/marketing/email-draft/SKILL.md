---
name: email-draft
user-invocable: false
description: Write a single email — subject line, preview text, body, and CTA. Conversational and on-brand.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Email Draft Playbook

## Inputs

- $ARGUMENTS — Email purpose, key message, CTA, audience segment
- `data/brand/brand-dna.md` — Brand identity and voice
- `data/strategy/audience-personas.md` — Audience profiles

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Write the email:
   - **Subject line** — 3-5 variants (curiosity, value, urgency, personal)
   - **Preview text** — Complements subject line, adds context
   - **Opening** — Personal, hooks the reader in first 2 lines
   - **Body** — One key message, clear and concise, scannable
   - **CTA** — Single clear action, button text + link destination
   - **Sign-off** — On-brand, personal
3. Keep tone conversational — emails are 1:1, not broadcast
4. Keep under 300 words (shorter is better for most emails)
5. Format for mobile-first reading (short paragraphs, line breaks)

## Output

- Write to `data/marketing/email-draft-[name]-[date].md`
- Reminder: All emails are DRAFTS. the user sends them manually.
- Update your MEMORY.md with subject line patterns and email tone calibrations
