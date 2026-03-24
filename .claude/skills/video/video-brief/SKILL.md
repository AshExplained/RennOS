---
name: video-brief
user-invocable: false
description: Create a video production brief — concept, target audience, format, script outline, visual direction, platform specs.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Video Brief Playbook

## Inputs

- $ARGUMENTS — Video concept, topic, or campaign context
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
2. Research platform-specific video specs via web (dimensions, length limits, format requirements for YouTube, Instagram, TikTok, LinkedIn, etc.)
3. Define the video concept and primary objective (educate, entertain, convert, awareness)
4. Identify the target audience segment from personas
5. Select platform, format, and target length
6. Write the hook — first 3 seconds must stop the scroll
7. Draft the script outline:
   - Hook (0-3s)
   - Setup / context
   - Core value delivery
   - Payoff / transformation
   - CTA
8. Define visual direction:
   - Style (live action, screen recording, motion graphics, mixed)
   - Color palette and brand elements
   - Text overlay style and placement
   - Transitions and pacing
9. Specify audio direction (music mood, voiceover style, sound effects)
10. List production requirements (equipment, software, assets needed)
11. Route to the appropriate creator agent based on video type (demo-walkthrough, feature-showcase, reel-script, etc.)

## Output

- Write the brief to `data/content/video/brief-[name]-[date].md`
- Update your MEMORY.md with key findings and patterns discovered
