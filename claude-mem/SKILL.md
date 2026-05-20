---
name: claude-mem
description: Persistent memory compression system for Claude Code. Automatically captures tool usage observations across sessions, generates semantic summaries, and injects relevant context into future sessions so Claude remembers your project history.
---

# Claude-Mem

Claude-Mem gives Claude persistent memory across sessions by automatically recording what happens during each session, summarizing it, and making it available the next time you start Claude Code.

## When to Use This Skill

- Starting a new session on a long-running project and needing context from previous sessions
- Resuming work after a break and wanting Claude to remember prior decisions
- Searching your project history with natural language queries
- Maintaining continuity across multiple Claude Code sessions on the same codebase

## Installation

Install with a single command:

```bash
npx claude-mem install
```

Or from inside Claude Code via the plugin marketplace:

```
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

Restart Claude Code — context from previous sessions will automatically appear in new sessions.

## How It Works

Claude-Mem hooks into Claude Code's lifecycle to:

1. **Record observations** — Every tool use (Read, Write, Bash, etc.) is captured as a structured observation with title, facts, and narrative.
2. **Generate summaries** — At session end, observations are distilled into a searchable summary.
3. **Inject context** — At the start of the next session, the most relevant past observations are inserted into the system prompt.

No manual intervention required — it runs automatically in the background.

## Searching Memory

Query your project history using natural language:

```
Search memory for when we set up the database schema
```

```
What did we decide about authentication last week?
```

```
Find observations about the payment integration
```

Claude-Mem provides 4 MCP search tools following a token-efficient 3-layer workflow:

1. **`search`** — Get a compact index with observation IDs (~50–100 tokens/result)
2. **`timeline`** — Get chronological context around interesting results
3. **`get_observations`** — Fetch full details only for the IDs you care about (~500–1,000 tokens/result)

This layered approach saves ~10x tokens compared to fetching everything upfront.

## Privacy Control

Wrap any content in `<private>` tags to exclude it from storage:

```
<private>This sensitive information won't be recorded by claude-mem</private>
```

## Web Viewer

Browse your full memory timeline at [http://localhost:37777](http://localhost:37777) while Claude Code is running.

## Key Features

- Persistent memory that survives session restarts
- Automatic operation — no prompts or commands required
- Hybrid search (keyword + vector/semantic via Chroma)
- Progressive disclosure with token-cost visibility
- Web viewer UI at localhost:37777
- Privacy control via `<private>` tags
- Works with Claude Code, Gemini CLI, and OpenCode

## Resources

- [GitHub Repository](https://github.com/thedotmack/claude-mem)
- [Full Documentation](https://docs.claude-mem.ai/)
- [Installation Guide](https://docs.claude-mem.ai/installation)
- [Architecture Overview](https://docs.claude-mem.ai/architecture/overview)
