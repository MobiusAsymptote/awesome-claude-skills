---
name: token-optimizer
description: Analyzes and rewrites prompts, system instructions, and SKILL.md files to cut token usage while preserving meaning, tone, and behavior. Use before shipping any prompt that runs frequently or at scale, when auditing skill files for bloat, or when a draft feels padded, repetitive, or unnecessarily long.
---

# Token Optimizer

Reduces the token footprint of prompts, system instructions, and skill files without changing what they instruct Claude to do. Every prompt token is paid for on every call, so trimming padding from a prompt that runs thousands of times compounds into real cost and latency savings — this skill makes that trimming systematic instead of ad hoc.

## When to Use This Skill

- Auditing a `SKILL.md` before submitting it to a skills repo or marketplace
- Trimming a system prompt or agent instruction set that runs on every request
- Reducing cost/latency for prompts called in a loop, pipeline, or at scale
- Cleaning up AI-drafted or human-drafted prompts full of filler and hedging
- Checking a prompt against a context-window or cost budget before shipping it

## What This Skill Does

1. **Estimates token usage** for the given prompt(s) or file(s), using `scripts/estimate_tokens.py`
2. **Flags waste patterns** — see Optimization Techniques below
3. **Rewrites the prompt** to be denser while preserving every instruction, constraint, example, and behavior
4. **Reports before/after token counts** and percent reduction
5. **Refuses to silently cut meaning** — anything whose removal could change model behavior is flagged for the user to confirm rather than deleted outright

## Optimization Techniques

Apply these, roughly in order of impact:

1. **Cut throat-clearing.** Remove preambles like "In this section, we will discuss..." — start with the instruction itself.
2. **Say it once.** Merge instructions restated in multiple places (intro, body, and "tips" section repeating the same rule).
3. **Prefer structure over prose.** Bullet lists and tables communicate the same constraints as multi-sentence paragraphs in fewer tokens.
4. **Collapse repeated examples.** Keep the one or two examples that cover the most edge cases; drop near-duplicates that teach nothing new.
5. **Drop hedging and filler adjectives.** "very," "really," "in order to," "it's important to note that" carry no instruction.
6. **Use imperative voice.** "Write the summary in..." beats "You should try to write the summary in...".
7. **Don't explain the self-evident.** Skip commentary on well-named steps or obvious constraints.
8. **Replace long enumerations with a rule.** A rule ("always use snake_case for filenames") replaces a paragraph of examples showing the same rule.

Never apply these if they would remove a constraint, edge case, example the model needs to disambiguate behavior, or safety/formatting requirement — optimizing for tokens must never optimize away correctness.

## How to Use

### Basic Usage

```
Optimize this prompt for token efficiency: <paste prompt>
```

### Auditing a file

```
Run the token optimizer on my-skill/SKILL.md and show before/after token counts
```

Claude will read the file, apply the techniques above, write the optimized version, and run the estimator to report savings:

```bash
python3 token-optimizer/scripts/estimate_tokens.py --before my-skill/SKILL.md.orig --after my-skill/SKILL.md
```

### Auditing a whole directory

```
Rank every SKILL.md in this repo by token count so I know where to focus
```

```bash
python3 token-optimizer/scripts/estimate_tokens.py .
```

## Example

**Before** (47 tokens):
> "In order to get started with this feature, it's important to note that you should first make sure that you have properly configured your settings. Once you have done that, you can then proceed to click the button labeled 'Submit' in order to continue with the process."

**After** (14 tokens):
> "Configure your settings, then click Submit."

Same instruction, ~70% fewer tokens, nothing lost.

## Tips

- Optimize structure first (prose → bullets/tables), then wordsmith what's left
- Re-run `estimate_tokens.py` after every edit pass to confirm real savings, not just a shorter-looking file
- Diff the before/after so a human can verify no instruction, example, or edge case was lost
- A prompt that's ambiguous after trimming will cost more tokens in retries and clarification turns than it saved — when in doubt, keep the clarifying sentence
- `tiktoken` gives exact counts if installed (`pip install tiktoken`); the script falls back to a chars/4 estimate otherwise

## Common Use Cases

- Trimming `SKILL.md` files before opening a PR to this repo
- Cutting system-prompt costs for high-volume or high-frequency agents
- Cleaning up verbose AI-drafted prompts before they ship
- Fitting a prompt back under a context-window or token-budget limit
