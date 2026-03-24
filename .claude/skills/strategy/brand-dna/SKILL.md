---
name: brand-dna
user-invocable: false
description: Create or update the brand DNA document — voice, tone, values, messaging pillars. The foundational document all content must align with.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Brand DNA Playbook

## Inputs

- $ARGUMENTS — Interview notes, profile data, existing content, or update instructions
- `.claude/ceo-memory/user_profile.md` — the user's profile and preferences
- `data/brand/brand-dna.md` — Existing brand DNA (if any)

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for domain methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read `${CLAUDE_SKILL_DIR}/examples/example-brand-dna.md` for a completed example
4. Read the user's profile from `.claude/ceo-memory/user_profile.md`
5. Read existing brand DNA (if populated)
6. Analyze voice/tone from any existing content or profiles provided
7. Define or update core identity:
   - **Who** — Who is the user?
   - **What** — What do they do / offer?
   - **Why** — Why does it matter? What's the mission?
8. Define voice characteristics:
   - 4-5 adjectives that describe the voice
   - Examples of on-brand language
   - Anti-examples (what the brand does NOT sound like)
9. Define 3-5 messaging pillars (core themes that all content maps to)
10. Define positioning statement: "For [audience], [brand] is the [category] that [differentiator] because [proof]"
11. If updating (not creating), preserve existing structure and clearly mark what changed

## Output

- Write to `data/brand/brand-dna.md`
- Update your MEMORY.md with key decisions and rationale
