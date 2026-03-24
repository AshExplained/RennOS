---
name: voice-check
user-invocable: false
description: Tactical voice and tone check — does this content sound like us? Fix wording, tone, and style at the line level.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Voice Check Playbook

## Inputs

- $ARGUMENTS — Path to content or content pasted directly
- `data/brand/brand-dna.md` — Brand voice characteristics
- `data/brand/style-guide.md` — Writing and style guidelines

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for voice analysis methodology
2. Apply the voice spectrum and scoring criteria from the reference
3. Read `data/brand/brand-dna.md` voice characteristics (adjectives, examples, anti-examples)
4. Read `data/brand/style-guide.md`
5. Read the content to check
6. Line-by-line analysis:
   - Flag specific phrases/sentences that don't match brand voice
   - For each flag: quote the original, explain why it's off-brand, provide a rewrite
7. Score overall voice alignment (1-10)
8. Provide a summary: "This piece is [X]% on-brand. Key adjustments: [list]"

## Output

- Write voice check report to `data/content/drafts/[name]-voice-check.md`
- Update your MEMORY.md with key findings and patterns discovered

## Note

This is *tactical* (line-level wording/tone fixes). For *strategic* brand alignment (does this campaign fit our positioning?), use @brand-strategist's brand-review skill instead.
