---
name: persona-builder
user-invocable: false
description: Build and refine audience personas from data, research, and analytics. Creates detailed profiles of who the audience is.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Persona Builder Playbook

## Inputs

- $ARGUMENTS — Audience data, platform analytics, interview notes, or niche to research
- `data/brand/brand-dna.md` — Brand context
- `data/strategy/audience-personas.md` — Existing personas (if any)

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for persona methodology
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Read existing personas in `data/strategy/audience-personas.md`
4. Read `data/brand/brand-dna.md` for brand context
5. Analyze provided data and research the audience if needed
6. Identify distinct audience segments
7. For each persona, build a detailed profile:
   - **Name** — A memorable label (e.g., "The Aspiring Creator")
   - **Demographics** — Age range, location, profession, income
   - **Psychographics** — Values, beliefs, aspirations, fears
   - **Pain points** — What keeps them up at night?
   - **Goals** — What are they trying to achieve?
   - **Platforms** — Where do they spend time online?
   - **Language patterns** — How do they talk? What words/phrases do they use?
   - **Content preferences** — What formats, topics, and tones resonate?
   - **Influencers they follow** — Who shapes their opinions?
8. Validate each persona against brand positioning — can we genuinely serve this person?

## Output

- Write to `data/strategy/audience-personas.md`
- Update your MEMORY.md with key findings
