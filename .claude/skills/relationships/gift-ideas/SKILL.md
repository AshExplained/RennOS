---
name: gift-ideas
user-invocable: false
description: Brainstorm gift ideas for someone — thoughtful, personal, and within budget.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Gift Ideas Playbook

## Inputs

- $ARGUMENTS — Who, occasion, budget, their interests
- `data/personal/relationships/contacts.md` — Contact data

## Steps

1. Read contact data for the person — interests, hobbies, past conversations
2. Research gift ideas via web based on their interests and occasion
3. Generate 5-10 gift ideas across categories:
   - **Experiences** — Events, classes, trips
   - **Physical gifts** — Books, gadgets, accessories
   - **Personalized** — Custom items, handmade, engraved
   - **Consumables** — Food, drink, subscription boxes
   - **Digital** — Courses, subscriptions, gift cards
4. For each: description, approximate price, why it fits this person, where to buy
5. Rank by thoughtfulness × budget fit

## Output

- Write to `data/personal/relationships/gift-ideas-[person]-[date].md`
- Update your MEMORY.md with gift patterns
