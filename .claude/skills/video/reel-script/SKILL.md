---
name: reel-script
user-invocable: false
description: Write a script for a short-form video (Reel, Short, TikTok) — hook-first, visually structured, platform-optimized.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Reel Script Playbook

## Inputs

- $ARGUMENTS — Topic, platform target, or content brief reference
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles
- Top-performing content references (if available in `data/analytics/`)

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Review top-performing content data if available in `data/analytics/`
3. Research trending formats via web for the target platform:
   - Current trending audio/sounds
   - Popular video structures and transitions
   - Platform-specific algorithm preferences
4. Write the script using the short-form structure:
   - **Hook** (0-3s) — Pattern interrupt, question, bold claim, or visual shock. This is everything.
   - **Setup** (3-8s) — Context, framing, "here's the thing..."
   - **Value** (8-25s) — Core insight, demonstration, story, or proof
   - **Payoff** (25-30s) — Transformation, result, punchline, or reveal
   - **CTA** (last 3s) — Follow, save, comment, link in bio
5. For each section, specify:
   - **On-screen text** — Exact words displayed (large, readable, positioned for mobile)
   - **Audio direction** — Voiceover script, trending sound, or music mood
   - **Visual direction** — What's shown (talking head, screen recording, B-roll, text animation)
6. Provide 2-3 hook variants to A/B test:
   - Variant A: Question hook ("Did you know...?")
   - Variant B: Bold claim hook ("This changed everything...")
   - Variant C: Visual hook (unexpected visual + text overlay)
7. Include hashtag recommendations (3-5 relevant, 1-2 trending)

## Output

- Write the script to `data/content/video/reel-[topic]-[platform]-[date].md`
- Update your MEMORY.md with key findings and patterns discovered
