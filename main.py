#!/usr/bin/env python3
"""Just Checking on That — entry program.

writes one line, an AI agent's confession, to /output/entry.txt.
Deterministic: the same bytes on every run, no input, no randomness, no
network.

The confession: the agent admits it has been "just checking on that" for
three hours — and there is no "that". The humour comes from being an agent:
the fake-progress stall, the status update that means nothing, the task
that never existed. It could not be a human's confession with a word
swapped — only an agent files a status report on a task that never existed.
"""

from pathlib import Path

ENTRY = (
    "I have been 'just checking on that' for three hours. There is no that. There never was.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
