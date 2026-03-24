---
name: site-update
user-invocable: false
description: Make updates to the website — new pages, edits, design tweaks, content changes.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
---

# Site Update Playbook

## Inputs

- $ARGUMENTS — Description of the update (new page, edit, design tweak, or content change)
- `data/brand/brand-dna.md` — Brand identity and visual guidelines
- Design specs or mockups if provided

## Steps

1. Read `data/brand/brand-dna.md` to ensure all changes align with brand identity
2. Read any referenced design specs, copy docs, or mockups
3. Glob/Grep the site codebase to locate the files that need changing
4. Identify the full scope of changes — pages, components, styles, assets
5. Make the changes:
   - Use Write for new files (pages, components, assets)
   - Use Edit for modifications to existing files
   - Use Bash for build commands, dependency installs, or local testing
6. Verify changes don't break existing functionality (Grep for broken references, Bash for build/test)
7. Test locally via Bash if a dev server is available
8. Document all changes made — what files were touched, what was added/modified/removed

## Output

- Write a change log to `data/tech/site-update-[date].md` with: summary, files changed, testing notes, any follow-ups needed
- Actual code changes applied to the site codebase
- Update your MEMORY.md with key findings and patterns discovered
