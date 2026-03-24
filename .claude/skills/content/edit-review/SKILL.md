---
name: edit-review
user-invocable: false
description: Edit and polish any content piece — grammar, clarity, flow, structure, and overall quality.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Edit & Review Playbook

## Inputs

- $ARGUMENTS — Path to draft in `data/content/drafts/`, or content pasted directly
- `data/brand/brand-dna.md` — Brand voice and positioning
- `data/brand/style-guide.md` — Writing and style guidelines

## Current State
!`cat data/brand/brand-dna.md 2>/dev/null`

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for editing methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the editor's note format
3. Read `data/brand/brand-dna.md` and `data/brand/style-guide.md`
4. Read the draft to edit
5. First pass — structural edit:
   - Does the structure flow logically?
   - Is the hook strong enough?
   - Is the CTA clear?
   - Are there sections that drag or feel redundant?
6. Second pass — line edit:
   - Grammar and punctuation
   - Sentence clarity and conciseness
   - Word choice (remove filler, strengthen verbs)
   - Readability (break up long paragraphs, add transitions)
7. Third pass — brand voice check:
   - Does it sound like us? (refer to brand DNA voice characteristics)
   - Fix any off-brand language
8. Write a brief editor's note summarizing changes made and any flags for the CEO agent/user

## Output

- Write edited version to same path (overwrite draft) or `data/content/drafts/[name]-edited.md`
- Include editor's note at top documenting changes
- Update your MEMORY.md with key findings and patterns discovered
