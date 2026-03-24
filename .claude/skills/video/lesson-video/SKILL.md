---
name: lesson-video
user-invocable: false
description: Plan and structure a single lesson video — learning objective, visual plan, demonstration flow, and production spec.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Lesson Video Playbook

## Inputs

- $ARGUMENTS — Lesson topic, course context, or learning objective
- Course design document (if part of a course, from `data/content/courses/`)
- `data/brand/brand-dna.md` — Brand voice and visual identity

## Steps

1. Read the course design document if available and `data/brand/brand-dna.md`
2. Research educational video best practices via web:
   - Retention curves — where viewers drop off and why
   - Engagement techniques (questions, visual changes, knowledge checks)
   - Optimal lesson video length by platform (YouTube: 8-15min, course: 5-10min)
3. Define the learning objective — one clear, measurable outcome per lesson
4. Structure the lesson video:
   - **Hook** (0-15s) — Why this matters, what they'll be able to do after watching
   - **Concept Introduction** (15s-2min) — Explain the theory, principle, or framework
   - **Demonstration** (2-5min) — Show it in action:
     - Screen recordings of the process
     - Slides or diagrams for abstract concepts
     - Stitch UI screens for product-related lessons
     - Step-by-step walkthrough with narration
   - **Practice Prompt** — Give the viewer something to try (pause point or exercise)
   - **Summary** (15-30s) — Recap key takeaway, preview next lesson
5. Define production requirements:
   - Screen recordings needed (list specific flows)
   - Slides or diagrams to create
   - Stitch UI screens to pull
   - Narration outline (key points per section, not word-for-word)
   - Background music mood
6. Note visual pacing — change the visual every 10-15 seconds to maintain engagement

## Output

- Write the lesson plan to `data/content/video/lesson-[topic]-[date].md`
- Update your MEMORY.md with key findings and patterns discovered
