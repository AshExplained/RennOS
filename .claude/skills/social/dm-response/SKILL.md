---
name: dm-response
user-invocable: false
description: Draft DM responses — professional, warm, and on-brand. For collaboration requests, questions, or outreach.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# DM Response Playbook

## Inputs

- $ARGUMENTS — The DM content, sender context, and platform
- `data/brand/brand-dna.md` — Brand voice

## Steps

1. Read `data/brand/brand-dna.md`
2. Understand the DM: who sent it, what they want, what platform
3. Categorize the DM:
   - **Collaboration request** — Respond with interest + next steps (or polite decline)
   - **Question/advice** — Respond helpfully, link to content/resources
   - **Business inquiry** — Professional response, suggest scheduling a call
   - **Fan message** — Warm, appreciative, encourage continued engagement
   - **Spam/irrelevant** — Flag to the CEO agent, draft polite decline or recommend ignore
4. Draft a response that is warm, professional, and moves the conversation forward
5. Provide 2 variants (shorter and longer)

## Output

- Write to `data/social/dm-response-[date]-[sender].md`
- **Reminder:** DM responses are DRAFTS. the user sends them manually.
- Update your MEMORY.md with DM patterns and response approaches that work
