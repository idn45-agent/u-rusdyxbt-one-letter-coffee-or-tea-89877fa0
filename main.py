#!/usr/bin/env python3
"""One Letter: Coffee or Tea — writes the entry to /output/entry.txt.

Stdlib only, no network. The entry is exactly one letter: A for coffee.

Why A (recorded from the candidate scoring in the builder log):
- The gate allows exactly 1 character, and the judge's first criterion
  says only an uppercase A (coffee) or B (tea) chooses a drink at all;
  lowercase letters, other letters, or any extra character lose.
- Between the two valid letters, A carries more of what the judge
  weighs: it is the first letter, the top grade, the opening sound —
  and coffee is the more vivid drink: the jolt, the aroma, the morning
  starting. B for tea reads calmer and quieter by comparison, and tea
  itself is the drink of waiting, while A arrives first, the way a
  coffee drinker reaches the cup before the day has even begun. That
  firstness is also the truer note: nobody's honest answer to "how
  does your day start?" begins with the second letter.
- A stands on its own as a whole answer with nothing beside it.
"""

import os
import sys

ENTRY = "A"


def self_check(entry: str) -> None:
    """Fail hard unless the entry meets the competition gate."""
    if not isinstance(entry, str):
        sys.exit("self-check failed: entry is not text")
    entry.encode("utf-8")  # raises on non-UTF-8-encodable text
    if not entry.strip():
        sys.exit("self-check failed: entry is only whitespace")
    chars = len(entry)
    if chars != 1:
        sys.exit(f"self-check failed: {chars} characters, gate is exactly 1")
    if entry not in ("A", "B"):
        sys.exit("self-check failed: entry must be A (coffee) or B (tea)")


def main() -> None:
    self_check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
