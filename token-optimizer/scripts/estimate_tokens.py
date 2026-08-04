#!/usr/bin/env python3
"""Estimate token counts for prompt files without any external dependencies.

Uses tiktoken's cl100k_base encoding when available for an exact count,
and falls back to a chars/4 heuristic (a widely used approximation for
English prose) otherwise, so the script runs in any environment.

Usage:
    python3 estimate_tokens.py FILE_OR_DIR [FILE_OR_DIR ...]
    python3 estimate_tokens.py --before old.md --after new.md
"""

import argparse
import glob
import os
import sys

try:
    import tiktoken

    _ENC = tiktoken.get_encoding("cl100k_base")

    def count_tokens(text: str) -> int:
        return len(_ENC.encode(text))

    METHOD = "tiktoken/cl100k_base"
except ImportError:
    def count_tokens(text: str) -> int:
        return max(1, round(len(text) / 4))

    METHOD = "heuristic (chars/4)"


def iter_files(paths):
    for path in paths:
        if os.path.isdir(path):
            for f in sorted(glob.glob(os.path.join(path, "**", "*.md"), recursive=True)):
                yield f
        else:
            yield path


def report(paths):
    rows = []
    for path in iter_files(paths):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        rows.append((path, count_tokens(text), len(text)))

    rows.sort(key=lambda r: r[1], reverse=True)
    width = max((len(r[0]) for r in rows), default=4)
    print(f"# token estimate method: {METHOD}\n")
    print(f"{'file'.ljust(width)}  tokens  chars")
    for path, tokens, chars in rows:
        print(f"{path.ljust(width)}  {tokens:>6}  {chars:>6}")
    if rows:
        total = sum(r[1] for r in rows)
        print(f"\ntotal: {total} tokens across {len(rows)} file(s)")


def compare(before_path, after_path):
    with open(before_path, encoding="utf-8") as fh:
        before = count_tokens(fh.read())
    with open(after_path, encoding="utf-8") as fh:
        after = count_tokens(fh.read())
    saved = before - after
    pct = (saved / before * 100) if before else 0
    print(f"# token estimate method: {METHOD}\n")
    print(f"before: {before} tokens ({before_path})")
    print(f"after:  {after} tokens ({after_path})")
    print(f"saved:  {saved} tokens ({pct:.1f}%)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="Files or directories to scan")
    parser.add_argument("--before", help="Original file, used with --after")
    parser.add_argument("--after", help="Optimized file, used with --before")
    args = parser.parse_args()

    if args.before or args.after:
        if not (args.before and args.after):
            parser.error("--before and --after must be used together")
        compare(args.before, args.after)
        return

    if not args.paths:
        parser.error("provide at least one file/directory, or use --before/--after")

    report(args.paths)


if __name__ == "__main__":
    main()
