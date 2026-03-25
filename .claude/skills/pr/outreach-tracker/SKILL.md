---
name: outreach-tracker
user-invocable: false
description: Track media outreach status — who was pitched, when, response status, and follow-up schedule.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Outreach Tracker Playbook

## Inputs

- $ARGUMENTS — New outreach to log, or "review" to check status
- `data/pr/` — Existing tracker, pitch drafts

## Current State
!`cat data/pr/outreach-tracker.md 2>/dev/null`

## Steps

1. Run `python3 -m scripts.pr.outreach_stats` to gather current data
2. Read existing outreach tracker from `data/pr/outreach-tracker.md` if it exists
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. If logging new outreach:
   - Add entry: journalist/outlet, story angle, date pitched, pitch subject line, status (sent/pending/responded/declined/no-response)
   - Use Edit (append) — do NOT overwrite existing entries
5. If reviewing status:
   - Check all entries, flag items needing follow-up (no response after 7 days)
   - Recommend follow-up actions per entry
   - Summarize win rate (responses/total pitches)
6. Maintain clean table format for easy scanning

## Output

- Update `data/pr/outreach-tracker.md` (use Edit to append, not Write to overwrite)
- If creating for the first time, use Write to create `data/pr/outreach-tracker.md`
- Update your MEMORY.md with outreach patterns and response rates
