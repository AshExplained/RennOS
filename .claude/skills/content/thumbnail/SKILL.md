---
name: thumbnail
user-invocable: false
description: Generate thumbnail concepts — text overlays, visual direction, emotion/expression notes.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Thumbnail Playbook

## Inputs

- $ARGUMENTS — Content title, platform, content type
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/brand/visual-identity.md` — Visual brand guidelines

## Steps

1. Read `data/brand/brand-dna.md` and `data/brand/visual-identity.md`
2. Generate 3-5 thumbnail concepts, each with:
   - Text overlay (max 4-6 words)
   - Visual direction (background, imagery, the user's expression if face-cam)
   - Color scheme (aligned with visual identity)
   - Emotion to convey (curiosity, shock, excitement, authority)
3. Consider platform-specific best practices:
   - YouTube: face + text + bright colors
   - Blog: clean, professional, branded
   - Social: bold, scroll-stopping
4. Recommend the top concept with rationale

## Output

- Write thumbnail concepts to `data/content/drafts/thumbnail-[content-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
