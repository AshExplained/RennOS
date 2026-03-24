---
name: event-brief
user-invocable: false
description: Prep brief for an upcoming event — audience, key contacts, goals, logistics, and strategic opportunities.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Event Brief Playbook

## Inputs

- $ARGUMENTS — Event name, date, the user's role (speaker/attendee/panelist)
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Target audience

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Research the event via web:
   - Audience demographics and expected size
   - Speaker lineup and other attendees
   - Schedule and key sessions relevant to the user
   - Hashtags and social conversation around the event
3. Create the event brief:
   - **Event overview** — What, when, where, who
   - **the user's role** — Speaker, panelist, attendee, sponsor
   - **Goals for this event** — What does the user want to achieve? (connections, visibility, deals, content)
   - **Key people to connect with** — Specific names and why (potential partners, media, influencers)
   - **Talking points** — Key messages for networking conversations
   - **Content opportunities** — What to post before/during/after (social, stories, recap)
   - **Logistics** — Travel, schedule, prep timeline
4. If the user is speaking → flag to trigger @interview-prep-coach (Dept 4) for talk prep

## Output

- Write to `data/partnerships/event-brief-[event]-[date].md`
- Update your MEMORY.md with event details and key contacts identified
