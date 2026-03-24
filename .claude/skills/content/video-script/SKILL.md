---
name: video-script
user-invocable: false
description: Write a video script with structure, timing cues, and visual notes. Ready for recording.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Video Script Playbook

## Inputs

- $ARGUMENTS — Topic, format, target length
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/strategy/audience-personas.md` — Target audience profiles

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md`
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Research the topic if needed
5. Define video structure:
   - Hook (first 3-5 seconds)
   - Intro / context
   - Main content (2-4 key points)
   - CTA / outro
6. Write the full script with:
   - Spoken dialogue (what to say)
   - Visual cues [brackets for B-roll, graphics, text overlays]
   - Timing estimates per section
7. Keep language conversational — written for speaking, not reading

## Output

- Write the script to `data/content/drafts/script-video-[topic-slug].md`
- Update your MEMORY.md with key findings and patterns discovered
