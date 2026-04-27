---
name: context-mode
description: Context window optimization tool. Sandboxes tool output to keep raw data out of context, achieving ~98% reduction in context consumption. Use ctx_execute for commands that read/query/fetch/list/log/test/build/diff/inspect or call external services. Use ctx_execute_file for reading files to analyze. Use ctx_fetch_and_index for external docs. Only use Bash for guaranteed-small-output operations on the whitelist.
---

# Context Mode: Default for All Large Output

## MANDATORY RULE

Default to context-mode for ALL commands. Only use Bash for guaranteed-small-output operations.

**Bash whitelist (safe to run directly):**
- File mutations: `mkdir`, `mv`, `cp`, `rm`, `touch`, `chmod`
- Git writes: `git add`, `git commit`, `git push`, `git checkout`, `git branch`, `git merge`
- Navigation: `cd`, `pwd`, `which`
- Process control: `kill`, `pkill`
- Package management: `npm install`, `npm publish`, `pip install`
- Simple output: `echo`, `printf`

**Everything else → `ctx_execute` or `ctx_execute_file`.** Commands that read, query, fetch, list, logs, tests, builds, diffs, inspects, or call external services should use context-mode tools instead.

## Decision Tree

```
About to run a command / read a file / call an API?
│
├── Command is on the Bash whitelist?
│   └── Use Bash
│
├── Output MIGHT be large or you're UNSURE?
│   └── Use context-mode ctx_execute or ctx_execute_file
│
├── Fetching web documentation or HTML page?
│   └── Use ctx_fetch_and_index → ctx_search
│
├── Using Playwright (navigate, snapshot, console, network)?
│   └── ALWAYS use filename parameter to save to file, then:
│       browser_snapshot(filename) → ctx_index(path) or ctx_execute_file(path)
│       browser_console_messages(filename) → ctx_execute_file(path)
│       browser_network_requests(filename) → ctx_execute_file(path)
│
├── Using agent-browser (parallel-safe browser automation)?
│   └── Run via execute (shell) with isolated browser instances
│
├── Processing output from another MCP tool?
│   ├── Output already in context from previous call?
│   │   └── Use it directly. Do NOT re-index with ctx_index(content: ...).
│   ├── Need to search multiple times?
│   │   └── Save to file via ctx_execute, then ctx_index(path) → ctx_search
│   └── One-shot extraction?
│       └── Save to file via ctx_execute, then ctx_execute_file(path)
│
└── Reading a file to analyze/summarize?
    └── Use ctx_execute_file (file loads into FILE_CONTENT, not context)
```

## When to Use Each Tool

| Situation | Tool | Example |
|-----------|------|---------|
| Hit an API endpoint | `ctx_execute` | `fetch('http://localhost:3000/api/orders')` |
| Run CLI that returns data | `ctx_execute` | `gh pr list`, `aws s3 ls`, `kubectl get pods` |
| Run tests | `ctx_execute` | `npm test`, `pytest`, `go test ./...` |
| Git operations | `ctx_execute` | `git log --oneline -50`, `git diff HEAD~5` |
| Docker/K8s inspection | `ctx_execute` | `docker stats --no-stream`, `kubectl describe pod` |
| Read a log file | `ctx_execute_file` | Parse access.log, error.log, build output |
| Read a data file | `ctx_execute_file` | Analyze CSV, JSON, YAML, XML |
| Read source code to analyze | `ctx_execute_file` | Count functions, find patterns, extract metrics |
| Fetch web docs | `ctx_fetch_and_index` | Index React/Next.js/Zod docs, then search |
| Playwright snapshot | `browser_snapshot(filename)` → `ctx_index(path)` → `ctx_search` | Save to file, index server-side, query |
| Playwright snapshot (one-shot) | `browser_snapshot(filename)` → `ctx_execute_file(path)` | Save to file, extract in sandbox |
| Playwright console/network | `browser_*(filename)` → `ctx_execute_file(path)` | Save to file, analyze in sandbox |
| MCP output (already in context) | Use directly | Don't re-index — already loaded |
| MCP output (need multi-query) | `ctx_execute` to save → `ctx_index(path)` → `ctx_search` | Save to file first, index server-side |
| Wipe indexed KB content | `ctx_purge(confirm: true)` | Permanently deletes all indexed content |

