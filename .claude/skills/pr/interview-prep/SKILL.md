---
name: interview-prep
user-invocable: false
description: Prepare talking points, key messages, and Q&A for an upcoming interview or media appearance.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Interview Prep Playbook

## Inputs

- $ARGUMENTS — Interview details: who, where, when, topic, format
- `data/brand/brand-dna.md` — Brand positioning
- `data/strategy/audience-personas.md` — Audience context
- `data/pr/` — PR strategy, story angles

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Read `data/brand/brand-dna.md`, `data/strategy/audience-personas.md`, and PR strategy from `data/pr/`
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Research the interviewer and outlet via web (past interviews, style, audience)
5. Define 3-5 key messages the user should land during the interview
6. For each key message: headline + supporting evidence + memorable soundbite
7. Prepare Q&A:
   - 5-7 expected questions with recommended responses
   - 3-5 tough/curveball questions with deflection or reframe strategies
   - Questions to AVOID answering and how to redirect
8. Include opening and closing statements
9. Add bridge phrases for steering back to key messages
10. Note any topics to stay away from or handle carefully

## Output

- Write to `data/pr/interview-prep-[outlet]-[date].md`
- Update your MEMORY.md with interviewer style notes and messaging that works
