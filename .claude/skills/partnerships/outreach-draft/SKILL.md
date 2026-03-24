---
name: outreach-draft
user-invocable: false
description: Draft a partnership outreach message — warm, personal, value-first, and tailored to the specific partner.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Outreach Draft Playbook

## Inputs

- $ARGUMENTS — Partner name, partnership idea, channel (email/DM/etc.)
- `data/brand/brand-dna.md` — Brand positioning
- `data/partnerships/` — Partner brief if available

## Steps

1. Read `data/brand/brand-dna.md` and any existing partner brief from `data/partnerships/`
2. Research the partner's recent activity via web (latest content, announcements, wins)
3. Draft the outreach message:
   - **Opening** — Personal reference to their work (specific, not generic)
   - **Connection** — Why you're reaching out (shared audience, aligned values, mutual benefit)
   - **Value proposition** — What's in it for them (lead with their benefit, not yours)
   - **The ask** — Specific, low-commitment next step (call, coffee chat, collab idea)
   - **Sign-off** — Warm, professional
4. Keep it concise — under 150 words for DMs, under 250 for email
5. Provide 2 variants (shorter casual, longer professional)
6. Tailor tone to the channel and partner's communication style

## Output

- Write to `data/partnerships/outreach-[partner-name]-[date].md`
- **Reminder:** Outreach messages are DRAFTS. the user sends them manually.
- Update your MEMORY.md with outreach approach details
