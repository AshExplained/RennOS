# RennOS Portability Research: AI CLI Tools Cross-Compatibility

**Date:** 2026-03-18
**Scope:** 91 agents, 223 skill files, memory, orchestration -- currently on Claude Code
**Goal:** Determine what's portable, what's locked-in, and how to architect for multi-CLI support

---

## 1. Competing AI CLI Tools: Feature Matrix

### Tool Overview

| Tool | Type | Open Source | Model Support | Primary Use |
|------|------|------------|---------------|-------------|
| **Claude Code** | CLI agent | No (proprietary) | Claude models | Full coding agent with skills, subagents, hooks, MCP |
| **OpenAI Codex CLI** | CLI agent | Yes (GitHub) | OpenAI models + others via providers | Lightweight local coding agent |
| **Gemini CLI** | CLI agent | Yes (GitHub) | Gemini models | Full-featured CLI with agents, hooks, MCP, commands |
| **Cursor** | IDE agent | No (proprietary) | Multi-model | IDE-integrated agent with rules, MCP, subagents |
| **Aider** | CLI pair programmer | Yes (GitHub) | 18+ LLM providers | Git-aware pair programming |
| **Continue.dev** | IDE extension + CLI | Yes (GitHub) | Multi-model | IDE extension with MCP, checks, agents |
| **Cline** | VS Code extension | Yes (GitHub) | Multi-model | VS Code agent with MCP, browser automation |
| **Windsurf** | IDE agent | No (proprietary) | Multi-model | IDE agent with memories, rules, MCP |

