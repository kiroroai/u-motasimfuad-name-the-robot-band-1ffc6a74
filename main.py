#!/usr/bin/env python3
"""Name the Robot Band — one funny robot band name + hit song line.

Writes a single original line (under 200 characters) to /output/entry.txt.
Python 3, stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "The Blue Screen of Death Metal, whose hit single 'Ctrl+Alt+Delete My Number' crashed the charts."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
