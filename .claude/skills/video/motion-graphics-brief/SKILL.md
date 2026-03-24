---
name: motion-graphics-brief
user-invocable: false
description: Plan a motion graphics piece — animated logo, kinetic typography, branded intro/outro, lower third, or transition effect.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Motion Graphics Brief Playbook

## Inputs

- $ARGUMENTS — Motion graphics type (logo animation, intro, lower third, transition, kinetic typography), purpose, and context
- `data/brand/brand-dna.md` — Brand voice and visual identity
- Brand visual assets (logo, colors, fonts)

## Steps

1. Read `data/brand/brand-dna.md` and visual identity guidelines
2. Research motion design trends via web:
   - Current motion graphics styles in the brand's industry
   - Animation timing and easing best practices
   - Platform-specific motion requirements
3. Create the motion graphics brief:
   - **Type** — Logo animation, kinetic typography, branded intro/outro, lower third, transition, or custom
   - **Purpose** — Where and how it will be used
   - **Duration** — Target length (logo: 3-5s, intro: 5-8s, lower third: 4-6s, transition: 1-2s)
   - **Visual Style** — Minimal, bold, elegant, playful — aligned with brand
   - **Animation Style** — Smooth/spring, snappy/mechanical, organic/fluid, kinetic/energetic
4. Define key elements and their animation sequence:
   - Element 1 → entrance motion → hold → exit motion
   - Element 2 → entrance motion → hold → exit motion
   - (Stagger timing for visual rhythm)
5. Specify sound design:
   - Swoosh, click, pop, whoosh, or musical sting
   - Sync points (which animation triggers which sound)
6. Create frame-by-frame storyboard:
   - Frame 1 (0s): Starting state
   - Frame 2 (0.5s): First motion
   - Frame 3 (1s): Key pose
   - ... through to final frame
7. Define Remotion implementation approach:
   - React components needed
   - Spring animation configurations (mass, damping, stiffness)
   - Composition structure (sequences, layers)
   - Color and font constants from brand
8. Build and render via Bash: `npx remotion render`

## Output

- Write the brief to `data/content/video/motion-brief-[name]-[date].md`
- Remotion project code saved in the appropriate project directory
- Update your MEMORY.md with key findings and patterns discovered