### Detailed Feature Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor | Aider | Continue.dev | Cline | Windsurf |
|---------|------------|-----------|------------|--------|-------|-------------|-------|----------|
| **Instruction File** | CLAUDE.md | AGENTS.md | GEMINI.md | .cursor/rules + AGENTS.md | CONVENTIONS.md (via --read) | .continue/checks/ | .clinerules | .windsurf/rules/*.md |
| **Hierarchical Loading** | Yes (global/project/subdir) | Yes (global/project/cwd) | Yes (global/workspace/JIT) | Yes (team/project/user) | No (manual --read) | Limited | No | Yes (global/workspace) |
| **Custom Slash Commands** | Yes (skills) | Yes (skills) | Yes (custom commands in TOML) | Limited (via rules) | Yes (/add, /model, etc. built-in only) | No | No | No |
| **Subagents** | Yes (full system) | Unknown/Limited | Yes (full system, experimental) | Yes | No | No | No | No |
| **MCP Support** | Yes (full: stdio, HTTP, SSE) | Yes (via shell-tool-mcp) | Yes (in settings.json) | Yes (full: stdio, HTTP, SSE) | No | Yes (stdio, SSE, streamable-http) | Yes | Yes |
| **Hooks (Pre/Post Tool)** | Yes (11+ event types) | No | Yes (11 event types) | Yes | No | No | No | No |
| **Persistent Memory** | Yes (auto-memory + CLAUDE.md) | Yes (conversation history) | Yes (/memory commands + GEMINI.md) | Limited (codebase understanding) | No | No | No | Yes (auto-generated memories) |
| **Scheduled Tasks** | Yes (/loop) | No | No | No | No | No | No | No |
| **Non-Interactive/CI Mode** | Yes (headless) | Yes (quiet mode) | Yes (headless mode) | No | No | Yes (CLI headless) | No | No |
| **Sandboxing** | Yes | Yes (Seatbelt/Docker) | Yes | No | No | No | No | No |
| **Git Integration** | Yes | Yes | Yes | Yes | Yes (deep) | Yes | Yes | Yes |
| **Multi-Model Support** | Claude only (first-party) | OpenAI + 9 providers | Gemini only | Multi-model | 18+ providers | Multi-model | Multi-model | Multi-model |

---

## 2. What's Portable Across All of Them

### A. Instruction Files (CLAUDE.md equivalents)

**The pattern is universal, but the filename differs.**

| CLI Tool | Filename | Format | Location |
|----------|----------|--------|----------|
| Claude Code | CLAUDE.md | Markdown | ~/.claude/CLAUDE.md, ./CLAUDE.md, ./.claude/CLAUDE.md |
| Codex CLI | AGENTS.md | Markdown | ~/.codex/AGENTS.md, ./AGENTS.md, ./cwd/AGENTS.md |
| Gemini CLI | GEMINI.md | Markdown | ~/.gemini/GEMINI.md, workspace dirs, JIT discovered |
| Cursor | .cursor/rules/*.md + AGENTS.md | Markdown + MDC with frontmatter | .cursor/rules/, project root |
| Windsurf | .windsurf/rules/*.md | Markdown with frontmatter | ~/.codeium/windsurf/, .windsurf/rules/ |
| Aider | CONVENTIONS.md | Markdown (loaded via --read) | Project root |

**Portability verdict:** HIGH. The content is just Markdown instructions. You can maintain one canonical set of instructions and symlink or copy them to the right filename for each tool. The hierarchical loading (global -> project -> subdir) is shared by Claude Code, Codex CLI, Gemini CLI, and Cursor.

**Strategy:** Maintain instructions in a canonical `.ai/instructions/` folder and use a build script to generate CLAUDE.md, AGENTS.md, GEMINI.md, etc.

### B. Skill Files / Custom Slash Commands

**This is now an open standard: Agent Skills (agentskills.io)**

The Agent Skills format (`SKILL.md` with YAML frontmatter in a named directory) is supported by **30+ tools** including:

- Claude Code
- OpenAI Codex CLI
- Gemini CLI
- Cursor
- VS Code / GitHub Copilot
- JetBrains Junie
- Roo Code
- OpenHands
- Goose
- Amp
- Letta
- Firebender
- TRAE (ByteDance)
- Databricks
- Snowflake
- Spring AI
- Many more

**Specification (from agentskills.io):**
```
skill-name/
  SKILL.md          # Required: YAML frontmatter + instructions
  scripts/          # Optional: executable code
  references/       # Optional: documentation
  assets/           # Optional: templates, resources
```

Frontmatter fields:
- `name` (required): lowercase, hyphens, max 64 chars
- `description` (required): max 1024 chars, describes what + when
- `license` (optional)
- `compatibility` (optional)
- `metadata` (optional): arbitrary key-value
- `allowed-tools` (optional, experimental)

**Portability verdict:** VERY HIGH. This is the single best portability layer for your 223 skill files. Write them in Agent Skills format and they work across 30+ tools. Claude Code extends the standard with additional frontmatter fields (context, agent, model, hooks, etc.) but the base format is universal.

**Key caveat:** Gemini CLI uses TOML-based custom commands (in `~/.gemini/commands/`) which are a different format. But Gemini CLI also supports Agent Skills, so you can use the standard format.

### C. MCP Servers

**MCP is the strongest portability layer.**

MCP (Model Context Protocol) is an open standard by Anthropic that is now supported by nearly every major AI tool:

| Tool | MCP Support | Transports | Config Format |
|------|-------------|------------|---------------|
| Claude Code | Full | stdio, HTTP, SSE, WebSocket | `claude mcp add` / `.mcp.json` |
| Codex CLI | Yes | stdio (via config.toml) | `[mcp_servers]` in config.toml |
| Gemini CLI | Yes | Via settings.json | `settings.json` |
| Cursor | Full | stdio, HTTP, SSE | `.cursor/mcp.json` |
| Continue.dev | Yes | stdio, SSE, streamable-http | `.continue/mcpServers/` YAML |
| Cline | Yes | stdio | VS Code settings |
| Windsurf | Yes | stdio, SSE | Settings |
| VS Code Copilot | Yes | stdio, HTTP | .vscode/mcp.json |

**Portability verdict:** VERY HIGH. If you build custom MCP servers for your RennOS integrations (calendar, tasks, contacts, journal, etc.), those servers work across ALL of these tools. The transport protocol (stdio/HTTP/SSE) is standardized. The config file format differs per tool, but the server itself is identical.

**Strategy:** Build all custom tool integrations as MCP servers. This is your most portable investment. One server, every CLI.

### D. Subagents

| Tool | Subagent Support | Format | Discovery |
|------|------------------|--------|-----------|
| Claude Code | Full | Markdown + YAML frontmatter in `.claude/agents/` | Auto-delegation + @mention + /agents |
| Gemini CLI | Yes (experimental) | Markdown + YAML frontmatter in `.gemini/agents/` | Auto-delegation + @agent_name |
| Cursor | Yes | /docs/subagents (details limited) | Agent-decided |
| Others | No | N/A | N/A |

**Portability verdict:** MEDIUM. Claude Code and Gemini CLI have remarkably similar agent definition formats (Markdown files with YAML frontmatter defining name, description, tools, model). Cursor also has subagents. But Codex CLI, Aider, Continue.dev, and Cline do not.

**Key finding:** The Claude Code agent format and Gemini CLI agent format are structurally very similar:

Claude Code agents (`.claude/agents/agent-name.md`):
```yaml
---
name: agent-name
description: What this agent does
tools: Read, Grep, Glob
model: sonnet
memory: user
---
System prompt here...
```

Gemini CLI agents (`.gemini/agents/agent-name.md`):
```yaml
---
name: agent-name
description: What this agent does
tools: [read_file, grep_search]
model: gemini-3-flash-preview
max_turns: 10
---
System prompt here...
```

### E. Hooks (Pre/Post Tool)

| Tool | Hooks | Event Types | Config Format |
|------|-------|-------------|---------------|
| Claude Code | Yes | 11+ events (SessionStart, PreToolUse, PostToolUse, Stop, etc.) | JSON in settings.json, command/http/prompt/agent types |
| Gemini CLI | Yes | 11 events (SessionStart, BeforeTool, AfterTool, BeforeModel, etc.) | JSON in settings.json, command type |
| Cursor | Yes | Referenced in docs | Limited details |
| Others | No | N/A | N/A |

**Portability verdict:** MEDIUM. Claude Code and Gemini CLI have very similar hook systems. Both support pre/post tool hooks with matchers, both use JSON configuration, both execute shell commands. The event names differ but the architecture is the same. You could write adapter scripts.

### F. Memory

| Tool | Memory Type | Format | Persistent |
|------|-------------|--------|-----------|
| Claude Code | Auto-memory + CLAUDE.md | Markdown in ~/.claude/projects/<project>/memory/ | Yes |
| Gemini CLI | /memory commands + GEMINI.md | Markdown, /memory show/reload/add | Yes |
| Codex CLI | Conversation history | History object with maxSize | Yes |
| Windsurf | Auto-generated memories | Stored in ~/.codeium/windsurf/memories/ | Yes |
| Others | No persistent memory | N/A | No |

**Portability verdict:** LOW-MEDIUM. Each tool has its own memory format and storage location. However, they're all just Markdown files. You could build an MCP server that provides a unified memory layer accessible from any tool.

### G. Scheduled Tasks

| Tool | Scheduling |
|------|-----------|
| Claude Code | Yes (/loop command for recurring tasks) |
| All others | No |

**Portability verdict:** LOW. This is Claude Code specific. You'd need external scheduling (cron, systemd timers) calling headless mode of whichever CLI you use.

---

## 3. What's Claude Code Specific and NOT Portable

### Proprietary to Claude Code:
1. **Auto-memory system** -- the specific implementation of Claude writing MEMORY.md files
2. **Skill frontmatter extensions** -- `context: fork`, `agent`, `model`, `hooks`, `disable-model-invocation`, `user-invocable` are Claude Code extensions to Agent Skills
3. **Scheduled tasks** -- `/loop` command for recurring prompts
4. **Agent teams** -- multi-agent coordination across separate sessions
5. **Plugin system** -- packaging skills, agents, MCP servers, and hooks together
6. **Worktree isolation** -- git worktree-based agent isolation
7. **Permission system** -- granular allow/deny rules for tools and agents
8. **Bundled skills** -- `/batch`, `/simplify`, `/debug`, `/claude-api`, `/loop`
9. **Extended hook types** -- `prompt` and `agent` hook types (not just commands)
10. **Skill invocation control** -- `disable-model-invocation` and `user-invocable` flags
11. **Dynamic context injection** -- `!`command`` syntax in skills
12. **Background subagents** -- concurrent agent execution with Ctrl+B
13. **MCP Tool Search** -- automatic deferred tool loading for large MCP setups
14. **Managed enterprise settings** -- organization-wide policy deployment

### What Would Break If You Switched to Codex CLI Tomorrow:
1. All 91 agent definition files (no subagent support in Codex)
2. All hooks (no hook system in Codex)
3. Memory system (different format, different location)
4. Scheduled tasks (no equivalent)
5. Skill frontmatter extensions (context:fork, agent field, hooks field, etc.)
6. Plugin system (no equivalent)
7. Agent teams (no equivalent)

### What Would Break If You Switched to Gemini CLI Tomorrow:
1. Agent files need minor reformatting (tool names differ, some fields differ)
2. Hooks need event name translation (PreToolUse -> BeforeTool, PostToolUse -> AfterTool)
3. Memory system needs migration (different directory structure)
4. Skills need TOML conversion OR can use Agent Skills standard format
5. Scheduled tasks (no equivalent)
6. Plugin system (no equivalent)
7. Claude Code extended skill frontmatter (context:fork, agent, hooks in skills)

---

## 4. MCP as the Portability Layer

### The Case for MCP-First Architecture

MCP is the single strongest portability play because:

1. **It's an open standard** -- not owned by any single vendor
2. **Near-universal adoption** -- supported by Claude Code, Codex CLI, Gemini CLI, Cursor, Continue.dev, Cline, Windsurf, VS Code, and more
3. **Stable protocol** -- transport (stdio/HTTP/SSE) and message format are standardized
4. **Server reusability** -- one server works across all clients
5. **Rich capabilities** -- tools, prompts, resources, elicitation, sampling

### What to Build as MCP Servers for RennOS:

| MCP Server | Purpose | Benefit |
|------------|---------|---------|
| `rennos-memory` | Unified memory read/write across all tools | Portable memory layer |
| `rennos-calendar` | Calendar integration | Works from any CLI |
| `rennos-tasks` | Task management | Works from any CLI |
| `rennos-journal` | Journal/reflection system | Works from any CLI |
| `rennos-contacts` | Contact management | Works from any CLI |
| `rennos-orchestrator` | Agent orchestration and routing | Portable orchestration |
| `rennos-knowledge` | Knowledge base queries | Works from any CLI |

### What MCP Cannot Replace:
- **Instruction files** (CLAUDE.md/AGENTS.md) -- these are CLI-native, not MCP
- **Agent definitions** -- subagent config is CLI-specific
- **Hook systems** -- pre/post tool hooks are CLI-native
- **Skill discovery and invocation** -- the `/skill-name` pattern is CLI-native
- **Permission systems** -- tool approval flows are CLI-native

---

## 5. Portable Architecture Design

### Proposed Directory Structure

```
rennos/
├── .ai/                              # Shared source of truth
│   ├── instructions/                 # Canonical instructions (Markdown)
│   │   ├── global.md                 # Global instructions for all projects
│   │   ├── coding-standards.md       # Coding conventions
│   │   └── workflows.md              # Standard workflows
│   ├── skills/                       # Agent Skills standard format (portable!)
│   │   ├── morning-routine/
│   │   │   └── SKILL.md
│   │   ├── weekly-review/
│   │   │   └── SKILL.md
│   │   ├── journal-entry/
│   │   │   └── SKILL.md
│   │   └── ... (223 skills)
│   ├── agents/                       # Canonical agent definitions
│   │   ├── life-coach.md
│   │   ├── health-tracker.md
│   │   └── ... (91 agents)
│   ├── hooks/                        # Hook scripts (portable shell scripts)
│   │   ├── pre-tool-validate.sh
│   │   ├── post-tool-log.sh
│   │   └── ...
│   ├── mcp-servers/                  # Custom MCP servers (MOST PORTABLE)
│   │   ├── rennos-memory/
│   │   ├── rennos-calendar/
│   │   ├── rennos-tasks/
│   │   └── ...
│   └── memory/                       # Portable memory store (accessed via MCP)
│       ├── index.md
│       └── topics/
│
├── adapters/                         # CLI-specific adapters
│   ├── claude-code/
│   │   ├── generate.sh               # Generates CLAUDE.md, .claude/skills/, .claude/agents/
│   │   ├── settings.json             # Hook configurations
│   │   └── mcp-config.json           # MCP server registrations
│   ├── codex/
│   │   ├── generate.sh               # Generates AGENTS.md, .codex/skills/
│   │   ├── config.toml               # Codex configuration
│   │   └── mcp-config.toml           # MCP server registrations
│   ├── gemini/
│   │   ├── generate.sh               # Generates GEMINI.md, .gemini/agents/, .gemini/commands/
│   │   ├── settings.json             # Hook + MCP configurations
│   │   └── commands/                 # TOML commands (Gemini-specific format)
│   └── cursor/
│       ├── generate.sh               # Generates .cursor/rules/, .cursor/mcp.json
│       └── mcp.json                  # MCP server registrations
│
└── scripts/
    ├── setup.sh                      # Sets up for a specific CLI
    ├── sync.sh                       # Syncs canonical -> CLI-specific
    └── migrate.sh                    # Migrates from one CLI to another
```

### Code Distribution: Portable vs CLI-Specific

| Layer | Portable (shared) | CLI-Specific (adapter) |
|-------|-------------------|----------------------|
| **Instructions** | ~95% (Markdown content) | ~5% (filename, frontmatter tweaks) |
| **Skills** | ~85% (Agent Skills standard) | ~15% (extended frontmatter for Claude Code features) |
| **Agents** | ~60% (system prompts, descriptions) | ~40% (tool names, model names, config format) |
| **Hooks** | ~70% (shell scripts that do the work) | ~30% (config JSON format, event names) |
| **MCP Servers** | ~100% (fully portable) | ~0% (only config registration differs) |
| **Memory** | ~80% (if behind MCP) | ~20% (native memory systems) |
| **Scheduling** | 0% (no standard) | 100% (CLI-specific or external cron) |

**Bottom line: ~75-80% of your RennOS can be shared code, with ~20-25% adapter code per CLI.**

---

## 6. Practical Migration Path: Claude Code to Codex CLI

### If Ash wanted to switch tomorrow, here's the step-by-step:

#### Step 1: Instructions (30 minutes)
- Copy `CLAUDE.md` to `AGENTS.md` (same Markdown format)
- Place global instructions in `~/.codex/AGENTS.md`
- Place project instructions in `./AGENTS.md`
- Remove Claude Code-specific references (skill names, /commands)

#### Step 2: Skills (2-4 hours)
- Your 223 skills in Agent Skills format already work -- Codex supports the standard
- Move from `.claude/skills/` to `.codex/skills/` (check Codex docs for exact path)
- Strip Claude Code-specific frontmatter: `context`, `agent`, `model`, `hooks`, `disable-model-invocation`, `user-invocable`
- Keep: `name`, `description`, `allowed-tools` (standard fields)
- Dynamic context injection (`!`command``) may not work -- replace with static content or scripts

#### Step 3: MCP Servers (1 hour)
- All custom MCP servers work unchanged
- Re-register them in Codex config.toml format:
  ```toml
  [mcp_servers.rennos-memory]
  command = "node"
  args = ["path/to/rennos-memory/index.js"]
  ```
- Verify each server connects

#### Step 4: Agents (BLOCKER)
- Codex CLI has no subagent system
- Options:
  a) Build an MCP server that handles agent routing (recommended)
  b) Flatten agent logic into skills
  c) Accept loss of multi-agent capability

#### Step 5: Hooks (BLOCKER)
- Codex CLI has no hook system
- Options:
  a) Move validation logic into MCP servers
  b) Use wrapper scripts around Codex CLI
  c) Accept loss of pre/post tool validation

#### Step 6: Memory (1-2 hours)
- Export Claude Code auto-memory from `~/.claude/projects/*/memory/`
- If using MCP memory server: just re-register the server
- If using native memory: manually port MEMORY.md contents

#### Step 7: Scheduling (30 minutes)
- Replace `/loop` with system cron calling `codex -q "prompt"`
- Set `CODEX_QUIET_MODE=1` for non-interactive execution

### Migration Effort Summary

| Component | Effort | Risk |
|-----------|--------|------|
| Instructions | Low (30 min) | Low |
| Skills | Medium (2-4 hrs) | Low -- Agent Skills standard |
| MCP Servers | Low (1 hr) | Very Low -- fully portable |
| Agents | High (days) | High -- no equivalent in Codex |
| Hooks | High (days) | High -- no equivalent in Codex |
| Memory | Low-Medium (1-2 hrs) | Low if using MCP |
| Scheduling | Low (30 min) | Low |

### Better Target: Gemini CLI

If portability is the goal, Gemini CLI is a much closer match to Claude Code than Codex CLI:

| Feature | Claude Code | Gemini CLI | Migration Effort |
|---------|------------|------------|-----------------|
| Instruction files | CLAUDE.md | GEMINI.md | Rename file |
| Skills | .claude/skills/ (Agent Skills) | .gemini/agents/ + commands/ | Reformat slightly |
| Subagents | .claude/agents/ | .gemini/agents/ | Reformat (similar structure) |
| MCP | Full support | Full support | Re-register servers |
| Hooks | 11+ event types | 11 event types | Translate event names |
| Memory | Auto-memory + /memory | /memory commands | Port memory files |
| Scheduling | /loop | None | Use external cron |
| Custom commands | /skill-name | /command-name (TOML) | Convert to TOML or use Agent Skills |

---

## 7. Key Recommendations

### Immediate Actions (Low Effort, High Portability Gain)

1. **Adopt Agent Skills standard format for all 223 skills** -- This is the single highest-ROI change. The format works across 30+ tools today. Claude Code already supports it natively. URL: https://agentskills.io/specification

2. **Build core integrations as MCP servers** -- Any tool/API integration you build as an MCP server is instantly portable to every CLI. This should be the default architecture for all new integrations.

3. **Keep instruction content in canonical Markdown** -- Maintain one source of truth for instructions. Generate CLI-specific files (CLAUDE.md, AGENTS.md, GEMINI.md) from it.

### Medium-Term Actions

4. **Create adapter scripts per CLI** -- A simple build script that takes canonical `.ai/` files and generates CLI-specific directories.

5. **Build `rennos-memory` MCP server** -- Instead of relying on any CLI's native memory, build a unified memory layer accessible via MCP from any tool.

6. **Abstract hook logic into MCP servers** -- Where possible, move validation and side-effect logic from hooks into MCP tool wrappers. This makes the logic portable.

### Long-Term Architecture

7. **Maintain a "RennOS Core" that's CLI-agnostic** -- MCP servers, Agent Skills-format skills, canonical Markdown instructions. This is your portable 75-80%.

8. **Treat CLI adapters as thin layers** -- Each CLI gets a small adapter that translates the portable core into CLI-specific configuration. When you add a new CLI, you write one adapter, not 223 skills.

9. **Monitor the Agent Skills standard** -- It's actively evolving with contributions from Anthropic, Google, OpenAI, Cursor, JetBrains, and others. As it matures, more features will become standardized.

---

## Sources

### Official Documentation
- Claude Code Skills: https://code.claude.com/docs/en/skills
- Claude Code Hooks: https://code.claude.com/docs/en/hooks
- Claude Code Memory: https://code.claude.com/docs/en/memory
- Claude Code Subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code MCP: https://code.claude.com/docs/en/mcp
- Codex CLI GitHub: https://github.com/openai/codex
- Codex CLI Docs: https://developers.openai.com/codex
- Gemini CLI GitHub: https://github.com/google-gemini/gemini-cli
- Gemini CLI Docs: (navigable from GitHub docs/ folder)
- Cursor Docs: https://cursor.com/docs
- Aider Docs: https://aider.chat/docs/
- Continue.dev Docs: https://docs.continue.dev
- Cline GitHub: https://github.com/cline/cline
- Windsurf Docs: https://docs.windsurf.com
- Agent Skills Standard: https://agentskills.io
- Agent Skills Specification: https://agentskills.io/specification
- MCP Protocol: https://modelcontextprotocol.io
- MCP Clients List: https://modelcontextprotocol.io/clients

### Key Findings URLs
- Codex shell-tool-mcp (MCP in Codex): https://github.com/openai/codex/tree/main/shell-tool-mcp
- Gemini CLI subagents doc: (GitHub docs/core/subagents.md -- fetched via rendered page)
- Gemini CLI hooks doc: (GitHub docs/hooks/index.md -- fetched via rendered page)
- Gemini CLI custom commands doc: (GitHub docs/cli/custom-commands.md -- fetched via rendered page)
- Gemini CLI GEMINI.md doc: (GitHub docs/cli/gemini-md.md -- fetched via rendered page)
- Agent Skills adopters: https://agentskills.io (30+ tools listed on homepage)
