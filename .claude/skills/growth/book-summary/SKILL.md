---
name: book-summary
user-invocable: false
description: Summarize a book's key takeaways — main ideas, actionable insights, and how they apply to the user.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Book Summary Playbook

## Inputs

- $ARGUMENTS — Book title and author (and any specific angles the user wants covered)
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/brand/brand-dna.md` — the user's brand and professional context
- `vault/personal/` — the user's personal goals and interests
- `data/personal/growth/reading-list.md` — Current reading list

## Steps

1. Read the user's profile (`data/brand/brand-dna.md`, `vault/personal/`) to understand context — what matters to the user, current goals, areas of focus
2. Research the book via web search — reviews, summaries, key themes, author background
3. Create a structured summary:
   - **Core thesis:** The book's central argument in 2-3 sentences
   - **Key takeaways:** 5-7 most important ideas, clearly explained
   - **Actionable insights:** Specific things the user can do based on these ideas
   - **How it applies to the user:** Connect the book's themes to the user's goals, brand, and situation
   - **Best quotes:** 3-5 standout quotes that capture the book's essence
   - **Rating:** Overall value for the user (1-10) with brief justification
4. Update the reading list — mark the book as "finished" with the current date

## Output

- Write the summary to `data/personal/growth/book-summary-[title]-[date].md`
- Update `data/personal/growth/reading-list.md` to mark the book as finished
- Update your MEMORY.md with key takeaways and how they connect to the user's goals
