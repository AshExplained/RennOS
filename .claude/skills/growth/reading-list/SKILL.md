---
name: reading-list
user-invocable: false
description: Add to or manage the reading list — to-read, currently reading, finished.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Reading List Playbook

## Inputs

- $ARGUMENTS — Action: "add [book title]", "update [book title] [status]", "review", or book details
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/personal/growth/reading-list.md` — Existing reading list (living document)

## Steps

1. Read the existing reading list at `data/personal/growth/reading-list.md`
2. Determine the action:
   - **If adding a book:** Research the book via web search (author, genre, page count, key topics, why it's worth reading), then add it to the list with status "to-read"
   - **If updating status:** Move the book between statuses — "to-read" → "currently reading" → "finished" (add date started/finished as appropriate)
   - **If reviewing:** List all books organized by status, flag any books that have been "currently reading" for too long (stalled), suggest next reads from "to-read" based on current goals
3. Use Edit to append or modify entries — never overwrite the full file unless restructuring

## Output

- Update `data/personal/growth/reading-list.md` (living document — append or modify, don't overwrite)
- Update your MEMORY.md with changes made to the reading list
