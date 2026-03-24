---
name: pr-calendar
user-invocable: false
description: Plan PR activities around key dates, launches, events, and opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# PR Calendar Playbook

## Inputs

- $ARGUMENTS — Time period, any specific events to include
- `data/pr/` — PR strategy, story angles
- `data/strategy/quarterly-roadmap.md` — Strategic milestones
- `data/content/content-calendar.md` — Content schedule
- `data/operations/master-calendar.md` — Master calendar

## Current State
!`cat data/pr/pr-calendar-*.md 2>/dev/null | tail -60`

## Steps

1. Read PR strategy, quarterly roadmap, content calendar, and master calendar
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Map key PR moments:
   - Product/service launches
   - Industry events and conferences
   - Seasonal/cultural moments relevant to the brand
   - Award submission deadlines
   - Speaking opportunity windows
   - Milestone celebrations (follower counts, revenue, anniversaries)
4. For each PR moment:
   - Date/window
   - Story angle to push
   - Target media
   - Deliverables needed (press release, pitch, statement)
   - Lead time required
5. Identify gaps — periods with no PR activity
6. Sync with content calendar to ensure PR and content efforts reinforce each other

## Output

- Write to `data/pr/pr-calendar-[period].md`
- Update your MEMORY.md with PR timing patterns and key dates
