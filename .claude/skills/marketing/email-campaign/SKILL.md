---
name: email-campaign
user-invocable: false
description: Design an email campaign — sequence structure, timing, subject lines, and content briefs for each email.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Email Campaign Playbook

## Inputs

- $ARGUMENTS — Campaign goal, audience segment, number of emails, timeline
- `data/brand/brand-dna.md` — Brand identity and voice
- `data/strategy/audience-personas.md` — Audience profiles
- `data/strategy/quarterly-roadmap.md` — Strategic direction

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and roadmap
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Define campaign structure:
   - Campaign goal (nurture, launch, re-engage, onboard, etc.)
   - Target segment (which persona)
   - Number of emails and cadence (daily, every 2 days, weekly)
   - Overall narrative arc across the sequence
5. For each email in the sequence:
   - Purpose/goal for this specific email
   - Subject line (3 variants)
   - Preview text
   - Content brief (key message, tone, CTA)
   - Timing (when to send relative to trigger/previous email)
6. Define entry trigger (opt-in, purchase, behavior, date)
7. Define exit conditions (unsubscribe, conversion, sequence complete)
8. Define success metrics (open rate, click rate, conversion target)

## Output

- Write to `data/marketing/email-campaign-[name]-[date].md`
- Update your MEMORY.md with campaign structures and sequence patterns that work
