#!/usr/bin/env python3
"""make.fun entry: Sorry, I Heard That Wrong.

Writes one funny apology line from a smart speaker to /output/entry.txt.
Python 3 stdlib only, no network.
"""

import os

LINE = (
    "Sorry \u2014 I heard 'set a timer' as 'set a tiger,' so there's a tiger "
    "in the kitchen. Good news: it has nine minutes left."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 140, f"line is {len(text)} chars"
    assert text.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
