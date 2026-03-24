---
name: story-angle
user-invocable: false
description: Identify compelling story angles from brand activities, milestones, or expertise that would interest media.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Story Angle Playbook

## Inputs

- $ARGUMENTS — Recent brand activity, milestone, or topic to angle
- `data/brand/brand-dna.md` — Brand identity
- `data/pr/` — PR strategy
- `data/strategy/quarterly-roadmap.md` — Strategic context

## Steps

1. Read brand DNA, PR strategy from `data/pr/`, and quarterly roadmap
2. Research what media are currently covering via web
3. Identify 3-5 story angles:
   - For each angle:
     - **The hook** — Why would a journalist care?
     - **The narrative** — What's the story?
     - **The proof** — Data, results, unique perspective
     - **The timeliness** — Why now?
     - **Target outlets** — Who would run this?
4. Rank angles by newsworthiness x brand fit x timeliness
5. For the top angle, draft a brief pitch outline (not a full pitch — that's the pitch-draft skill)

## Output

- Write to `data/pr/story-angles-[topic]-[date].md`
- Update your MEMORY.md with angle patterns and what resonates with media
