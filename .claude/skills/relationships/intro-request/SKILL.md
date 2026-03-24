---
name: intro-request
user-invocable: false
description: Draft an introduction request — ask a mutual connection to introduce the user to someone.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Intro Request Playbook

## Inputs

- $ARGUMENTS — Who to be introduced to, who to ask, context
- `data/personal/relationships/contacts.md` — Contact data
- `data/brand/brand-dna.md` — Brand identity

## Steps

1. Read contact data and brand DNA
2. Draft the intro request:
   - **To** — The mutual connection
   - **Requesting intro to** — The target person
   - **Why** — Clear reason that benefits all three parties
   - **Context for the connector** — Make it easy for them (short blurb about both parties)
   - **Low pressure** — "Only if you think it's a good fit"
3. Keep it short — under 100 words
4. Provide 2 variants (casual and professional)

## Output

- Write to `data/personal/relationships/intro-request-[person]-[date].md`
- **Reminder:** Intro requests are DRAFTS. the user sends them manually.
- Update your MEMORY.md with intro patterns
