---
name: goal-setting
user-invocable: false
description: Define a personal goal with structure, accountability, and clear success criteria.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Goal Setting Playbook

## Inputs

- $ARGUMENTS — The goal the user wants to set, and any context or constraints
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/brand/brand-dna.md` — the user's professional identity
- `vault/personal/goals/` — Existing goals and personal vision
- `vault/personal/` — Personal context and values

## Steps

1. Read the user's profile (`data/brand/brand-dna.md`, `vault/personal/`) to understand broader vision and values
2. Read existing goals in `vault/personal/goals/` to ensure alignment and avoid conflicts
3. Structure the goal with full clarity:
   - **Specific & measurable:** What exactly will be achieved? How will success be measured?
   - **Why it matters:** Connection to the user's deeper motivations and values
   - **Timeline:** Start date, target completion date, key date milestones
   - **Success criteria:** Concrete, observable outcomes that mean "done"
   - **Milestones:** 3-5 intermediate checkpoints with dates
   - **First step:** The single next action to start (make it easy)
   - **Accountability:** How progress will be tracked and reviewed (check-in schedule)
   - **Obstacles:** Anticipated challenges and strategies to overcome them
4. Connect the goal to the user's broader vision — how does this goal serve the bigger picture?

## Output

Create the goal in Obsidian using the CLI:
```bash
obsidian create path="personal/goals/goal-[name]-[date].md" content="[goal content with frontmatter]" vault="vault"
```
Tag it for easy discovery:
```bash
obsidian property:set path="personal/goals/goal-[name]-[date].md" name="tags" value="[goal, area-tag]" type=list vault="vault"
```
- Update your MEMORY.md with the new goal and its connection to the user's broader vision
