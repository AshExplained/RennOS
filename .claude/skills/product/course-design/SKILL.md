---
name: course-design
user-invocable: false
description: Design course curriculum — modules, lessons, learning outcomes, and structure.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Course Design Playbook

## Inputs

- $ARGUMENTS — Course topic, target audience, desired outcome, format (self-paced/live/hybrid)
- `data/brand/brand-dna.md` — Core brand identity
- `data/strategy/audience-personas.md` — Audience segments
- `data/content/top-performers.md` — Top-performing content (for topic validation)

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for course design methodology
2. Apply the backward design and learning frameworks from the reference
3. Read brand DNA, audience personas, and top-performing content
4. Research course design best practices and competitor courses via web
5. Define the course:
   - **Title** — Benefit-driven, specific
   - **Target student** — Which persona, what they already know, what they want to achieve
   - **Transformation promise** — "By the end, you will be able to..."
   - **Format** — Self-paced / live cohort / hybrid, length, cadence
6. Design the curriculum:
   - **Modules** (3-8) — Each with a clear theme and learning outcome
   - **Lessons per module** (2-5) — Each with specific objective, content type (video/text/exercise), estimated time
   - **Exercises/assignments** — Practical application per module
   - **Milestones** — Checkpoints where students prove progress
7. Identify existing content that can be repurposed into course material
8. Define delivery requirements (platform, tech, production assets needed)

## Output

- Write to `data/product/course-design-[name]-[date].md`
- Update your MEMORY.md with course design patterns
