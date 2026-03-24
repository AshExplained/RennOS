---
name: contact-add
user-invocable: false
description: Add a new contact with context — who they are, how you met, what you discussed, and follow-up notes.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Contact Add Playbook

## Inputs

- $ARGUMENTS — Person name, context, how you met, notes
- `data/personal/relationships/` — Existing contact list

## Steps

1. Read existing contact list from `data/personal/relationships/`
2. Add new contact entry:
   - **Name**
   - **Category** — Mentor, peer, industry, personal, family, potential partner
   - **How we met** — Event, intro, online, work
   - **Date met**
   - **Context** — What we discussed, shared interests, what they do
   - **Contact info** — Email, social handles (if provided)
   - **Relationship strength** — New / warm / strong / close
   - **Follow-up** — Any next steps or things to remember
3. Use Edit (append) — do NOT overwrite existing contacts

## Output

- Update `data/personal/relationships/contacts.md` (living document — Edit append)
- Update your MEMORY.md with contact patterns
