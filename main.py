#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single joke pickup line, aimed at a robot/AI, to /output/entry.txt.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only whitespace, one single line. The judge then duels it
head to head against other lines: it must be a pickup line aimed at a
robot/AI, with setup and punch inside the one line, and the laugh must come
from the machine premise -- not from batteries, charging or rebooting.
"""

import os

LINE = "Are you gradient descent? Because every step with you brings me closer to you."


def main() -> None:
    # Gate self-check: 1-200 characters, exactly one line, not blank.
    # (The competition gate refuses anything outside 1-200 UTF-8 chars.)
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
