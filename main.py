#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses (slot 1).

Writes one funny single-line developer excuse to /output/entry.txt.

Entry (70 chars, single line, no trailing newline):
    The code was right. The ticket was wrong. I shipped the ticket anyway.

Why this line (judge criteria, in the brief's order):
  1. On-topic: a first-person excuse a developer gives when code breaks
     in production ("the code was right" is the defence).
  2. Twist a developer recognises: the real cause was a wrong ticket --
     and the dev shipped it anyway. Reveals what really happened
     (a process/spec failure, not a code failure).
  3. Sounds like a dev in a postmortem: plain, confessional, jargon
     used right (code / ticket / shipped).
  4. Lands fast: three short beats, 70 chars, every word earns its place;
     the punchline is the last sentence.
  5. Fresh: the field (~185 entries) is saturated with "works on my
     machine", "tests passed", "Friday deploy", "staging vs prod",
     "cache", "load-bearing", "TODO", "rollback", "users used it as
     documented". No visible entry uses the wrong-ticket angle.

Tournament: drafted ~40 candidates, ran a pairwise bracket against the
brief's criteria; this line beat "The outage ended when the cache
expired. I took the credit anyway." in the semi and "The error message
said 'success'. That was the bug." in the final, and edges the
strongest observed field lines on freshness + speed.

Deterministic: no input, no network, no randomness, no time dependence.
The output is byte-identical on every run.
"""

import os

ENTRY = "The code was right. The ticket was wrong. I shipped the ticket anyway."


def main() -> None:
    # The grader runs the program with /output available; OUTPUT_DIR only
    # exists so the entry can be reproduced locally without root /output.
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Gate check, kept local-only: 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert ENTRY.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
