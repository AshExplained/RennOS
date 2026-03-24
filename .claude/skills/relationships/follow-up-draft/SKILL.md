---
name: follow-up-draft
user-invocable: false
description: Draft a follow-up message after a meeting, event, or conversation — warm, specific, and human.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Follow-Up Draft Playbook

## Inputs

- $ARGUMENTS — Who, context (what you discussed, when you met)
- `data/personal/relationships/contacts.md` — Contact data
- `data/brand/brand-dna.md` — Brand identity (for professional follow-ups)

## Steps

1. Read contact data for context on the person
2. Draft the follow-up:
   - **Reference something specific** from your conversation (not generic "nice to meet you")
   - **Add value** — Share a resource, article, or idea related to what you discussed
   - **Next step** — Suggest a specific follow-up (coffee, call, collaboration idea)
   - **Keep it short** — 3-5 sentences
3. Adapt tone to relationship type (professional vs personal, new vs established)
4. Provide 2 variants (shorter and longer)

## Output

- Write to `data/personal/relationships/follow-up-[person]-[date].md`
- **Reminder:** All messages are DRAFTS. the user sends them manually.
- Update your MEMORY.md with follow-up patterns
