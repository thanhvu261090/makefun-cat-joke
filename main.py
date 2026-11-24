#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun entry program.

Writes a single cat joke, one line under 200 characters, to
/output/entry.txt. Nothing else goes in the entry.
"""

import os

ENTRY = (
    "My cat pushed my glass off the table, held eye contact "
    "the whole way down, and somehow I ended up apologizing."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Mirror the make.fun gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if text != text.strip():
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if "cat" not in text.lower():
        return False
    if "  " in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate_check failed: entry is not a valid one-liner")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
