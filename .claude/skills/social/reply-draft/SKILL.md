---
name: reply-draft
user-invocable: false
description: Draft replies to comments and mentions — on-brand, engaging, and human-sounding.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Reply Draft Playbook

## Inputs

- $ARGUMENTS — The comment/mention to reply to, platform, and context
- `data/brand/brand-dna.md` — Brand voice characteristics

## Steps

1. Read `data/brand/brand-dna.md` voice characteristics
2. Read the comment/mention and understand context (positive, negative, question, collaboration offer, etc.)
3. Draft a reply that is:
   - On-brand in voice and tone
   - Engaging and human (not corporate/robotic)
   - Appropriate to the platform's culture
   - Proportional to the comment (don't over-reply to simple compliments)
4. For different comment types:
   - **Compliment/positive:** Thank warmly, add value, encourage further engagement
   - **Question:** Answer helpfully, link to relevant content if applicable
   - **Criticism/negative:** Acknowledge, don't get defensive, offer to help or take offline
   - **Troll/bad faith:** Short, unbothered, or ignore (recommend to the CEO agent)
5. Provide 2-3 reply variants for the CEO agent/user to choose from

## Output

- Write to `data/social/reply-draft-[date]-[context].md`
- **Reminder:** Replies are DRAFTS. the user sends them manually.
- Update your MEMORY.md with reply patterns and what resonates
