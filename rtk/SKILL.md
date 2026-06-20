---
name: rtk
description: Reduce token consumption 60-90% by using RTK (Rust Token Killer) to proxy CLI commands. RTK filters and compresses output from git, cargo, pytest, docker, kubectl, and 100+ other commands before they reach Claude's context. Use for any task involving shell commands that produce verbose output.
---

# RTK - Rust Token Killer

RTK is a CLI proxy that dramatically reduces token usage by filtering and compressing command output before it reaches Claude's context window. The Claude Code hook rewrites Bash commands transparently — `git status` automatically becomes `rtk git status`.

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
rtk init -g   # installs hook + RTK.md, then restart Claude Code
```

Add to `~/.claude/settings.json`:
```json
{
  "hooks": { "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{ "type": "command", "command": "rtk hook claude" }]
  }]}
}
```

## Meta Commands

Always call these directly (not via the hook):

```bash
rtk gain              # token savings analytics for this session
rtk gain --history    # historical savings across sessions
rtk discover          # scan Claude Code history for missed RTK opportunities
rtk proxy <cmd>       # run a command without RTK filtering (for debugging)
rtk --version         # verify installation
```

## How It Works

Once the hook is installed, all Bash tool calls are automatically rewritten:

| Original | RTK Equivalent | Savings |
|----------|---------------|---------|
| `git status` | `rtk git status` | -80% |
| `git log` | `rtk git log` | -80% |
| `cargo test` | `rtk cargo test` | -90% |
| `pytest` | `rtk pytest` | -90% |
| `ls` / `tree` | `rtk ls` | -80% |
| `docker ps` | `rtk docker ps` | compact |
| `kubectl get pods` | `rtk kubectl get pods` | compact |

**Limitation**: Claude Code built-in tools (`Read`, `Grep`, `Glob`) bypass the hook. Use explicit shell commands when you want RTK filtering.

## Key Categories

- **Git**: status, log, diff, add, commit, push, pull — all compressed
- **Testing**: cargo test, pytest, go test, jest, vitest, playwright (failures-only mode)
- **Build/Lint**: cargo build, clippy, tsc, ESLint, ruff, golangci-lint
- **Files**: ls, tree, cat, grep, find, diff
- **DevOps**: docker, kubectl, aws (strips secrets automatically)
- **Package managers**: pnpm, pip, bundle

## Real-World Impact

Typical 30-minute Claude Code session on a TypeScript/Rust project:
- Without RTK: ~118,000 tokens
- With RTK: ~23,900 tokens
- **Savings: ~80%**
