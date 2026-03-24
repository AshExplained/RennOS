# Available Tools & Integrations

> What's connected, what each tool does, and when to use it.

## MCP Servers (Live)

### Asana MCP (`mcp__claude_ai_Asana__`)
**What:** Project management — create projects, manage tasks, track sprints, status updates.
**Scope:** Piloting with Dept 10 Scrum Team only. Other departments do NOT use Asana yet.
**When to use:** Sprint boards, backlog management, task assignment, project milestones the user needs to track externally.
**Key tools:**
- `search_objects` — Find projects, tasks, users
- `create_project_preview` + `create_project_confirm` — Create Asana projects
- `create_task_preview` + `create_task_confirm` — Create tasks
- `update_task` — Update task status, assignee, notes, due dates (supports `html_notes` for PR/design links)
- `get_tasks` — List tasks in a project/section
- `get_status_overview` — Get project status summary

**Agents with Asana access:** @scrum-master, @tech-lead, @full-stack-developer, @qa-engineer, @devops-engineer (all Dept 10 Team B)

### Google Stitch MCP (`mcp__stitch__`)
**What:** AI design tool — generates high-fidelity UI screens from text prompts, exports HTML/CSS.
**Scope:** Available to @ux-designer and @visual-designer (Dept 14).
**When to use:** UI design for products, landing pages, app screens. Design → code pipeline.
**Key tools:**
- `create_project` — Create a Stitch project for a new product
- `generate_screen_from_text` — Generate UI screen from text prompt (takes a few minutes)
- `edit_screens` — Iterate on existing screens with text prompts
- `generate_variants` — Explore design variations (refine/explore/reimagine)
- `get_screen` — Retrieve screen details and code (HTML/CSS)
- `list_screens` — List all screens in a project
- `list_projects` — List all Stitch projects
- `get_project` — Get project details

**Agents with Stitch access:** @ux-designer (generates screens), @visual-designer (reviews for brand consistency), @full-stack-developer (converts designs to React)

**Stitch Skills (installed from google-labs-code/stitch-skills):**
| Skill | What it does | Assigned to |
|---|---|---|
| `stitch-design` | Unified design entry — prompt enhancement + design system + screen generation | @ux-designer |
| `stitch-design-md` | Extracts design system into DESIGN.md from Stitch projects | @visual-designer |
| `stitch-enhance-prompt` | Transforms vague UI ideas into optimized Stitch prompts | @ux-designer, @visual-designer |
| `stitch-react-components` | Converts Stitch designs → React components with AST validation | @full-stack-developer |
| `stitch-shadcn-ui` | shadcn/ui component integration and best practices | @full-stack-developer |
| `stitch-loop` | Iterative build loop — generate → integrate → next page | @ux-designer |
| `stitch-remotion` | Generate walkthrough videos from Stitch projects using Remotion | Video dept (planned) |

## CLI Tools (Live)

### Obsidian CLI (`obsidian`)
**What:** Programmatic access to the user's Obsidian vault — create, read, move, tag, search notes.
**Scope:** Available to any agent/skill with Bash access that works with vault content.
**When to use:** Processing vault inbox, creating journal entries, tagging notes, organizing vault files.
**Key commands:**
- `obsidian files folder="inbox" vault="vault"` — List files in a folder
- `obsidian read path="inbox/note.md" vault="vault"` — Read a note
- `obsidian create path="folder/note.md" content="..." vault="vault"` — Create a note
- `obsidian append path="note.md" content="..." vault="vault"` — Append to a note
- `obsidian move path="inbox/note.md" to="professional/notes/" vault="vault"` — Move a note
- `obsidian delete path="note.md" vault="vault"` — Delete a note
- `obsidian property:set path="note.md" name="tags" value="[tag1,tag2]" type=list vault="vault"` — Set frontmatter
- `obsidian search query="keyword" vault="vault"` — Search vault
- `obsidian tags vault="vault"` — List all tags
- `obsidian daily:append content="..." vault="vault"` — Append to daily note

**Vault name:** `vault` (at `/Users/ash/RennOS/vault/`)

**Skills using Obsidian CLI:** `/process-inbox`, `health/journal-prompt`, `growth/goal-setting`, `growth/reflection`

### GitHub CLI (`gh`)
**What:** GitHub operations — repos, branches, PRs, issues, releases, CI/CD.
**Scope:** Available to Dept 10 Team B dev agents with Bash access.
**When to use:** Code workflow — creating branches, opening PRs, code review, merging, deployments.
**Key commands:**
- `gh pr create` — Open a pull request
- `gh pr list` — List open PRs
- `gh pr diff <number>` — View PR changes
- `gh pr review <number> --approve` — Approve a PR
- `gh pr merge <number>` — Merge a PR
- `gh pr checks <number>` — Check CI status
- `gh release create` — Create a release
- `gh run list` — List CI workflow runs
- `gh issue list` — List issues

**Agents with GitHub access:** @tech-lead, @full-stack-developer, @qa-engineer, @devops-engineer

## Not Yet Connected (Planned)

| Tool | Purpose | When to add |
|---|---|---|
| Slack MCP | Team notifications, alerts | When the user uses Slack for business |
| Google Calendar MCP | Calendar integration for @schedule-manager | When calendar sync is needed |
| Notion MCP | Knowledge base integration | If the user uses Notion alongside Obsidian |
| Stripe MCP | Payment tracking for @income-tracker | When the user processes payments via Stripe |
