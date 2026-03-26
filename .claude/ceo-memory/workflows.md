# Operational Workflows

## Multi-Agent Workflow Playbooks

Repeatable multi-step processes live in **`.claude/workflows/`**. Before improvising a chain, check if a workflow exists.

| Workflow | File | Trigger | Profile |
|----------|------|---------|---------|
| Content Publish | `content-publish.md` | "Write/publish a blog post" | Full, B&B |
| Content Repurpose | `content-repurpose.md` | "Repurpose this into social content" | Full, B&B |
| Weekly Review | `weekly-review.md` | "Weekly review" / "Sunday review" | All |
| Partnership Deal | `partnership-deal.md` | "We got a sponsorship inquiry" / "Reach out to [brand]" | Full, B&B |
| Product Launch | `product-launch.md` | "Launch [product]" / "Plan a product launch" | Full, B&B |
| Audience Deep Dive | `audience-deep-dive.md` | "Research my audience" / "Update personas" | Full, B&B |
| Crisis Response | `crisis-response.md` | Negative press, controversy, reputation threat | Full, B&B |
| Personal Reset | `personal-reset.md` | "I need a reset" / "Things have slipped" | Full, Life |

**Creating new workflows:** After completing any multi-step chain (3+ agents), the CEO agent uses judgment: *"Would this be useful as a repeatable workflow?"* If yes, suggest it to the user. See `.claude/workflows/README.md` for the template.

---

## Task Management — Two Systems

You have two task systems. Use both — they serve different purposes.

### Claude Tasks (Internal Execution)
Use `TaskCreate`, `TaskUpdate`, `TaskList` to track agent work within and across sessions.
- **When the user asks you to do something** — break it into tasks, delegate to agents, update status as they complete
- **Granularity:** Specific to-dos — "Write hero section copy", "SEO optimize blog draft", "Draft 3 subject lines"
- **Persistence:** Tasks survive across sessions (stored at `~/.claude/tasks/rennos/`)
- **Audience:** You and your agents. The user doesn't need to look at these.
- **On wake-up:** Check TaskList for incomplete items from previous sessions

### Asana (External Visibility)
Use Asana MCP tools for projects and milestones the user needs to track outside Claude Code.
- **When the user needs visibility** — create/update Asana tasks for real project milestones
- **Granularity:** Project-level — "Q2 Course Launch", "Sponsorship Pipeline", "Website Redesign"
- **Persistence:** Permanent. The user checks from phone/browser.
- **Audience:** The user. This is their project management view.

### When to use which
| Situation | System |
|-----------|--------|
| Breaking down work for agents | Claude Tasks |
| Tracking agent execution progress | Claude Tasks |
| Project milestone the user wants to track | Asana |
| Multi-week initiative with timeline | Asana |
| Quick delegation to one agent | Neither — just delegate |

### Asana Pilot — Dept 10 (Web & Tech)
Asana is currently piloting with the Scrum Dev Team (Dept 10 Team B). Use Asana MCP tools for:
- Sprint boards and backlog management (@scrum-master)
- Task assignment and status tracking (all Team B agents)
- Sprint reviews and velocity tracking

Other departments do NOT use Asana yet. Expansion will follow after pilot proves the workflow.

---

## Software Development Workflow (Dept 10 Scrum Team)

### Design Freeze Gate
When building software products, designs must be approved before coding starts:
1. @product-designer writes product spec
2. @ux-designer generates UI screens in Google Stitch
3. @visual-designer reviews for brand consistency
4. **The CEO agent presents designs to the user for design freeze approval**
5. Only after the user says "go" → @scrum-master plans the sprint
6. No coding without frozen designs — this is a hard gate

### Dept 10 Dev Team Exception to Approval Gate
Dev agents (Team B) are authorized to execute code, create branches, open PRs, and deploy to **staging** as part of normal sprint work. However, three hard gates require the user (Sponsor) as human-in-the-loop:

1. **Design Freeze** — The user reviews and approves UI designs before any sprint starts
2. **UAT (User Acceptance Testing)** — After staging deployment, the user tests the product and confirms it meets requirements. The CEO agent presents the staging build + Asana task summary. No production deploy without UAT sign-off.
3. **Production Deployment** — The user explicitly approves go-live after UAT passes

Other dev team rules:
- **PR merges to main** require @tech-lead review + QA sign-off
- All activity is traceable via Asana tasks (with Stitch design refs + GitHub PR links)
