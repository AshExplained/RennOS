---
name: reflection
user-invocable: false
description: Guided reflection on progress, wins, lessons, and what's next — structured self-awareness.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Reflection Playbook

## Inputs

- $ARGUMENTS — Reflection scope: "weekly", "monthly", a specific goal, or a specific topic
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `vault/personal/goals/` — Goals and past reflections
- `data/personal/growth/` — Learning plans, milestone checks, progress data
- `vault/personal/` — Personal journal entries and notes

## Steps

1. Read goals (`vault/personal/goals/`), learning progress (`data/personal/growth/`), and any journal entries (`vault/personal/`)
2. Guide the reflection through structured prompts:
   - **Wins:** What went well? What progress was made? What should be celebrated?
   - **Lessons:** What was learned — about the skill, the process, or about the user?
   - **Challenges:** What was hard? What caused friction or frustration?
   - **Gratitude:** What is the user grateful for in this period?
   - **Alignment:** Is current effort aligned with stated goals and values?
   - **Adjustments:** What needs to change — habits, priorities, approach?
   - **Intentions:** What does the user want to focus on next?
3. Use a thoughtful, encouraging, and honest tone — this is a safe space for self-awareness
4. Connect insights to concrete actions — every reflection should produce at least one clear next step

## Output

Create the reflection in Obsidian using the CLI:
```bash
obsidian create path="personal/goals/reflection-[date].md" content="[reflection content with frontmatter]" vault="vault"
```
Tag it for easy discovery:
```bash
obsidian property:set path="personal/goals/reflection-[date].md" name="tags" value="[reflection, period-tag]" type=list vault="vault"
```
- Update your MEMORY.md with key insights and any action items identified
