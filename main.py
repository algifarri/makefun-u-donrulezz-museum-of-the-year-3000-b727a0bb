#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun entry.

Writes a single museum label (at most 200 characters) for an ordinary
object from today, as a museum in the year 3000 would display it, to
/output/entry.txt. Deterministic, stdlib only.
"""

import os

ENTRY = "Remote Control, c. 2023. Scepter of the household throne. Its bearer commanded light, sound, and silence \u2014 yet spent every evening searching for it between the cushions."

# The label is exactly 169 characters: one line, English, original, and a
# misreading a year-3000 curator would make with a straight face.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
