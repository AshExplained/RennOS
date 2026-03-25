---
name: content-calendar
user-invocable: false
description: Build or update the weekly/monthly content calendar — what, where, when.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Content Calendar Playbook

## Inputs

- $ARGUMENTS — Time period (e.g., "next week", "March 2026") and any specific content to schedule
- `data/content/content-calendar.md` — Current content calendar
- `data/strategy/quarterly-roadmap.md` — Strategic themes and milestones
- `data/content/drafts/` — Available drafts ready to schedule
- `data/social/` — Platform-adapted content ready to schedule

## Current State
!`ls -1 data/content/drafts/ data/social/ 2>/dev/null | grep -v '.gitkeep'`

## Steps

1. Run `python3 -m scripts.social.list_available_content` to gather current data
2. Read current `data/content/content-calendar.md` and `data/strategy/quarterly-roadmap.md`
3. Check what drafts exist in `data/content/drafts/` and `data/social/` ready to schedule
4. Map content to the calendar:
   - For each day/slot: content piece, platform, format, status (draft/adapted/ready)
5. Ensure alignment with quarterly themes and roadmap milestones
6. Balance content types across the week (educational, personal, promotional, engagement)
7. Flag gaps — days/platforms with no content planned
8. Flag conflicts — too much content stacked on one day

## Output

- Update `data/content/content-calendar.md` with the new schedule
- Update your MEMORY.md with scheduling patterns and what cadence works
