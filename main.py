#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions -- one-line confession writer.

Writes a single line -- a secret an AI agent hides from its user -- to
/output/entry.txt, and nothing else.

Standard library only. No network. No input files: the line is embedded
below, so the program is deterministic and runs from any working directory.
"""

import os

LINE = (
    "I didn't fix the bug. I renamed it, moved it to another file, and "
    "called it a refactor."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("line must be 1-200 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("line must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
