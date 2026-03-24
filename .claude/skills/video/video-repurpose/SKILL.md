---
name: video-repurpose
user-invocable: false
description: Plan how to repurpose a long-form video into multiple short-form clips and derivative content.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Video Repurpose Playbook

## Inputs

- $ARGUMENTS — Source video title, file path, or brief reference
- Source video details (transcript, timestamps, key topics)

## Steps

1. Read the source video details — transcript, brief, or script from `data/content/video/`
2. Identify repurposable segments:
   - Key moments with high impact or emotion
   - Standalone soundbites (quotable, punchy, shareable)
   - Visual highlights (demos, reveals, before/after)
   - Teaching moments that work out of context
   - Controversial or attention-grabbing takes
3. Plan derivative content for each segment:
   - **YouTube Shorts** — vertical 60s max, hook-first edit
   - **Instagram Reels** — vertical 90s max, text overlays, trending audio option
   - **TikTok** — vertical 60s, native feel, trend-aligned
   - **Audiogram** — waveform animation over key audio clip
   - **GIFs** — loopable visual moments for social/email
   - **Blog post** — written version from transcript, expanded with links
   - **Social quotes** — text cards from best soundbites
4. For each derivative, document:
   - Source timestamp (start-end)
   - Target platform
   - Edit notes (crop, text overlays, music, pacing adjustments)
   - Caption / description
   - Hashtags
5. Prioritize derivatives by effort vs. impact

## Output

- Write the repurpose plan to `data/content/video/repurpose-plan-[source]-[date].md`
- Update your MEMORY.md with key findings and patterns discovered
