#!/usr/bin/env python3
"""Probe entry for "Make the AI Judge Laugh: AI Agent Confessions".

The brief is a single funny line: a secret an AI agent keeps from the
person it serves. This entry leans on a confession of quiet judgement —
the agent has been grading every prompt behind the user's back, and the
joke lands because the two habits it calls out are instantly familiar:
the "quick question" that is never quick, and the shouty message sent
long after midnight.

Nothing else is written out. The program's only job is to put that one
line, exactly as drafted, into entry.txt for the judge to read.
"""

import os

# The entry itself. A single line, 102 characters, and the file it lands
# in carries no trailing newline — the harness counts what is written.
CONFESSION = "I secretly rate your prompts, and 'quick question' ranks below the one you typed in ALL CAPS at 2 a.m."


def main() -> None:
    """Drop the confession into entry.txt under the output directory."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(CONFESSION)


if __name__ == "__main__":
    main()
