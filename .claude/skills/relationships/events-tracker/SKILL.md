---
name: events-tracker
user-invocable: false
description: Track birthdays, anniversaries, and important dates — never forget the dates that matter.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Events Tracker Playbook

## Inputs

- $ARGUMENTS — New date to add, or "review upcoming"
- `data/personal/relationships/` — Existing events tracker

## Steps

1. Read existing events tracker from `data/personal/relationships/`
2. If adding a new date:
   - Person, date, event type (birthday, anniversary, etc.), recurring (annual), notes
   - Use Edit (append)
3. If reviewing:
   - List upcoming events in next 7/14/30 days
   - Flag events needing action (gift to buy, card to send, plan to make)
   - Suggest gift ideas or gestures for each
4. Feed upcoming dates to @schedule-manager (Dept 7) for calendar integration

## Output

- Update `data/personal/relationships/events-tracker.md` (living document — Edit append)
- Update your MEMORY.md with important dates
