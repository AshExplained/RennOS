---
name: asset-brief
user-invocable: false
description: Create a brief for visual assets — photos, illustrations, icons, or graphics needed for a specific project.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Asset Brief Playbook

## Inputs

- $ARGUMENTS — What assets are needed, for what project/content
- `data/brand/brand-dna.md` — Core brand identity
- `data/brand/visual-identity.md` — Visual system

## Steps

1. Read brand DNA and visual identity
2. Define each asset needed:
   - **Asset type** — Photo, illustration, icon, graphic, animation
   - **Purpose** — Where it will be used (blog header, social post, landing page, email)
   - **Dimensions** — Size specifications per placement
   - **Visual direction** — Mood, style, colors (aligned with visual identity)
   - **Content** — What should be depicted or communicated
   - **Text overlays** — Any text that goes on the image
   - **Reference** — Example images or style references
3. Group assets by project/campaign for production efficiency
4. Note priority and deadline per asset

## Output

- Write to `data/design/asset-brief-[project]-[date].md`
- Update your MEMORY.md with asset patterns
