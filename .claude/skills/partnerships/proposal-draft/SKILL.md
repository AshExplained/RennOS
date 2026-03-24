---
name: proposal-draft
user-invocable: false
description: Write a partnership or sponsorship proposal — the formal document sent to a partner outlining the opportunity.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Proposal Draft Playbook

## Inputs

- $ARGUMENTS — Partner, deal type, key terms
- `data/brand/brand-dna.md` — Brand positioning
- `data/partnerships/` — Deal structure, partner brief, media kit

## Steps

1. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
2. Read `data/brand/brand-dna.md`, deal structure, and partner brief from `data/partnerships/`
3. Write the proposal:
   - **Introduction** — Who the user is, brief positioning (reference media kit)
   - **The opportunity** — What this partnership looks like
   - **Mutual value** — What both sides gain (lead with their value)
   - **Audience** — Key audience stats (size, demographics, engagement — pull from media kit)
   - **Deliverables** — What the user will deliver, with timeline
   - **Investment** — Pricing/terms (from deal structure)
   - **Case studies/proof** — Past partnerships, results, testimonials (if available)
   - **Next steps** — Clear CTA (schedule a call, reply to discuss)
4. Keep it professional but not corporate — match brand voice
5. Format for easy scanning (headers, bullet points, minimal long paragraphs)

## Output

- Write to `data/partnerships/proposal-[partner]-[date].md`
- **Reminder:** Proposals are DRAFTS. the user sends them manually.
- Update your MEMORY.md with proposal patterns
