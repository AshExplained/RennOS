---
name: animated-infographic
user-invocable: false
description: Create an animated data visualization — stats that reveal, charts that build, numbers that count up. Bring static infographics to life.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Animated Infographic Playbook

## Inputs

- $ARGUMENTS — Data topic, source data, or static infographic reference
- `data/brand/brand-dna.md` — Brand voice and visual identity
- Static infographic content or raw data to visualize

## Steps

1. Read `data/brand/brand-dna.md` and the visual identity guidelines
2. Read the source data or static infographic content
3. Research animated data visualization techniques via web:
   - Best practices for animated charts and graphs
   - Timing and easing for data reveals
   - Accessibility considerations for motion content
4. Design the animation plan:
   - **Data Points** — List every stat, chart, or number to animate
   - **Reveal Sequence** — Order data appears (build narrative tension, most impactful last)
   - **Animation Types** per element:
     - Count-up numbers (0 → final value)
     - Bar grow (height animates from 0)
     - Pie fill (segments sweep in)
     - Line draw (path traces along data points)
     - Icon pop (scale from 0 with spring bounce)
     - Text slide (slide in from edge with fade)
   - **Timing** — Stagger reveals for drama (0.3-0.5s between elements)
   - **Brand Visual Style** — Colors, fonts, iconography from brand identity
5. Implement in Remotion:
   - Create React components for each animation type (CountUp, BarChart, PieChart, LineGraph, IconReveal)
   - Use `spring()` for organic motion and `interpolate()` for linear progressions
   - Structure with `<Sequence>` components for precise timing control
   - Apply brand colors and typography as constants
   - Layer elements with proper z-index for visual hierarchy
6. Add finishing touches:
   - Branded title card at start
   - Source citation at end
   - Subtle background animation or texture
   - Sound design sync points (optional)
7. Render via Bash: `npx remotion render` with target dimensions (1080x1080 for social, 1920x1080 for presentation)
8. Document the project — data sources, animation decisions, render settings

## Output

- Write documentation to `data/content/video/infographic-[topic]-[date].md`
- Remotion project code saved in the appropriate project directory
- Update your MEMORY.md with key findings and patterns discovered
