---
name: media-list
user-invocable: false
description: Build or update a targeted media contact list for a specific story, niche, or campaign.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Media List Playbook

## Inputs

- $ARGUMENTS — Niche/topic, story angle, target outlets
- `data/brand/brand-dna.md` — Targeting context
- `data/pr/` — Existing media lists
- `data/strategy/audience-personas.md` — Audience alignment

## Steps

1. Read `data/brand/brand-dna.md` and `data/strategy/audience-personas.md` for targeting context
2. Read existing media lists in `data/pr/` if any
3. Use `${CLAUDE_SKILL_DIR}/template.md` as the output format
4. Research relevant journalists, bloggers, podcasters, and outlets via web:
   - Who covers this niche/topic?
   - What's their reach and audience?
   - What kind of stories do they publish?
   - Have they covered similar topics before?
5. For each contact, log:
   - Name, outlet, role/beat
   - Contact info (email, social handles — if publicly available)
   - Audience size/reach estimate
   - Relevance to the user's brand (1-10)
   - Best approach (email pitch, social DM, mutual connection)
6. Prioritize contacts by relevance and reach

## Output

- Write to `data/pr/media-list-[niche-or-campaign].md`
- Update your MEMORY.md with key findings about the media landscape for this niche
