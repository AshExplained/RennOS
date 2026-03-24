---
name: media-statement
user-invocable: false
description: Draft a public statement or official response — for announcements, reactions, or crisis communications.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Media Statement Playbook

## Inputs

- $ARGUMENTS — Situation, key message, audience
- `data/brand/brand-dna.md` — Brand identity
- `data/pr/` — PR strategy, any crisis context

## Steps

1. Read `data/brand/brand-dna.md` and relevant PR context from `data/pr/`
2. Assess the situation: proactive announcement vs reactive response
3. Draft the statement:
   - **Proactive:** Lead with the news, explain significance, include vision/next steps
   - **Reactive:** Acknowledge the situation, state position, explain actions being taken
4. Keep tone measured, professional, and on-brand
5. Include 2-3 variants:
   - Shorter social-ready version
   - Full statement
   - Q&A companion
6. Flag any legal/compliance considerations for the CEO agent's review
7. Note: Draft should be reviewed by @content-editor before going to the user

## Output

- Write to `data/pr/media-statement-[topic]-[date].md`
- Update your MEMORY.md with statement patterns and tone calibrations
