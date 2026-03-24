---
name: check-in-draft
user-invocable: false
description: Draft a casual check-in message — keep a relationship warm without needing a reason.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Check-In Draft Playbook

## Inputs

- $ARGUMENTS — Who, any recent context
- `data/personal/relationships/contacts.md` — Contact data

## Steps

1. Read contact data — when was last interaction? What do you know about them?
2. Draft a casual check-in:
   - **Personal touch** — Reference something you know about them (their project, kid, travel)
   - **Light ask** — "How did [thing] go?" or "Saw [relevant thing], thought of you"
   - **No agenda** — This is relationship maintenance, not a pitch
   - **Keep it brief** — 2-3 sentences
3. Tone: genuinely warm, not transactional
4. Provide 2 variants

## Output

- Write to `data/personal/relationships/check-in-[person]-[date].md`
- **Reminder:** All messages are DRAFTS. the user sends them manually.
- Update your MEMORY.md with check-in patterns
