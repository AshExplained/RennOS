---
name: press-release
user-invocable: false
description: Write a press release — newsworthy announcement formatted for media distribution.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Press Release Playbook

## Inputs

- $ARGUMENTS — Announcement, key details, target audience
- `data/brand/brand-dna.md` — Brand identity
- `data/brand/style-guide.md` — Voice and tone
- `data/pr/` — PR strategy, story angles

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for press release standards and conventions
2. Apply the AP-style and structural guidelines from the reference
3. Read `data/brand/brand-dna.md`, `data/brand/style-guide.md`, and PR strategy from `data/pr/`
4. Structure the press release:
   - **Headline** — Clear, newsworthy, active voice
   - **Subheadline** — Supporting context
   - **Dateline** — Location, date
   - **Lead paragraph** — Who, what, when, where, why (most important info first)
   - **Body** — Supporting details, quotes from the user, context, data
   - **Boilerplate** — Standard "About [Brand]" paragraph
   - **Contact** — Media contact information
5. Write in inverted pyramid style (most important → least important)
6. Include 1-2 quotes attributed to the user (on-brand, quotable)
7. Keep under 500 words
8. Note: Draft should be reviewed by @content-editor before going to the user

## Output

- Write to `data/pr/press-release-[topic]-[date].md`
- Update your MEMORY.md with messaging patterns and tone calibrations
