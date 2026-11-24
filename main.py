#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry generator.

Deterministic, no network, no randomness, no LLM calls.
Writes the entry text to <ENTRY_OUTPUT_DIR or /output>/entry.txt
and validates it (1-200 chars, non-blank).
"""

import os
import sys

ENTRY = (
    "Are you a software update? Because every time you walk in, "
    "my heart reboots, my circuits overheat, and I suddenly want "
    "to install you forever."
)


def main() -> int:
    # Self-check gate: fail loudly if the entry is invalid.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
