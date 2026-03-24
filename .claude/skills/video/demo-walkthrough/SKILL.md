---
name: demo-walkthrough
user-invocable: false
description: Create a product demo walkthrough video — animate Stitch UI screens with smooth transitions, zooming, and text overlays using Remotion.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Demo Walkthrough Playbook

## Inputs

- $ARGUMENTS — Product name, feature flow, or video brief reference
- `data/content/video/brief-*.md` — Video brief (if exists)
- `data/brand/brand-dna.md` — Brand voice and visual identity
- Stitch UI screens (pulled via MCP)

## Steps

1. Read the video brief from `data/content/video/` and `data/brand/brand-dna.md`
2. Pull Stitch UI screens via MCP for the product flow being demonstrated
3. Use the `stitch-remotion` skill to set up the Remotion project:
   - Configure Remotion composition (dimensions, FPS, duration)
   - Map each screen to a sequence in the timeline
   - Add transitions between screens (fade, slide, zoom)
   - Add text overlays for context and callouts
   - Set timing per screen (typically 3-5s per step)
4. Structure the demo flow:
   - **Intro** (2-3s) — Product name + what you'll see
   - **Setup** (3-5s) — Starting point / context
   - **Core Flow** (15-30s) — Step-by-step walkthrough with annotations
   - **Result** (3-5s) — End state / value delivered
   - **CTA** (3s) — Next action
5. Add visual enhancements:
   - Zoom into key UI elements during explanation
   - Highlight clickable areas with cursor animation or glow
   - Use branded lower thirds for step labels
   - Add subtle motion to static screens (ken burns, parallax)
6. Generate the video via Bash: `npx remotion render`
7. Document the full project — screens used, timing, transitions, render settings

## Output

- Write documentation to `data/content/video/demo-[product]-[date].md`
- Remotion project code saved in the appropriate project directory
- Update your MEMORY.md with key findings and patterns discovered
