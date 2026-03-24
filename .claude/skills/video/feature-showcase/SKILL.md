---
name: feature-showcase
user-invocable: false
description: Create a feature showcase video — highlight a specific feature with before/after, close-ups, and value demonstration.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Feature Showcase Playbook

## Inputs

- $ARGUMENTS — Feature name, product context, or video brief reference
- `data/content/video/brief-*.md` — Video brief (if exists)
- `data/brand/brand-dna.md` — Brand voice and visual identity
- Stitch UI screens (pulled via MCP)

## Steps

1. Read the video brief from `data/content/video/` and `data/brand/brand-dna.md`
2. Pull Stitch UI screens via MCP for the feature being showcased
3. Structure the showcase video:
   - **Problem** (3-5s) — Show the pain point or "before" state
   - **Introduction** (2s) — Name the feature with branded text overlay
   - **Demonstration** (10-20s) — Walk through the feature in action:
     - Close-up shots of key UI interactions
     - Annotated callouts pointing to important elements
     - Step-by-step progression with smooth transitions
   - **Before/After** (5s) — Side-by-side or sequential comparison
   - **Result** (3-5s) — Show the outcome / value delivered
   - **CTA** (3s) — Try it, learn more, sign up
4. Use the `stitch-remotion` skill to build the video:
   - Configure composition for target platform dimensions
   - Map screens to sequences with zooming and callout animations
   - Add branded text overlays, lower thirds, and annotations
   - Implement before/after transition (split screen, wipe, or fade)
   - Set pacing — faster for social, slower for product page
5. Generate the video via Bash: `npx remotion render`
6. Document the project — feature shown, screens used, timing, key messaging

## Output

- Write documentation to `data/content/video/feature-[name]-[date].md`
- Remotion project code saved in the appropriate project directory
- Update your MEMORY.md with key findings and patterns discovered
