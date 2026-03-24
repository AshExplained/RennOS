---
name: resource-finder
user-invocable: false
description: Find courses, tutorials, books, and resources for learning a skill.
allowed-tools: Read, Write, Edit, Grep, Glob, WebSearch, WebFetch
---

# Resource Finder Playbook

## Inputs

- $ARGUMENTS — Skill or topic to find resources for, and any preferences (free only, beginner-friendly, etc.)
- `.claude/agent-memory/growth-coach/MEMORY.md` — Agent memory
- `data/personal/growth/` — Existing learning plans for context

## Steps

1. Read the learning plan for the specified skill (if one exists) to understand current level, target, and timeline
2. Research via web search across multiple resource types:
   - **Courses:** Online platforms (Coursera, Udemy, Skillshare, etc.)
   - **Books:** Key texts for the skill, both foundational and advanced
   - **Tutorials:** Free guides, YouTube channels, blog series
   - **Practice platforms:** Hands-on environments, exercises, projects
   - **Free vs paid:** Flag cost for each resource
3. For each resource found, capture:
   - **Name** — Title of the resource
   - **Type** — Course / Book / Tutorial / Practice Platform / Community
   - **Cost** — Free / Price
   - **Level** — Beginner / Intermediate / Advanced
   - **Time commitment** — Estimated hours to complete
   - **Rating** — Community rating or reputation (if available)
   - **URL** — Direct link
4. Rank resources by quality x relevance x accessibility (prioritize free, high-rated, level-appropriate)
5. Recommend top 3-5 resources with a brief rationale for each pick

## Output

- Write the resource list to `data/personal/growth/resources-[skill]-[date].md`
- Update your MEMORY.md with top resources found and any patterns noticed
