---
name: video-calendar
user-invocable: false
description: Plan video content calendar — what videos to produce, when, for which platforms, aligned with content strategy.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Video Calendar Playbook

## Inputs

- $ARGUMENTS — Time period, focus areas, or strategic priorities
- `data/content/content-calendar.md` — Existing content schedule
- `data/strategy/quarterly-roadmap.md` — Current strategic roadmap
- `data/content/video/` — Existing video briefs and plans

## Steps

1. Read `data/content/content-calendar.md` and `data/strategy/quarterly-roadmap.md`
2. Scan `data/content/video/` for existing video briefs and completed work
3. Map video topics to strategic themes from the roadmap
4. Balance formats across the period:
   - Long-form (YouTube, course content)
   - Short-form (Reels, Shorts, TikToks)
   - Product videos (demos, showcases, app previews)
   - Educational (lessons, tutorials)
   - Motion graphics (intros, infographics)
5. Set production timeline for each video:
   - Brief due date
   - Script/storyboard date
   - Production date
   - Edit/review date
   - Publish date
6. Coordinate with the broader content calendar to avoid conflicts and maximize cross-promotion
7. For each video entry, specify:
   - Title
   - Format (short-form, long-form, demo, etc.)
   - Platform(s)
   - Key dates (brief → script → produce → publish)
   - Assigned creator agent
8. Flag gaps in coverage — platforms without content, themes without videos, weeks without posts

## Output

- Write the calendar to `data/content/video/video-calendar-[period].md`
- Update your MEMORY.md with key findings and patterns discovered
