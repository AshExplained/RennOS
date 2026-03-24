---
name: app-preview
user-invocable: false
description: Create an app store preview video — formatted for App Store or Play Store listing requirements.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# App Preview Playbook

## Inputs

- $ARGUMENTS — App name, target store (iOS/Android/both), or video brief reference
- `data/content/video/brief-*.md` — Video brief (if exists)
- `data/brand/brand-dna.md` — Brand voice and visual identity
- Stitch UI screens (pulled via MCP)

## Steps

1. Read the video brief from `data/content/video/` and `data/brand/brand-dna.md`
2. Research app store video requirements via web:
   - **iOS App Store**: 15-30s, specific resolutions (1080x1920 for iPhone, 1200x1600 for iPad), H.264, no external branding outside app UI
   - **Google Play Store**: 30s-2min, landscape 16:9 recommended, YouTube-hosted, can include device frames
3. Pull Stitch UI screens via MCP for the app's core flows
4. Structure the preview video:
   - **Opening** (2-3s) — App name/logo or hero screen with value proposition
   - **Core Flow 1** (3-5s) — Primary use case demonstration
   - **Core Flow 2** (3-5s) — Secondary feature highlight
   - **Core Flow 3** (3-5s) — Differentiating feature or delight moment
   - **Value Proposition Overlays** — Text reinforcing key benefits during each flow
   - **Closing CTA** (2-3s) — Download now / Get started
5. Use the `stitch-remotion` skill to build the video:
   - Configure composition with correct store dimensions and duration limits
   - Map app screens to sequences showing natural user flows
   - Add polished transitions (no gimmicky effects — clean and professional)
   - Overlay text captions for each feature shown
   - Ensure compliance with store guidelines (no pricing, no misleading content)
6. Generate the video via Bash: `npx remotion render` with correct output dimensions
7. Document the project — store targeted, compliance checklist, screens used

## Output

- Write documentation to `data/content/video/app-preview-[app]-[platform]-[date].md`
- Remotion project code saved in the appropriate project directory
- Update your MEMORY.md with key findings and patterns discovered
