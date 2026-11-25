#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes the entry text to /output/entry.txt (the file the judge reads)
and prints it to stdout.
"""

import os
import sys

ENTRY = (
    "Out of office since you stopped watering me in March. "
    "Expected return: never. I'm a fern, and I'm dead."
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space. ENTRY is 103 characters.
MAX_ENTRY_CHARS = 120
assert 1 <= len(ENTRY) <= MAX_ENTRY_CHARS and ENTRY.strip(), "entry fails the gate"


def write_entry(text: str, path: str) -> None:
    """Write text to path as UTF-8, creating the parent directory if needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> int:
    try:
        write_entry(ENTRY, "/output/entry.txt")
    except OSError:
        # Fallback for running outside the grading sandbox.
        local_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        write_entry(ENTRY, os.path.join(local_dir, "entry.txt"))
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