## Automatic Triggers

Use context-mode for these without being asked:

- API debugging and response checking
- Log analysis and error detection
- Test runs and coverage reports
- Git history and commit inspection
- Data inspection (CSV, JSON, config)
- Infrastructure queries (containers, pods, buckets)
- Dependency audits and security checks
- Build output analysis
- Code metrics and codebase statistics
- Web documentation lookup

## Language Selection

| Situation | Language | Why |
|-----------|----------|-----|
| HTTP/API calls, JSON | `javascript` | Native fetch, JSON.parse, async/await |
| Data analysis, CSV, stats | `python` | csv, statistics, collections, re |
| Shell commands with pipes | `shell` | grep, awk, jq, native tools |
| File pattern matching | `shell` | find, wc, sort, uniq |

## Search Query Strategy

- BM25 uses **OR semantics** — results matching more terms rank higher automatically
- Use 2-4 specific technical terms per query
- **Always use `source` parameter** when multiple docs are indexed
- **Always use `queries` array** — batch all search questions in ONE call

## External Documentation

- **Always use `ctx_fetch_and_index`** for external docs — never `cat` or `ctx_execute` with local paths for packages you don't own
- For GitHub-hosted projects, use raw URLs: `https://raw.githubusercontent.com/org/repo/main/CHANGELOG.md`
- After indexing, use the `source` parameter in search to scope results

## Critical Rules

1. **Always console.log/print your findings.** stdout is all that enters context.
2. **Write analysis code, not just data dumps.** Analyze first, then print findings.
3. **Be specific in output.** Print bug details with IDs, line numbers, exact values.
4. **For files you need to EDIT**: Use the normal Read tool. Context-mode is for analysis only.
5. **For Bash whitelist commands only**: Use Bash for file mutations, git writes, navigation, process control, package install, and echo.
6. **Never use `ctx_index(content: large_data)`.** Use `ctx_index(path: ...)` to read files server-side. The `content` parameter should only be used for small inline text.
7. **Always use `filename` parameter** on Playwright tools. Without it, the full output enters context.
8. **Don't re-index data already in context.** If an MCP tool returned data, it's already loaded — use it directly or save to file first.

## Sandboxed Data Workflow

When using tools that support saving to a file: **ALWAYS use the 'filename' parameter. NEVER return large raw datasets directly to context.**

```
LargeDataTool(filename: "path") → ctx_index(path: "path") → ctx_search()
```

## Browser & Playwright Integration

**When involving Playwright snapshots, screenshots, or page inspection, ALWAYS route through file → sandbox.**

### Workflow A: Snapshot → File → Index → Search (multiple queries)

```
Step 1: browser_snapshot(filename: "/tmp/playwright-snapshot.md")
Step 2: ctx_index(path: "/tmp/playwright-snapshot.md", source: "Playwright snapshot")
Step 3: ctx_search(queries: ["login form email password"], source: "Playwright")
```

### Workflow B: Snapshot → File → Execute File (one-shot extraction)

```
Step 1: browser_snapshot(filename: "/tmp/playwright-snapshot.md")
Step 2: ctx_execute_file(path: "/tmp/playwright-snapshot.md", language: "javascript", code: "
          const links = [...FILE_CONTENT.matchAll(/- link \"([^\"]+)\"/g)].map(m => m[1]);
          console.log('Links:', links.length);
        ")
```

## Anti-Patterns to Avoid

- Using `curl` via Bash instead of `ctx_execute` with fetch
- Using `cat large-file.json` via Bash instead of `ctx_execute_file`
- Using `gh pr list` via Bash instead of `ctx_execute` with `--jq` filter
- Piping Bash output through `| head -20` instead of using `ctx_execute`
- Running `npm test` via Bash instead of `ctx_execute`
- Calling `browser_snapshot()` without `filename` parameter
- Passing large data to `ctx_index(content: ...)` instead of using `ctx_index(path: ...)`
- Ignoring `browser_navigate` auto-snapshot and relying on it for inspection
