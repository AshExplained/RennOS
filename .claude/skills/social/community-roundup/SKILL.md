---
name: community-roundup
user-invocable: false
description: Summarize community activity, sentiment, and notable interactions across platforms.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Community Roundup Playbook

## Inputs

- $ARGUMENTS — Time period and platforms to cover
- `data/social/` — Mention scans, reply drafts, community data
- `data/brand/brand-dna.md` — Brand context

## Steps

1. Read recent mention scans and social activity from `data/social/`
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Summarize:
   - **Volume** — How many mentions, comments, DMs across platforms
   - **Sentiment** — Overall positive/negative/neutral breakdown
   - **Notable interactions** — Standout comments, viral replies, collaboration offers, notable followers who engaged
   - **Common themes** — What are people saying most about the brand?
   - **Community health** — Is engagement growing, stable, or declining?
4. Flag items needing the user's attention (unanswered questions, collaboration offers, negative trends)
5. Recommend community actions (thank a super-fan, address a concern, jump into a conversation)

## Output

- Write to `data/social/community-roundup-[date].md`
- Update your MEMORY.md with community health trends
