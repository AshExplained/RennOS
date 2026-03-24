---
name: course-video-plan
user-invocable: false
description: Plan video content for an entire course — lesson-by-lesson video structure, production timeline, and resource requirements.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Course Video Plan Playbook

## Inputs

- $ARGUMENTS — Course name, topic, or course design document reference
- Course design document (from `data/content/courses/`)
- `data/brand/brand-dna.md` — Brand voice and visual identity

## Steps

1. Read the course design document from `data/content/courses/` and `data/brand/brand-dna.md`
2. Research course video best practices via web:
   - Optimal lesson length by platform (Udemy, Teachable, YouTube, etc.)
   - Course video production standards and engagement benchmarks
   - Effective course video structures (talking head, screencast, hybrid)
3. Plan the full course video structure:
   - **Course Intro Video** (1-2min) — What they'll learn, who it's for, instructor intro, course overview
   - **Per-Module Intro** (30-60s each) — Module objective, what's covered, why it matters
   - **Per-Lesson Video Plan**:
     - Lesson title
     - Video type (talking head, screencast, slides, hybrid, demo)
     - Target length
     - Visual requirements (slides, screen recordings, Stitch screens, diagrams)
     - Demo/exercise components
     - Key production notes
   - **Course Outro Video** (1-2min) — Recap, next steps, community, upsell
4. Calculate total production scope:
   - Number of videos
   - Estimated total runtime
   - Production assets needed (slides, screens, recordings, graphics)
   - Estimated production timeline (days/weeks)
5. Prioritize the first module as a pilot:
   - Produce Module 1 first to validate format and gather feedback
   - Use pilot to refine production workflow before scaling to full course
6. Define quality checklist for each video (audio, visuals, pacing, branding)

## Output

- Write the plan to `data/content/video/course-video-plan-[course]-[date].md`
- Update your MEMORY.md with key findings and patterns discovered
