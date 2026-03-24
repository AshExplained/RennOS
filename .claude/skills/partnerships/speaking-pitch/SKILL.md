---
name: speaking-pitch
user-invocable: false
description: Pitch for a speaking slot at an event, conference, or panel — topic, abstract, bio, and why the user is the right speaker.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Speaking Pitch Playbook

## Inputs

- $ARGUMENTS — Event name, topic, format (keynote/panel/workshop)
- `data/brand/brand-dna.md` — Brand positioning
- `data/pr/` — Story angles for talk topics

## Steps

1. Read `data/brand/brand-dna.md` and current PR story angles from `data/pr/`
2. Research the event via web (audience, past speakers, themes, CFP requirements)
3. Write the pitch:
   - **Talk title** — Compelling, specific, benefit-driven (3 variants)
   - **Abstract** — 150-300 word talk summary (what the audience will learn)
   - **Speaker bio** — On-brand, credibility-focused, tailored to this event's audience
   - **Why the user** — Unique perspective, relevant experience, proof points
   - **Audience takeaways** — 3-5 specific things attendees will walk away with
   - **Technical requirements** — Slides, AV, workshop materials (if applicable)
4. Tailor the pitch to the event's theme and audience
5. If CFP has specific questions, address each one directly

## Output

- Write to `data/partnerships/speaking-pitch-[event]-[date].md`
- **Reminder:** Speaking pitches are DRAFTS. the user submits them manually.
- Update your MEMORY.md with event details and pitch approach
