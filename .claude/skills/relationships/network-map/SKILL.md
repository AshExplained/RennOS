---
name: network-map
user-invocable: false
description: Map your network by categories — mentors, peers, industry, personal, potential collaborators.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Network Map Playbook

## Inputs

- $ARGUMENTS — Focus area or "full map"
- `data/personal/relationships/contacts.md` — Contact list

## Steps

1. Read contact list
2. Map contacts by category:
   - **Inner circle** — Closest relationships (5-10 people)
   - **Mentors & advisors** — People the user learns from
   - **Peers** — Same level, mutual support
   - **Industry connections** — Professional network
   - **Potential collaborators** — People to work with
   - **Personal** — Family, close friends
3. Identify network gaps:
   - Missing mentor in a key area?
   - No peers in a specific niche?
   - Weak in a geographic region?
4. Visualize as a text-based map with categories and relationship strength

## Output

- Write to `data/personal/relationships/network-map-[date].md`
- Update your MEMORY.md with network patterns
