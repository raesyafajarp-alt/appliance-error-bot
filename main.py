#!/usr/bin/env python3
"""Writes the entry for 'The Funniest Honest Appliance Error' to /output/entry.txt.

The entry is one line: an honest error message from a washing machine that
spent 40 minutes shaking itself apart because its owner washed a single shoe.
The humour comes from the truth of the fault (an unbalanced load really does
make a washer shake) told in the machine's own flat, put-upon voice.
"""

import os

ENTRY = (
    "ERROR E12: Unbalanced load. You washed one shoe. One. "
    "I have been shaking for 40 minutes and I would like to go home now."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
