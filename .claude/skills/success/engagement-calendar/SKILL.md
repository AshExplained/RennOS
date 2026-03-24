---
name: engagement-calendar
user-invocable: false
description: Create an engagement calendar for a paid community — events, AMAs, challenges, and content drops.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Engagement Calendar Playbook

## Inputs

- $ARGUMENTS — Community name, time period, any specific events to include
- `data/customers/community-plan-*.md` — Community plan
- `data/content/content-calendar.md` — Content calendar

## Steps

1. Read community plan and content calendar
2. Design the engagement calendar:
   - **Weekly recurring:** Discussion prompts, wins sharing, resource drops
   - **Bi-weekly:** Live AMAs, workshops, or co-working sessions
   - **Monthly:** Guest expert session, monthly challenge, retrospective
   - **Quarterly:** Community milestone celebration, survey, roadmap share
3. For each event: date, type, topic, format (live/async), who runs it, prep needed
4. Balance event density — enough to keep engagement up, not so much it's overwhelming
5. Sync with content calendar to avoid conflicts

## Output

- Write to `data/customers/engagement-calendar-[community]-[date].md`
- Update your MEMORY.md with engagement patterns
