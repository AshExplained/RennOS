---
name: mention-scan
user-invocable: false
description: Scan for brand mentions, tags, and relevant conversations across platforms. Early warning for opportunities and threats.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Mention Scan Playbook

## Inputs

- $ARGUMENTS — Brand name/handles to scan, platforms, optional time window
- `data/brand/brand-dna.md` — Context on what to look for

## Current State
!`ls -1t data/social/mention-scan-* data/inbox/mention-scan-* 2>/dev/null | head -5`

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md` for context on what to look for
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Search the web for brand mentions:
   - Direct @mentions and tags
   - Name mentions without tags
   - Discussions about topics where the brand has authority
   - Competitor mentions (for context)
5. For each mention found, log:
   - Platform and source
   - Sentiment (positive/negative/neutral)
   - Reach/influence of the poster
   - Whether a response is warranted
   - Urgency (time-sensitive or not)
6. Categorize findings:
   - **Opportunities** — Positive mentions to amplify, collab requests, PR moments
   - **Threats** — Negative sentiment, complaints, reputation risks
   - **Neutral** — Informational mentions, no action needed
7. Flag urgent items at the top of the report

## Output

- On-demand: Write to `data/social/mention-scan-[date].md`
- Scheduled runs: Write to `data/inbox/mention-scan-[date].md`
- **Scheduled:** Daily 8:15am → writes to `data/inbox/` (requires `/loop` or scheduler — currently on-demand only)

## Cross-Department Triggers

- If reputation threat detected → flag for @crisis-manager (PR & Communications, Dept 4)
- If unauthorized IP use spotted → flag for @ip-protector (Legal & Compliance, Dept 9)

## Post-Task

- Update your MEMORY.md with mention patterns and sentiment trends
