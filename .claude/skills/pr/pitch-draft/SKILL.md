---
name: pitch-draft
user-invocable: false
description: Draft a media pitch for a specific story angle, tailored to the target journalist/outlet.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Pitch Draft Playbook

## Inputs

- $ARGUMENTS — Story angle, target journalist/outlet, context
- `data/brand/brand-dna.md` — Brand positioning
- `data/pr/` — Story angles, media lists

## Steps

1. Read `${CLAUDE_SKILL_DIR}/references/best-practices.md` for pitch structure and journalist preferences
2. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
3. Apply the pitch anatomy and best practices from the reference
4. Read `data/brand/brand-dna.md` and relevant story angles from `data/pr/`
5. Research the target journalist/outlet via web (what do they cover, recent articles, style)
6. Draft the pitch:
   - **Subject line** — Compelling, specific, not clickbait
   - **Opening hook** — Why this matters to their audience
   - **The story** — What's the angle, what's newsworthy
   - **Why the user** — Credentials, unique perspective, proof points
   - **The ask** — Interview, feature, guest post, quote
   - **Logistics** — Availability, assets, timeline
7. Keep it concise — journalists get hundreds of pitches. Under 200 words ideal.
8. Provide 2-3 subject line variants
9. Tailor tone to the outlet (casual for blogs, formal for trade press, personal for podcasts)

## Output

- Write to `data/pr/pitch-[journalist-or-outlet]-[date].md`
- **Reminder:** Pitches are DRAFTS. the user sends them manually.
- Update your MEMORY.md with pitch angle and target details
