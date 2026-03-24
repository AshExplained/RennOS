---
name: media-brief
user-invocable: false
description: Brief on an interviewer, journalist, or outlet — who they are, what they cover, their audience, and how to approach.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Media Brief Playbook

## Inputs

- $ARGUMENTS — Journalist/outlet name or URL
- `data/brand/brand-dna.md` — Positioning context

## Steps

1. Read `data/brand/brand-dna.md` for positioning context
2. Research the target via web:
   - **Person:** Background, beat, recent work, interview style, social presence, past coverage of similar topics
   - **Outlet:** Audience demographics, editorial focus, tone, reach, political/cultural lean
3. Assess alignment:
   - How well does their audience overlap with the user's target?
   - What angle would resonate most with their audience?
   - Any potential risks or sensitive areas?
4. Provide strategic recommendations:
   - Best angle to lead with
   - Tone to match (formal, casual, expert, conversational)
   - Topics to emphasize vs. avoid

## Output

- Write to `data/pr/media-brief-[outlet-or-person]-[date].md`
- Update your MEMORY.md with journalist/outlet profiles for future reference
