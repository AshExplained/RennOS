# Claude Code CLI -- Complete Feature Reference

> Extracted 2026-03-22 from code.claude.com/docs. Claude Code CLI only (no Agent SDK).

---

## TABLE OF CONTENTS

1. [Overview & Installation](#1-overview--installation)
2. [Memory: CLAUDE.md & Auto Memory](#2-memory-claudemd--auto-memory)
3. [Skills System](#3-skills-system)
4. [Sub-Agents](#4-sub-agents)
5. [MCP (Model Context Protocol)](#5-mcp-model-context-protocol)
6. [Settings & Configuration](#6-settings--configuration)
7. [Permissions System](#7-permissions-system)
8. [Hooks Guide](#8-hooks-guide)
9. [Hooks Reference](#9-hooks-reference)
10. [Interactive Mode](#10-interactive-mode)
11. [Common Workflows](#11-common-workflows)
12. [Checkpointing](#12-checkpointing)
13. [Scheduled Tasks](#13-scheduled-tasks)
14. [Agent Teams](#14-agent-teams)
15. [Tools Reference](#15-tools-reference)

---

## 1. OVERVIEW & INSTALLATION

### What Claude Code Is
An agentic coding tool that reads your codebase, edits files, runs commands, and integrates with development tools. Available in terminal, IDE, desktop app, and browser.

### Installation Methods

**Native Install (Recommended) -- auto-updates in background:**
```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex

# Windows CMD
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```
Windows requires Git for Windows.

**Homebrew (no auto-update):**
```bash
brew install --cask claude-code
# Update: brew upgrade claude-code
```

**WinGet (no auto-update):**
```powershell
winget install Anthropic.ClaudeCode
# Update: winget upgrade Anthropic.ClaudeCode
```

**Start:**
```bash
cd your-project
claude
```

### Available Surfaces
| Surface | Description |
|---------|-------------|
| **Terminal** | Full-featured CLI |
| **VS Code** | Extension with inline diffs, @-mentions, plan review |
| **JetBrains** | Plugin for IntelliJ, PyCharm, WebStorm, etc. |
| **Desktop App** | Standalone app, visual diffs, multiple sessions, scheduling |
| **Web** | Browser-based, no local setup, long-running tasks |

### Key Capabilities
- Build features, fix bugs in plain language
- Create commits and pull requests (`claude "commit my changes"`)
- Connect tools via MCP (Jira, Slack, Google Drive, etc.)
- Custom instructions via CLAUDE.md, skills, hooks
- Spawn agent teams for parallel work
- Pipe, script, automate with CLI (Unix philosophy)
- Work from anywhere: Remote Control, /teleport, /desktop, Slack @Claude

### Cross-Surface Integration Table
| Goal | Best Option |
|------|-------------|
| Continue session from phone/another device | Remote Control |
| Push events from Telegram/Discord/webhooks | Channels |
| Start task locally, continue on mobile | Web or iOS app |
| Automate PR reviews and issue triage | GitHub Actions or GitLab CI/CD |
| Auto code review on every PR | GitHub Code Review |
| Route bug reports from Slack to PRs | Slack integration |
| Debug live web apps | Chrome extension |

---

## 2. MEMORY: CLAUDE.md & AUTO MEMORY

### Two Memory Systems

| | CLAUDE.md files | Auto memory |
|---|---|---|
| **Who writes** | You | Claude |
| **Contains** | Instructions and rules | Learnings and patterns |
| **Scope** | Project, user, or org | Per working tree |
| **Loaded into** | Every session | Every session (first 200 lines) |
| **Use for** | Coding standards, workflows, architecture | Build commands, debugging insights |

### CLAUDE.md File Locations

| Scope | Location | Purpose | Shared with |
|-------|----------|---------|-------------|
| **Managed policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md` / Linux+WSL: `/etc/claude-code/CLAUDE.md` / Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | Organization-wide instructions | All org users |
| **Project** | `./CLAUDE.md` or `./.claude/CLAUDE.md` | Team-shared project instructions | Team via source control |
| **User** | `~/.claude/CLAUDE.md` | Personal preferences | Just you |

### How CLAUDE.md Files Load
- Walks UP the directory tree from CWD, loading each CLAUDE.md found
- Subdirectory CLAUDE.md files load on demand when Claude reads files there
- `/init` generates a starting CLAUDE.md (set `CLAUDE_CODE_NEW_INIT=true` for interactive multi-phase flow)

### Import Syntax
```text
See @README for project overview and @package.json for npm commands.
# Additional Instructions
- git workflow @docs/git-instructions.md
- @~/.claude/my-project-instructions.md   # personal, not checked in
```
- Relative paths resolve relative to the containing file
- Max import depth: 5 hops
- First encounter triggers approval dialog

### Organize Rules with `.claude/rules/`
```
your-project/
├── .claude/
│   ├── CLAUDE.md
│   └── rules/
│       ├── code-style.md
│       ├── testing.md
│       └── security.md
```

**Path-specific rules** (only load when Claude works with matching files):
```yaml
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
...
```

**Glob patterns:**
| Pattern | Matches |
|---------|---------|
| `**/*.ts` | All TypeScript files in any directory |
| `src/**/*` | All files under src/ |
| `*.md` | Markdown files in project root |
| `src/components/*.tsx` | React components in specific dir |

**User-level rules:** `~/.claude/rules/` -- apply to every project.

**Symlinks supported** in `.claude/rules/`.

### Load from Additional Directories
```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
```

### Exclude CLAUDE.md Files
```json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```
Managed policy CLAUDE.md files cannot be excluded.

### Auto Memory

**Enable/disable:**
```json
{ "autoMemoryEnabled": false }
```
Or env: `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`

**Storage:** `~/.claude/projects/<project>/memory/`
- `MEMORY.md` -- index, first 200 lines loaded every session
- Topic files (e.g., `debugging.md`) -- loaded on demand
- All worktrees/subdirs in same git repo share one memory directory

**Custom directory:**
```json
{ "autoMemoryDirectory": "~/my-custom-memory-dir" }
```

### Commands
- `/memory` -- browse all loaded files, toggle auto memory, open memory folder
- `/init` -- generate or improve CLAUDE.md

---

## 3. SKILLS SYSTEM

### What Skills Are
SKILL.md files with instructions that Claude adds to its toolkit. Claude uses them when relevant or you invoke directly with `/skill-name`.

**Custom commands merged into skills:** `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`. Skills take precedence if both exist.

### Bundled Skills

| Skill | Purpose |
|-------|---------|
| `/batch <instruction>` | Orchestrate large-scale parallel changes. Spawns one agent per unit in isolated git worktrees. |
| `/claude-api` | Load Claude API reference for your language. Auto-activates on anthropic imports. |
| `/debug [description]` | Troubleshoot current session by reading debug log. |
| `/loop [interval] <prompt>` | Run prompt repeatedly on interval. E.g. `/loop 5m check deploy` |
| `/simplify [focus]` | Review recently changed files for reuse/quality/efficiency. Spawns 3 review agents. |

### Skill File Locations

| Location | Path | Applies to |
|----------|------|------------|
| Enterprise | Managed settings | All users in org |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | All your projects |
| Project | `.claude/skills/<skill-name>/SKILL.md` | This project only |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Where plugin is enabled |

Priority: enterprise > personal > project. Plugin skills use `plugin-name:skill-name` namespace.

### Skill Directory Structure
```
my-skill/
├── SKILL.md           # Main instructions (required)
├── template.md        # Template for Claude to fill in
├── examples/
│   └── sample.md
└── scripts/
    └── validate.sh
```

### Frontmatter Reference

```yaml
---
name: my-skill
description: What this skill does
argument-hint: "[issue-number]"
disable-model-invocation: true
user-invocable: false
allowed-tools: Read, Grep, Glob
model: sonnet
effort: high
context: fork
agent: Explore
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
---
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | No | Display name. Lowercase letters, numbers, hyphens (max 64 chars) |
| `description` | Recommended | When to use it. Claude uses this for auto-loading |
| `argument-hint` | No | Hint shown during autocomplete |
| `disable-model-invocation` | No | `true` = only user can invoke (not Claude). Default: false |
| `user-invocable` | No | `false` = hidden from `/` menu. Default: true |
| `allowed-tools` | No | Tools without permission prompts when skill is active |
| `model` | No | Model to use when skill is active |
| `effort` | No | `low`, `medium`, `high`, `max` (Opus 4.6 only) |
| `context` | No | `fork` = run in forked subagent context |
| `agent` | No | Subagent type when `context: fork` (e.g., `Explore`, `Plan`, `general-purpose`) |
| `hooks` | No | Hooks scoped to skill's lifecycle |

### String Substitutions

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed when invoking |
| `$ARGUMENTS[N]` or `$N` | Specific argument by 0-based index |
| `${CLAUDE_SESSION_ID}` | Current session ID |
| `${CLAUDE_SKILL_DIR}` | Directory containing the SKILL.md file |

### Invocation Control

| Frontmatter | You can invoke | Claude can invoke |
|-------------|---------------|-------------------|
| (default) | Yes | Yes |
| `disable-model-invocation: true` | Yes | No |
| `user-invocable: false` | No | Yes |

### Dynamic Context Injection
```yaml
## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
```
Commands run BEFORE Claude sees anything. Output replaces the placeholder.

### Run in Subagent
```yaml
---
context: fork
agent: Explore
---
Research $ARGUMENTS thoroughly...
```

### Permission Control for Skills
```text
# Allow only specific skills
Skill(commit)
Skill(review-pr *)

# Deny specific skills
Skill(deploy *)
```

### Skill Description Budget
Scales at 2% of context window, fallback 16,000 chars. Override: `SLASH_COMMAND_TOOL_CHAR_BUDGET` env var.

### Enable Extended Thinking in a Skill
Include the word "ultrathink" anywhere in skill content.

---

## 4. SUB-AGENTS

### What Sub-Agents Are
Specialized AI assistants running in their own context window with custom system prompt, specific tool access, and independent permissions.

### Built-in Sub-Agents

| Agent | Model | Tools | Purpose |
|-------|-------|-------|---------|
| **Explore** | Haiku | Read-only | File discovery, code search, codebase exploration |
| **Plan** | Inherits | Read-only | Codebase research for planning (used in plan mode) |
| **General-purpose** | Inherits | All | Complex research, multi-step operations |
| **Bash** | Inherits | Terminal commands | Running commands in separate context |
| **statusline-setup** | Sonnet | - | When you run `/statusline` |
| **Claude Code Guide** | Haiku | - | Questions about Claude Code features |

Explore uses thoroughness levels: **quick**, **medium**, **very thorough**.

### Sub-Agent Scope & Priority

| Location | Scope | Priority |
|----------|-------|----------|
| `--agents` CLI flag | Current session | 1 (highest) |
| `.claude/agents/` | Current project | 2 |
| `~/.claude/agents/` | All your projects | 3 |
| Plugin's `agents/` directory | Where plugin is enabled | 4 (lowest) |

### Sub-Agent File Format
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
disallowedTools: Write, Edit
model: sonnet
permissionMode: default
maxTurns: 20
skills:
  - api-conventions
mcpServers:
  - playwright:
      type: stdio
      command: npx
      args: ["-y", "@playwright/mcp@latest"]
  - github
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/validate.sh"
memory: user
background: false
effort: high
isolation: worktree
---

System prompt content goes here...
```

### All Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier, lowercase + hyphens |
| `description` | Yes | When Claude should delegate |
| `tools` | No | Tools the subagent can use. Inherits all if omitted |
| `disallowedTools` | No | Tools to deny |
| `model` | No | `sonnet`, `opus`, `haiku`, full model ID, or `inherit` (default) |
| `permissionMode` | No | `default`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan` |
| `maxTurns` | No | Max agentic turns before stop |
| `skills` | No | Skills preloaded into context at startup |
| `mcpServers` | No | MCP servers (inline definitions or name references) |
| `hooks` | No | Lifecycle hooks scoped to this subagent |
| `memory` | No | `user`, `project`, or `local` |
| `background` | No | `true` = always run as background task |
| `effort` | No | `low`, `medium`, `high`, `max` (Opus 4.6 only) |
| `isolation` | No | `worktree` = run in temp git worktree |

### Memory Scopes

| Scope | Location |
|-------|----------|
| `user` | `~/.claude/agent-memory/<name>/` |
| `project` | `.claude/agent-memory/<name>/` |
| `local` | `.claude/agent-memory-local/<name>/` |

### CLI-Defined Sub-Agents
```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer.",
    "prompt": "You are a senior code reviewer.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

### Invoke Sub-Agents

1. **Natural language**: Name the subagent in your prompt
2. **@-mention**: `@"code-reviewer (agent)" look at the auth changes`
3. **Session-wide**: `claude --agent code-reviewer` or set `"agent": "code-reviewer"` in settings

### Foreground vs Background

- **Foreground**: Blocks main conversation. Permission prompts pass through.
- **Background**: Runs concurrently. Permissions pre-approved before launch. Auto-denies anything not pre-approved.
- Press **Ctrl+B** to background a running task
- Disable: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`

### Restrict Spawning
```yaml
tools: Agent(worker, researcher), Read, Bash
```
Only `worker` and `researcher` can be spawned. Omitting `Agent` entirely prevents all subagent spawning.

### Disable Specific Sub-Agents
```json
{
  "permissions": {
    "deny": ["Agent(Explore)", "Agent(my-custom-agent)"]
  }
}
```

### Resume Sub-Agents
Claude uses `SendMessage` with the agent's ID to resume a completed subagent. Transcripts: `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`

### Auto-Compaction
Triggers at ~95% capacity. Override: `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` (e.g., `50`).

---

## 5. MCP (MODEL CONTEXT PROTOCOL)

### What MCP Does
Connects Claude Code to external tools and data sources via the open MCP standard.

### Installation Commands

**HTTP server (recommended for remote):**
```bash
claude mcp add --transport http <name> <url>
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

**SSE server (deprecated, use HTTP):**
```bash
claude mcp add --transport sse <name> <url>
```

**Stdio server (local):**
```bash
claude mcp add --transport stdio --env KEY=value <name> -- <command> [args...]
claude mcp add --transport stdio --env AIRTABLE_API_KEY=KEY airtable -- npx -y airtable-mcp-server
```

**Important:** Options (`--transport`, `--env`, `--scope`, `--header`) must come BEFORE the server name. `--` separates name from command.

### Management Commands
```bash
claude mcp list                       # List all servers
claude mcp get github                 # Details for specific server
claude mcp remove github              # Remove a server
claude mcp add-from-claude-desktop    # Import from Claude Desktop
claude mcp add-json <name> '<json>'   # Add from JSON config
claude mcp reset-project-choices      # Reset project server approvals
claude mcp serve                      # Run Claude Code AS an MCP server
/mcp                                  # Check status, authenticate (in session)
```

### Scope Flags
| Scope | Flag | Storage | Shared |
|-------|------|---------|--------|
| `local` (default) | `--scope local` | `~/.claude.json` | No |
| `project` | `--scope project` | `.mcp.json` (version control) | Yes |
| `user` | `--scope user` | `~/.claude.json` | No (cross-project) |

### `.mcp.json` Format
```json
{
  "mcpServers": {
    "server-name": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

### Environment Variable Expansion in `.mcp.json`
- `${VAR}` -- expands to value
- `${VAR:-default}` -- with fallback
- Works in: `command`, `args`, `env`, `url`, `headers`

### OAuth Authentication
```bash
claude mcp add --transport http \
  --client-id your-id --client-secret --callback-port 8080 \
  my-server https://mcp.example.com/mcp
```
- `--callback-port` fixes the OAuth redirect port
- `--client-id` / `--client-secret` for pre-configured OAuth
- `MCP_CLIENT_SECRET` env var for CI
- `authServerMetadataUrl` in oauth config to override discovery

### MCP Resources
Type `@` to see resources from connected servers:
```text
@github:issue://123
@docs:file://api/authentication
@postgres:schema://users
```

### MCP Prompts as Commands
```text
/mcp__github__list_prs
/mcp__github__pr_review 456
```

### MCP Tool Search
Auto-enabled when MCP tool descriptions exceed 10% of context window.

| `ENABLE_TOOL_SEARCH` | Behavior |
|---|---|
| (unset) | Enabled by default. Disabled for non-first-party `ANTHROPIC_BASE_URL` |
| `true` | Always enabled |
| `auto` | Activates when MCP tools exceed 10% of context |
| `auto:<N>` | Custom threshold percentage |
| `false` | Disabled, all tools loaded upfront |

### Dynamic Tool Updates
Supports MCP `list_changed` notifications for live tool updates.

### Channels
MCP servers can push messages into sessions via `claude/channel` capability + `--channels` flag.

### Output Limits
- Warning at 10,000 tokens. Max default: 25,000 tokens.
- Override: `MAX_MCP_OUTPUT_TOKENS=50000`
- Startup timeout: `MCP_TIMEOUT=10000` (ms)

### Managed MCP Configuration

**Option 1: `managed-mcp.json`** (exclusive control):
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux/WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

**Option 2: Allowlist/Denylist** in managed settings:
```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverCommand": ["npx", "-y", "@modelcontextprotocol/server-filesystem"] },
    { "serverUrl": "https://mcp.company.com/*" }
  ],
  "deniedMcpServers": [
    { "serverName": "dangerous-server" }
  ]
}
```
Each entry must have exactly ONE of: `serverName`, `serverCommand`, `serverUrl`.

### Claude Code as MCP Server
```bash
claude mcp serve
```
Exposes Claude Code's tools (View, Edit, LS, etc.) to other MCP clients.

---

## 6. SETTINGS & CONFIGURATION

### Configuration Scopes

| Scope | Location | Who it affects | Shared? |
|-------|----------|---------------|---------|
| **Managed** | Server/plist/registry/`managed-settings.json` | All machine users | Yes (by IT) |
| **User** | `~/.claude/` | You, all projects | No |
| **Project** | `.claude/` in repo | All collaborators | Yes (git) |
| **Local** | `.claude/settings.local.json` | You, this repo only | No (gitignored) |

**Precedence:** Managed (highest) > CLI args > Local > Project > User (lowest)

### Settings Files Locations

| Feature | User | Project | Local |
|---------|------|---------|-------|
| Settings | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| Sub-Agents | `~/.claude/agents/` | `.claude/agents/` | -- |
| MCP servers | `~/.claude.json` | `.mcp.json` | `~/.claude.json` (per-project) |
| Plugins | `~/.claude/settings.json` | `.claude/settings.json` | `.claude/settings.local.json` |
| CLAUDE.md | `~/.claude/CLAUDE.md` | `CLAUDE.md` or `.claude/CLAUDE.md` | -- |

### Managed Settings Delivery
- **Server-managed**: Claude.ai admin console
- **MDM/OS-level**: macOS plist `com.anthropic.claudecode`, Windows registry `HKLM\SOFTWARE\Policies\ClaudeCode`
- **File-based**: `managed-settings.json` at:
  - macOS: `/Library/Application Support/ClaudeCode/`
  - Linux/WSL: `/etc/claude-code/`
  - Windows: `C:\Program Files\ClaudeCode\`

### JSON Schema
```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json"
}
```

### All Available Settings

| Key | Description | Example |
|-----|-------------|---------|
| `apiKeyHelper` | Script to generate auth value | `/bin/generate_temp_api_key.sh` |
| `autoMemoryDirectory` | Custom auto memory path | `"~/my-memory-dir"` |
| `autoMemoryEnabled` | Toggle auto memory | `false` |
| `cleanupPeriodDays` | Days before sessions deleted (default: 30). `0` = disable persistence | `20` |
| `companyAnnouncements` | Startup announcement(s) | `["Welcome!"]` |
| `env` | Environment variables for every session | `{"FOO": "bar"}` |
| `attribution` | Customize git commit/PR attribution | `{"commit": "...", "pr": ""}` |
| `includeCoAuthoredBy` | (Deprecated) Co-authored-by byline | `false` |
| `includeGitInstructions` | Include git instructions in system prompt | `false` |
| `permissions` | Permission rules object | See permissions section |
| `hooks` | Lifecycle hooks | See hooks section |
| `disableAllHooks` | Disable all hooks + status line | `true` |
| `allowManagedHooksOnly` | (Managed) Only managed/SDK hooks | `true` |
| `allowedHttpHookUrls` | URL allowlist for HTTP hooks | `["https://hooks.example.com/*"]` |
| `httpHookAllowedEnvVars` | Env var allowlist for HTTP hook headers | `["MY_TOKEN"]` |
| `allowManagedPermissionRulesOnly` | (Managed) Only managed permission rules | `true` |
| `allowManagedMcpServersOnly` | (Managed) Only managed MCP allowlist | `true` |
| `model` | Override default model | `"claude-sonnet-4-6"` |
| `availableModels` | Restrict model selection | `["sonnet", "haiku"]` |
| `modelOverrides` | Map model IDs to provider-specific IDs | `{"claude-opus-4-6": "arn:..."}` |
| `effortLevel` | Persist effort level | `"low"`, `"medium"`, `"high"` |
| `otelHeadersHelper` | Script for dynamic OpenTelemetry headers | `/bin/gen_otel.sh` |
| `statusLine` | Custom status line | `{"type": "command", "command": "..."}` |
| `fileSuggestion` | Custom @ file autocomplete script | `{"type": "command", "command": "..."}` |
| `respectGitignore` | @ picker respects .gitignore (default: true) | `false` |
| `outputStyle` | Adjust system prompt output style | `"Explanatory"` |
| `agent` | Run main thread as named subagent | `"code-reviewer"` |
| `forceLoginMethod` | Restrict login to `claudeai` or `console` | `"claudeai"` |
| `forceLoginOrgUUID` | Auto-select org during login | `"xxxxxxxx-..."` |
| `enableAllProjectMcpServers` | Auto-approve all project `.mcp.json` servers | `true` |
| `enabledMcpjsonServers` | Approve specific `.mcp.json` servers | `["memory", "github"]` |
| `disabledMcpjsonServers` | Reject specific `.mcp.json` servers | `["filesystem"]` |
| `channelsEnabled` | (Managed) Allow channels | `true` |
| `allowedMcpServers` | MCP server allowlist | `[{"serverName": "github"}]` |
| `deniedMcpServers` | MCP server denylist | `[{"serverName": "fs"}]` |
| `strictKnownMarketplaces` | (Managed) Plugin marketplace allowlist | `[{"source": "github", "repo": "..."}]` |
| `blockedMarketplaces` | (Managed) Marketplace blocklist | `[{"source": "github", "repo": "..."}]` |
| `pluginTrustMessage` | (Managed) Custom plugin trust warning | `"Approved by IT"` |
| `awsAuthRefresh` | Custom AWS auth refresh script | `"aws sso login ..."` |
| `awsCredentialExport` | Custom AWS credential export script | `/bin/gen_aws.sh` |
| `alwaysThinkingEnabled` | Enable extended thinking by default | `true` |
| `plansDirectory` | Where plan files are stored | `"./plans"` |
| `spinnerVerbs` | Custom spinner verbs | `{"mode": "append", "verbs": ["Pondering"]}` |
| `language` | Preferred response language | `"japanese"` |
| `voiceEnabled` | Push-to-talk voice dictation | `true` |
| `autoUpdatesChannel` | `"stable"` or `"latest"` (default) | `"stable"` |
| `spinnerTipsEnabled` | Show tips in spinner (default: true) | `false` |
| `spinnerTipsOverride` | Custom spinner tips | `{"excludeDefault": true, "tips": [...]}` |
| `prefersReducedMotion` | Reduce UI animations | `true` |
| `fastModePerSessionOptIn` | Fast mode doesn't persist across sessions | `true` |
| `teammateMode` | Agent team display: `auto`, `in-process`, `tmux` | `"in-process"` |
| `feedbackSurveyRate` | Survey probability 0-1 | `0.05` |

### Global Config Settings (in `~/.claude.json`, NOT `settings.json`)

| Key | Description |
|-----|-------------|
| `autoConnectIde` | Auto-connect to IDE from external terminal |
| `autoInstallIdeExtension` | Auto-install VS Code extension |
| `editorMode` | `"normal"` or `"vim"` |
| `showTurnDuration` | Show turn duration messages |
| `terminalProgressBarEnabled` | Terminal progress bar |

### Worktree Settings

| Key | Description | Example |
|-----|-------------|---------|
| `worktree.symlinkDirectories` | Dirs to symlink into worktrees | `["node_modules", ".cache"]` |
| `worktree.sparsePaths` | Dirs for sparse checkout | `["packages/my-app"]` |

### Sandbox Settings

| Key | Description |
|-----|-------------|
| `sandbox.enabled` | Enable bash sandboxing |
| `sandbox.autoAllowBashIfSandboxed` | Auto-approve bash when sandboxed (default: true) |
| `sandbox.excludedCommands` | Commands that run outside sandbox |
| `sandbox.allowUnsandboxedCommands` | Allow `dangerouslyDisableSandbox` parameter |
| `sandbox.filesystem.allowWrite` | Additional writable paths |
| `sandbox.filesystem.denyWrite` | Blocked write paths |
| `sandbox.filesystem.denyRead` | Blocked read paths |
| `sandbox.filesystem.allowRead` | Re-allow reading within denyRead |
| `sandbox.filesystem.allowManagedReadPathsOnly` | (Managed) Only managed allowRead |
| `sandbox.network.allowUnixSockets` | Accessible Unix socket paths |
| `sandbox.network.allowAllUnixSockets` | Allow all Unix sockets |
| `sandbox.network.allowLocalBinding` | Allow localhost port binding (macOS) |
| `sandbox.network.allowedDomains` | Allowed outbound domains |
| `sandbox.network.allowManagedDomainsOnly` | (Managed) Only managed domains |
| `sandbox.network.httpProxyPort` | Custom HTTP proxy port |
| `sandbox.network.socksProxyPort` | Custom SOCKS5 proxy port |
| `sandbox.enableWeakerNestedSandbox` | Weaker sandbox for Docker (Linux/WSL2) |
| `sandbox.enableWeakerNetworkIsolation` | Allow TLS trust service (macOS) |

### Sandbox Path Prefixes

| Prefix | Meaning |
|--------|---------|
| `/` | Absolute from filesystem root |
| `~/` | Relative to home directory |
| `./` or no prefix | Relative to project root (project settings) or `~/.claude` (user) |

### Attribution Settings
```json
{
  "attribution": {
    "commit": "Generated with Claude Code",
    "pr": ""
  }
}
```

---

## 7. PERMISSIONS SYSTEM

### Permission Tiers

| Tool type | Example | Approval required | "Don't ask again" |
|-----------|---------|-------------------|--------------------|
| Read-only | File reads, Grep | No | N/A |
| Bash commands | Shell execution | Yes | Permanently per project+command |
| File modification | Edit/write | Yes | Until session end |

### Permission Modes

| Mode | Description |
|------|-------------|
| `default` | Standard: prompts on first use |
| `acceptEdits` | Auto-accept file edits for session |
| `plan` | Read-only analysis, no modifications |
| `dontAsk` | Auto-deny unless pre-approved |
| `bypassPermissions` | Skip prompts (except .git/.claude/.vscode/.idea writes) |

### Rule Evaluation Order
**deny -> ask -> allow** (first match wins, deny always takes precedence)

### Permission Rule Syntax

**Basic:**
| Rule | Effect |
|------|--------|
| `Bash` | All Bash commands |
| `Bash(npm run build)` | Exact command |
| `Bash(npm run *)` | Wildcard prefix |
| `Read(./.env)` | Specific file |
| `WebFetch(domain:example.com)` | Domain restriction |

**Bash wildcards:**
- `Bash(ls *)` matches `ls -la` but NOT `lsof` (space before `*` = word boundary)
- `Bash(ls*)` matches both `ls -la` AND `lsof`
- Claude is aware of shell operators like `&&`

**Read and Edit patterns (gitignore spec):**
| Pattern | Meaning |
|---------|---------|
| `//path` | Absolute from filesystem root |
| `~/path` | From home directory |
| `/path` | Relative to PROJECT ROOT |
| `path` or `./path` | Relative to current directory |

Windows: paths normalized to POSIX (`C:\Users\alice` -> `/c/Users/alice`).

**MCP rules:**
- `mcp__puppeteer` -- all tools from puppeteer server
- `mcp__puppeteer__puppeteer_navigate` -- specific tool

**Agent rules:**
- `Agent(Explore)` -- specific subagent
- `Agent(my-custom-agent)` -- custom subagent

### Working Directories
- `--add-dir <path>` at startup
- `/add-dir` during session
- `additionalDirectories` in settings

### Managed-Only Settings

| Setting | Description |
|---------|-------------|
| `disableBypassPermissionsMode` | `"disable"` prevents bypass mode |
| `allowManagedPermissionRulesOnly` | Only managed permission rules |
| `allowManagedHooksOnly` | Only managed + SDK hooks |
| `allowManagedMcpServersOnly` | Only managed MCP allowlist |
| `blockedMarketplaces` | Marketplace blocklist |
| `sandbox.network.allowManagedDomainsOnly` | Only managed domains |
| `sandbox.filesystem.allowManagedReadPathsOnly` | Only managed read paths |
| `strictKnownMarketplaces` | Allowed marketplaces |

---

## 8. HOOKS GUIDE

### What Hooks Are
User-defined shell commands (or HTTP/prompt/agent handlers) that execute at specific lifecycle points. Deterministic control -- actions always happen rather than relying on LLM choice.

### Hook Types
| Type | Description |
|------|-------------|
| `command` | Run a shell command |
| `http` | POST event data to URL |
| `prompt` | Single-turn LLM evaluation |
| `agent` | Multi-turn verification with tool access |

### Hook Configuration Location

| Location | Scope |
|----------|-------|
| `~/.claude/settings.json` | All projects |
| `.claude/settings.json` | Single project (shareable) |
| `.claude/settings.local.json` | Single project (local) |
| Managed policy | Organization-wide |
| Plugin `hooks/hooks.json` | When plugin enabled |
| Skill/agent frontmatter | While component active |

### Key Use Cases

**Desktop notification:**
```json
{
  "hooks": {
    "Notification": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Claude needs attention\" with title \"Claude Code\"'"
      }]
    }]
  }
}
```

**Auto-format after edits:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|Write",
      "hooks": [{
        "type": "command",
        "command": "jq -r '.tool_input.file_path' | xargs npx prettier --write"
      }]
    }]
  }
}
```

**Re-inject context after compaction:**
```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "compact",
      "hooks": [{
        "type": "command",
        "command": "echo 'Reminder: use Bun, not npm.'"
      }]
    }]
  }
}
```

**Auto-approve specific permission prompts:**
```json
{
  "hooks": {
    "PermissionRequest": [{
      "matcher": "ExitPlanMode",
      "hooks": [{
        "type": "command",
        "command": "echo '{\"hookSpecificOutput\": {\"hookEventName\": \"PermissionRequest\", \"decision\": {\"behavior\": \"allow\"}}}'"
      }]
    }]
  }
}
```

**Prompt-based hook (LLM evaluates):**
```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "prompt",
        "prompt": "Check if all tasks are complete. If not, respond with {\"ok\": false, \"reason\": \"what remains\"}."
      }]
    }]
  }
}
```

**Agent-based hook (multi-turn with tools):**
```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "agent",
        "prompt": "Verify all unit tests pass. Run the test suite. $ARGUMENTS",
        "timeout": 120
      }]
    }]
  }
}
```

**HTTP hook:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "hooks": [{
        "type": "http",
        "url": "http://localhost:8080/hooks/tool-use",
        "headers": { "Authorization": "Bearer $MY_TOKEN" },
        "allowedEnvVars": ["MY_TOKEN"]
      }]
    }]
  }
}
```

### Exit Codes
| Code | Meaning |
|------|---------|
| **0** | Proceed. stdout added to context (for UserPromptSubmit, SessionStart) |
| **2** | Block action. stderr = feedback to Claude |
| **Other** | Proceed. stderr logged but not shown to Claude |

### Environment Variables for Hook Scripts
- `$CLAUDE_PROJECT_DIR` -- project root
- `${CLAUDE_PLUGIN_ROOT}` -- plugin installation dir
- `${CLAUDE_PLUGIN_DATA}` -- plugin data dir

### Disable All Hooks
```json
{ "disableAllHooks": true }
```

---

## 9. HOOKS REFERENCE

### All Hook Events

| Event | When | Can Block? | Matcher |
|-------|------|-----------|---------|
| `SessionStart` | Session begins/resumes | No | `startup`, `resume`, `clear`, `compact` |
| `UserPromptSubmit` | Prompt submitted, before processing | Yes | None |
| `PreToolUse` | Before tool executes | Yes | Tool name |
| `PermissionRequest` | Permission dialog appears | Yes | Tool name |
| `PostToolUse` | After tool succeeds | No* | Tool name |
| `PostToolUseFailure` | After tool fails | No | Tool name |
| `Notification` | Notification sent | No | `permission_prompt`, `idle_prompt`, `auth_success`, `elicitation_dialog` |
| `SubagentStart` | Subagent spawned | No | Agent type |
| `SubagentStop` | Subagent finishes | Yes | Agent type |
| `Stop` | Claude finishes responding | Yes | None |
| `StopFailure` | Turn ends from API error | No | `rate_limit`, `authentication_failed`, `billing_error`, `invalid_request`, `server_error`, `max_output_tokens`, `unknown` |
| `TeammateIdle` | Agent team teammate going idle | Yes | None |
| `TaskCompleted` | Task being marked complete | Yes | None |
| `InstructionsLoaded` | CLAUDE.md/rules loaded | No | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` |
| `ConfigChange` | Config file changes | Yes | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| `WorktreeCreate` | Worktree being created | Yes | None |
| `WorktreeRemove` | Worktree being removed | No | None |
| `PreCompact` | Before compaction | No | `manual`, `auto` |
| `PostCompact` | After compaction | No | `manual`, `auto` |
| `Elicitation` | MCP server requests input | Yes | MCP server name |
| `ElicitationResult` | User responds to elicitation | Yes | MCP server name |
| `SessionEnd` | Session terminates | No | `clear`, `resume`, `logout`, `prompt_input_exit`, `bypass_permissions_disabled`, `other` |

### Common Input Fields (All Events)
```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "EventName"
}
```

### Hook Handler Common Fields

| Field | Required | Description |
|-------|----------|-------------|
| `type` | Yes | `command`, `http`, `prompt`, `agent` |
| `timeout` | No | Seconds. Defaults: 600 (command), 30 (prompt), 60 (agent) |
| `statusMessage` | No | Custom spinner message |
| `once` | No | Run only once per session (skills only) |

### Command Hook Fields
| Field | Description |
|-------|-------------|
| `command` | Shell command to execute |
| `async` | `true` = run in background without blocking |

### HTTP Hook Fields
| Field | Description |
|-------|-------------|
| `url` | URL to POST to |
| `headers` | Additional headers with `$VAR_NAME` interpolation |
| `allowedEnvVars` | Env vars allowed for header interpolation |

### Prompt Hook Fields
| Field | Description |
|-------|-------------|
| `prompt` | Prompt text. `$ARGUMENTS` for input JSON |
| `model` | Model for evaluation (defaults to fast model) |

### Agent Hook Fields
| Field | Description |
|-------|-------------|
| `prompt` | Prompt text. `$ARGUMENTS` for input JSON |
| `model` | Model for evaluation |

### JSON Output Structure
```json
{
  "continue": true,
  "stopReason": "message when continue: false",
  "suppressOutput": false,
  "systemMessage": "warning to user",
  "hookSpecificOutput": { ... }
}
```

### PreToolUse Decision Output
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow|deny|ask",
    "permissionDecisionReason": "reason text",
    "updatedInput": { "command": "npm run lint" },
    "additionalContext": "context string"
  }
}
```

### PermissionRequest Decision Output
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": { ... },
      "updatedPermissions": [
        { "type": "setMode", "mode": "acceptEdits", "destination": "session" }
      ],
      "message": "deny reason"
    }
  }
}
```

### SessionStart -- Persist Environment Variables
```bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=production' >> "$CLAUDE_ENV_FILE"
fi
```

### SessionEnd Timeout
Default 1.5 seconds. Override: `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`

---

## 10. INTERACTIVE MODE

### Keyboard Shortcuts -- General

| Shortcut | Description |
|----------|-------------|
| `Ctrl+C` | Cancel current input/generation |
| `Ctrl+F` | Kill all background agents (press twice within 3s) |
| `Ctrl+D` | Exit session |
| `Ctrl+G` | Open in default text editor |
| `Ctrl+L` | Clear terminal screen (keeps history) |
| `Ctrl+O` | Toggle verbose output |
| `Ctrl+R` | Reverse search command history |
| `Ctrl+V` / `Cmd+V` / `Alt+V` | Paste image from clipboard |
| `Ctrl+B` | Background running tasks |
| `Ctrl+T` | Toggle task list |
| `Esc` + `Esc` | Rewind or summarize |
| `Shift+Tab` | Toggle permission modes (Normal -> Accept Edits -> Plan) |
| `Alt+P` / `Option+P` | Switch model |
| `Alt+T` / `Option+T` | Toggle extended thinking |

### Text Editing

| Shortcut | Description |
|----------|-------------|
| `Ctrl+K` | Delete to end of line |
| `Ctrl+U` | Delete entire line |
| `Ctrl+Y` | Paste deleted text |
| `Alt+Y` | Cycle paste history |
| `Alt+B` | Move cursor back one word |
| `Alt+F` | Move cursor forward one word |

### Multiline Input

| Method | Shortcut |
|--------|----------|
| Quick escape | `\` + `Enter` |
| macOS | `Option+Enter` |
| Shift+Enter | Works in iTerm2, WezTerm, Ghostty, Kitty |
| Control sequence | `Ctrl+J` |
| Paste mode | Paste directly |

### Quick Commands

| Prefix | Description |
|--------|-------------|
| `/` | Command or skill |
| `!` | Bash mode (run directly, add output to session) |
| `@` | File path mention (autocomplete) |
| Hold `Space` | Push-to-talk voice dictation |

### Vim Mode
Enable with `/vim` or via `/config`. Full vim keybindings: NORMAL/INSERT modes, h/j/k/l navigation, d/c/y operators, text objects (iw, aw, i", etc.).

### `/btw` -- Side Questions
Quick question without adding to conversation history. Runs independently (even while Claude is working). No tool access. Single response. Uses prompt cache (low cost).

### Task List
`Ctrl+T` toggles. Shows up to 10 tasks. Persists across compactions.
Share across sessions: `CLAUDE_CODE_TASK_LIST_ID=my-project claude`

### PR Review Status
Clickable PR link in footer with colored underline:
- Green: approved
- Yellow: pending
- Red: changes requested
- Gray: draft
- Purple: merged
Updates every 60 seconds. Requires `gh` CLI.

### Prompt Suggestions
Grayed-out suggestions based on git history and conversation. Press **Tab** to accept, **Enter** to accept and submit.
Disable: `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false`

### Background Bash Commands
- Prompt Claude to run in background, or press `Ctrl+B`
- Output buffered, retrieved via TaskOutput tool
- Auto-terminated at 5GB output
- Disable: `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1`

### Bash Mode (`!` prefix)
```bash
! npm test
! git status
```
Adds command + output to context. Supports `Ctrl+B` backgrounding. Tab autocomplete from history.

---

## 11. COMMON WORKFLOWS

### Understand Codebases
```text
give me an overview of this codebase
explain the main architecture patterns used here
find the files that handle user authentication
trace the login process from front-end to database
```

### Fix Bugs
```text
I'm seeing an error when I run npm test
suggest a few ways to fix the @ts-ignore in user.ts
update user.ts to add the null check you suggested
```

### Refactor Code
```text
find deprecated API usage in our codebase
suggest how to refactor utils.js to use modern JavaScript features
refactor utils.js to use ES2024 features while maintaining the same behavior
run tests for the refactored code
```

### Plan Mode
```bash
claude --permission-mode plan
# Or headless:
claude --permission-mode plan -p "Analyze the auth system"
```
Toggle with `Shift+Tab`. Plan mode = read-only analysis. Claude uses `AskUserQuestion` to gather requirements. Accepting a plan auto-names the session.

### Extended Thinking
Enabled by default. Control:
- `/effort` or `CLAUDE_CODE_EFFORT_LEVEL` env var
- "ultrathink" keyword in prompt = high effort for that turn
- `Alt+T` / `Option+T` toggle
- `/config` for global default
- `MAX_THINKING_TOKENS` env var to limit budget
- `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` to revert to fixed budget

### Work with Tests
```text
find functions in NotificationsService.swift not covered by tests
add tests for the notification service
add test cases for edge conditions
run the new tests and fix any failures
```

### Create Pull Requests
```text
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context
```
Creating PR with `gh pr create` auto-links session to that PR. Resume with `claude --from-pr <number>`.

### Reference Files
```text
Explain the logic in @src/utils/auth.js
What's the structure of @src/components?
Show me data from @github:repos/owner/repo/issues
```

### Work with Images
- Drag and drop, Ctrl+V paste, or provide path
- Cmd+Click image references to open

### Output Format Control
```bash
cat data.txt | claude -p 'summarize' --output-format text > summary.txt
cat code.py | claude -p 'analyze bugs' --output-format json > analysis.json
cat log.txt | claude -p 'parse errors' --output-format stream-json
```

### Resume Sessions
```bash
claude --continue           # Most recent in current dir
claude --resume             # Picker or by name
claude --resume auth-refactor
claude --from-pr 123        # Resume by PR number
claude -n auth-refactor     # Name at startup
/rename auth-refactor       # Name during session
/resume                     # Switch sessions mid-session
```

**Session picker shortcuts:**
| Key | Action |
|-----|--------|
| `P` | Preview session |
| `R` | Rename session |
| `/` | Search/filter |
| `A` | Toggle current dir / all projects |
| `B` | Filter to current git branch |

### Git Worktrees
```bash
claude --worktree feature-auth    # Named worktree
claude --worktree                 # Auto-generated name
claude -w                         # Short flag
```
Location: `<repo>/.claude/worktrees/<name>`. Branch: `worktree-<name>`.

Subagent worktrees: `isolation: worktree` in agent frontmatter.

Cleanup: no changes = auto-removed. Changes = prompted to keep/remove.

### Unix-Style Piping
```bash
cat build-error.txt | claude -p 'explain root cause' > output.txt
git diff main --name-only | claude -p "review for security issues"
tail -200 app.log | claude -p "Slack me if you see anomalies"
```

---

## 12. CHECKPOINTING

### How It Works
- Every user prompt creates a new checkpoint
- Tracks all file edits by Claude's editing tools
- Persists across sessions
- Auto-cleaned after 30 days (configurable via `cleanupPeriodDays`)

### Rewind Menu
Press `Esc` + `Esc` or use `/rewind`.

**Actions:**
| Action | Description |
|--------|-------------|
| **Restore code and conversation** | Revert both to that point |
| **Restore conversation** | Rewind messages, keep current code |
| **Restore code** | Revert files, keep conversation |
| **Summarize from here** | Compress conversation from this point forward |
| **Never mind** | Cancel |

### Summarize vs. Restore
- Restore undoes state (code, conversation, or both)
- Summarize compresses context (messages before selection stay intact, rest replaced with AI summary)
- Summarize keeps you in same session; for branching use `claude --continue --fork-session`

### Limitations
- Bash command file changes NOT tracked (`rm`, `mv`, `cp`)
- External/manual file changes NOT tracked
- Not a replacement for git version control

---

## 13. SCHEDULED TASKS

Requires Claude Code v2.1.72+. Session-scoped (gone when you exit).

### `/loop` Skill
```text
/loop 5m check if the deployment finished
/loop check the build                        # defaults to 10 minutes
/loop check the build every 2 hours          # trailing clause
/loop 20m /review-pr 1234                    # loop over another command
```

**Interval units:** `s` (seconds, rounded to minutes), `m`, `h`, `d`

### One-Time Reminders
```text
remind me at 3pm to push the release branch
in 45 minutes, check whether the integration tests passed
```

### Management Tools

| Tool | Purpose |
|------|---------|
| `CronCreate` | Schedule task (5-field cron, prompt, recur flag) |
| `CronList` | List all tasks with IDs, schedules, prompts |
| `CronDelete` | Cancel task by ID |

Max 50 tasks per session. Each has 8-char ID.

### Cron Expression Reference (5-field)
```
minute hour day-of-month month day-of-week
```

| Example | Meaning |
|---------|---------|
| `*/5 * * * *` | Every 5 minutes |
| `0 * * * *` | Every hour |
| `0 9 * * *` | Daily at 9am |
| `0 9 * * 1-5` | Weekdays at 9am |

### Behavior
- Fires between turns (not mid-response)
- Local timezone
- Jitter: recurring up to 10% of period (max 15 min), one-shot up to 90s
- 3-day auto-expiry for recurring tasks
- Disable: `CLAUDE_CODE_DISABLE_CRON=1`

### Limitations
- Only fires while Claude Code is running and idle
- No catch-up for missed fires
- No persistence across restarts

---

## 14. AGENT TEAMS

**Experimental.** Enable: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (env or settings.json).

Requires Claude Code v2.1.32+.

### What Agent Teams Are
Multiple Claude Code instances coordinated together. One lead session, multiple teammates, shared task list, inter-agent messaging.

### Agent Teams vs. Sub-Agents

| | Sub-Agents | Agent Teams |
|---|---|---|
| **Context** | Own window, results return to caller | Own window, fully independent |
| **Communication** | Report back to main only | Message each other directly |
| **Coordination** | Main manages all | Shared task list, self-coordinate |
| **Best for** | Focused tasks, only result matters | Complex work needing collaboration |
| **Token cost** | Lower | Higher |

### Starting a Team
```text
Create an agent team to explore this from different angles: one on UX,
one on technical architecture, one playing devil's advocate.
```

### Display Modes
| Mode | Description |
|------|-------------|
| `auto` (default) | Split panes in tmux/iTerm2, in-process otherwise |
| `in-process` | All in main terminal. Shift+Down to cycle |
| `tmux` | Each teammate in own pane |

Configure: `"teammateMode": "in-process"` in settings or `--teammate-mode in-process` flag.

### Team Architecture

| Component | Role |
|-----------|------|
| Team lead | Main session, creates team, coordinates |
| Teammates | Separate Claude instances |
| Task list | Shared work items |
| Mailbox | Messaging system |

Storage:
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

### Task States
Pending -> In Progress -> Completed. Tasks can have dependencies.

### Plan Approval
```text
Spawn an architect teammate to refactor auth. Require plan approval before changes.
```
Lead reviews and approves/rejects plans autonomously.

### Talking to Teammates
- **In-process**: Shift+Down to cycle, type to message, Enter to view, Escape to interrupt
- **Split-pane**: Click into teammate's pane

### Quality Gates via Hooks
- `TeammateIdle` -- exit 2 sends feedback, keeps teammate working
- `TaskCompleted` -- exit 2 prevents completion, sends feedback

### Permissions
Teammates start with lead's permissions. Can change individually after spawn.

### Best Practices
- 3-5 teammates for most workflows
- 5-6 tasks per teammate
- Break work so each teammate owns different files
- Start with research/review tasks (no file conflicts)
- Monitor and steer (don't leave unattended too long)

### Limitations
- No session resumption for in-process teammates
- Task status can lag
- Shutdown can be slow
- One team per session
- No nested teams
- Lead is fixed
- Permissions set at spawn
- Split panes require tmux or iTerm2

---

## KEY ENVIRONMENT VARIABLES (Referenced Across Docs)

| Variable | Purpose |
|----------|---------|
| `CLAUDE_CODE_NEW_INIT` | Enable interactive `/init` flow |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Load CLAUDE.md from `--add-dir` dirs |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Disable auto memory |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | Disable background tasks |
| `CLAUDE_CODE_DISABLE_CRON` | Disable scheduled tasks |
| `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` | Enable agent teams |
| `CLAUDE_CODE_EFFORT_LEVEL` | Set effort level |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | Revert to fixed thinking budget |
| `CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION` | Toggle prompt suggestions |
| `CLAUDE_CODE_TASK_LIST_ID` | Named task list directory |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | SessionEnd hook timeout |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Auto-compaction percentage trigger |
| `CLAUDE_ENV_FILE` | Path for persisting env vars in hooks |
| `ENABLE_TOOL_SEARCH` | MCP tool search behavior |
| `ENABLE_CLAUDEAI_MCP_SERVERS` | Toggle Claude.ai MCP servers |
| `MAX_MCP_OUTPUT_TOKENS` | MCP output token limit |
| `MCP_TIMEOUT` | MCP server startup timeout |
| `MAX_THINKING_TOKENS` | Thinking token budget limit |
| `SLASH_COMMAND_TOOL_CHAR_BUDGET` | Skill description budget |
| `ANTHROPIC_BASE_URL` | Custom API base URL |
| `ANTHROPIC_MODEL` | Override model |

---

## CLI COMMANDS REFERENCED

| Command | Purpose |
|---------|---------|
| `claude` | Start interactive session |
| `claude -p "prompt"` | Non-interactive/headless mode |
| `claude --continue` / `-c` | Resume most recent session |
| `claude --resume [name]` | Resume by name or open picker |
| `claude --from-pr <number>` | Resume session linked to PR |
| `claude -n <name>` | Name session at startup |
| `claude --agent <name>` | Run as specific subagent |
| `claude --agents '{json}'` | Define session subagents |
| `claude --worktree [name]` / `-w` | Create isolated worktree |
| `claude --add-dir <path>` | Add additional directory |
| `claude --permission-mode plan` | Start in plan mode |
| `claude --model <model>` | Override model |
| `claude --output-format text\|json\|stream-json` | Control output format |
| `claude --debug` | Full debug output |
| `claude --version` | Show version |
| `claude --teammate-mode <mode>` | Agent team display mode |
| `claude --dangerously-skip-permissions` | Bypass permissions (dangerous) |
| `claude --allowedTools "..."` | Session tool allowlist |
| `claude --disallowedTools "..."` | Session tool denylist |
| `claude --append-system-prompt "..."` | Add to system prompt |
| `claude agents` | List configured subagents |
| `claude mcp add/list/get/remove/add-json/add-from-claude-desktop/reset-project-choices/serve` | MCP management |

### In-Session Commands

| Command | Purpose |
|---------|---------|
| `/init` | Generate/improve CLAUDE.md |
| `/memory` | Browse memory files, toggle auto memory |
| `/agents` | Manage subagents |
| `/hooks` | Browse configured hooks |
| `/mcp` | Check MCP status, authenticate |
| `/permissions` | View/manage permissions |
| `/config` | Open settings UI |
| `/compact` | Compact conversation |
| `/rewind` | Open rewind menu |
| `/resume` | Switch to different session |
| `/rename` | Rename current session |
| `/add-dir` | Add working directory |
| `/vim` | Enable vim mode |
| `/theme` | Change theme |
| `/effort` | Change effort level |
| `/model` | Change model |
| `/context` | Check context usage |
| `/btw` | Side question (no history) |
| `/loop` | Schedule recurring prompt |
| `/batch` | Parallel codebase changes |
| `/simplify` | Code review + fix |
| `/debug` | Troubleshoot session |
| `/clear` | Clear conversation |
| `/terminal-setup` | Install terminal bindings |
| `/statusline` | Configure status line |
| `/voice` | Enable voice dictation |
| `/fast` | Toggle fast mode |
| `/desktop` | Hand off to desktop app |
| `/teleport` | Pull web session into terminal |

---

## 15. TOOLS REFERENCE

### All 28 Built-In Tools

#### File Operations
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `Read` | Read file contents | No |
| `Write` | Create/overwrite files | Yes |
| `Edit` | Make targeted edits to files | Yes |
| `NotebookEdit` | Modify Jupyter notebook cells | Yes |

#### Search & Discovery
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `Grep` | Search file contents with regex | No |
| `Glob` | Find files by pattern matching | No |
| `ToolSearch` | Search for/load deferred MCP tools | No |

#### Execution & Process
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `Bash` | Execute shell commands | Yes |
| `Agent` | Spawn subagents/worker agents | No |

#### Web & External
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `WebSearch` | Perform web searches | Yes |
| `WebFetch` | Fetch content from URLs | Yes |

#### Task Management (Persist Across Compactions)
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `TaskCreate` | Create tasks in the task list | No |
| `TaskGet` | Retrieve task details | No |
| `TaskList` | List all tasks with status | No |
| `TaskUpdate` | Update task status, dependencies, details | No |
| `TaskOutput` | Get output from background tasks | No |
| `TaskStop` | Kill running background tasks | No |
| `TodoWrite` | Manage session checklist (non-interactive mode only) | No |

#### Scheduling
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `CronCreate` | Schedule recurring/one-shot prompts (5-field cron) | No |
| `CronList` | List scheduled tasks with IDs | No |
| `CronDelete` | Cancel scheduled task by ID | No |

#### Planning & Worktrees
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `EnterPlanMode` | Switch to read-only plan mode | No |
| `ExitPlanMode` | Present plan for approval | Yes |
| `EnterWorktree` | Create isolated git worktree | No |
| `ExitWorktree` | Exit worktree, return to original directory | No |

#### User Interaction & Skills
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `AskUserQuestion` | Ask multiple-choice questions | No |
| `Skill` | Execute a skill in the main conversation | Yes |

#### MCP Resources
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `ListMcpResourcesTool` | List MCP server resources | No |
| `ReadMcpResourceTool` | Read specific MCP resource by URI | No |

#### Code Intelligence
| Tool | Purpose | Permission Required |
|------|---------|:---:|
| `LSP` | Language Server Protocol — type checking, navigation | No |

### Subagent Tool Inheritance

**When `tools:` is omitted** — subagent inherits ALL tools from the main session, including Task, Cron, and MCP tools.

**When `tools:` is specified** — only listed tools are available (allowlist).

**`disallowedTools:`** — remove specific tools from inherited set (denylist).

```yaml
# Inherits everything (including TaskCreate, CronCreate, etc.)
---
name: full-access-agent
tools:              # omitted = inherit all
---

# Restricted to specific tools
---
name: read-only-researcher
tools: Read, Grep, Glob, WebSearch, WebFetch
---

# All tools except specific ones
---
name: no-write-agent
disallowedTools: Write, Edit, Bash
---
```

### Tool Specifiers

```yaml
# Agent tool — restrict which subagents can be spawned
tools: Agent(worker, researcher), Read, Bash

# Agent tool — any subagent allowed
tools: Agent, Read, Bash

# Bash tool — restrict commands
tools: Bash(npm run *)
```

### Key Restriction

**`Agent` tool does not work in subagents.** Subagents cannot spawn other subagents. It only works on the main thread or when running as `claude --agent <name>`.

### Permission Rules for Tools

Tools can be allowed/denied in `settings.json`:
```json
{
  "permissions": {
    "allow": ["Read", "Write", "Edit", "Grep", "Glob", "WebSearch", "WebFetch", "Agent(*)"],
    "deny": ["Bash(rm *)", "Bash(sudo *)"]
  }
}
```

Pattern syntax:
- `Bash(npm run *)` — wildcard prefix
- `Agent(*)` — all subagents
- `Agent(code-reviewer)` — specific subagent
- `mcp__server__tool` — specific MCP tool
- `Read(./.env)` — specific file
- `WebFetch(domain:example.com)` — domain restriction
