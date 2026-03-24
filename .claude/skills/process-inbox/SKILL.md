---
name: process-inbox
description: Process web clippings from vault/inbox/ — categorize, tag with frontmatter, and file to appropriate vault directories. Run during wake-up or when the user says "process my clippings."
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Process Inbox Playbook

Uses the **Obsidian CLI** (`obsidian`) for all vault operations — reading, tagging, and moving files.

## Inputs

- `vault/inbox/` — Unprocessed web clippings
- `data/brand/brand-dna.md` — Brand context for categorization
- `templates/clipping.md` — Clipping template for frontmatter format

## Steps

1. List clippings in inbox:
   ```bash
   obsidian files folder="inbox" vault="vault"
   ```
   If no files found (or only `.gitkeep`), report "Inbox is empty" and stop.

2. For each clipping file, read its content:
   ```bash
   obsidian read path="inbox/[filename].md" vault="vault"
   ```

3. Determine the category based on content:
   | Content about... | Destination |
   |---|---|
   | Health/fitness/nutrition/wellness | `personal/health/` |
   | Relationships/networking | `personal/relationships/` |
   | Goals/motivation/mindset | `personal/goals/` |
   | Professional notes/industry | `professional/notes/` |
   | Learnings/tutorials/skills | `professional/learnings/` |
   | Ideas/product concepts | `professional/ideas/` |
   | Competitor/market intel | Move to `data/strategy/` (outside vault — use Write tool) |
   | Brand/marketing reference | Move to `data/brand/` or `data/marketing/` (outside vault — use Write tool) |

4. Tag the clipping with frontmatter properties:
   ```bash
   obsidian property:set path="inbox/[filename].md" name="status" value="processed" vault="vault"
   obsidian property:set path="inbox/[filename].md" name="tags" value="[category-tag, topic-tag]" type=list vault="vault"
   ```

5. Move the clipping to the appropriate vault directory:
   ```bash
   obsidian move path="inbox/[filename].md" to="[destination-folder]/" vault="vault"
   ```

   **Exception:** If destination is outside vault (`data/strategy/`, `data/brand/`, `data/marketing/`), use the Read tool to get content, Write tool to create the file in `data/`, then delete the original:
   ```bash
   obsidian delete path="inbox/[filename].md" vault="vault"
   ```

6. Report summary to the user: "X clippings processed — N professional, N personal, N moved to company data"

## Obsidian CLI Quick Reference

```bash
# List files in a folder
obsidian files folder="inbox" vault="vault"

# Read a file
obsidian read path="inbox/note.md" vault="vault"

# Set a property (frontmatter)
obsidian property:set path="inbox/note.md" name="status" value="processed" vault="vault"
obsidian property:set path="inbox/note.md" name="tags" value="[tag1, tag2]" type=list vault="vault"

# Move a file
obsidian move path="inbox/note.md" to="professional/notes/" vault="vault"

# Delete a file
obsidian delete path="inbox/note.md" vault="vault"

# Search vault
obsidian search query="keyword" vault="vault"

# List tags
obsidian tags vault="vault"
```

## Output

- Clippings moved from `vault/inbox/` to appropriate directories with proper frontmatter
- Summary report of what was processed and where it went
