---
name: post-publish
user-invocable: false
description: Prepare and format a post for publishing — final formatting, metadata, and pre-publish checklist.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Post Publish Playbook

## Inputs

- $ARGUMENTS — Path to platform-adapted content and platform name
- `data/brand/brand-dna.md` — Brand voice for final check

## Steps

1. Read the platform-adapted content from `data/social/`
2. Run pre-publish checklist:
   - Brand voice alignment (quick check against Brand DNA)
   - Character/length within platform limits
   - Links working (if any mentioned)
   - Hashtags appropriate and current
   - CTA present and clear
   - No sensitive/controversial content without the user's explicit approval
3. Format the final post copy (ready to paste into platform)
4. Include metadata: platform, suggested posting time, target persona, campaign (if applicable)
5. Mark status as "Ready for the user's approval"

## Output

- Write to `data/social/publish-ready-[platform]-[slug].md`
- This is the LAST step before the user manually publishes. The post is NEVER published automatically.
- Update your MEMORY.md with any checklist patterns or recurring issues
