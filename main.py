"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed to /output/entry.txt, where the sealed scorer reads it.

The line is validated against the gate before it is written: UTF-8 text,
1 to 160 characters, a single line, not only white space — so an invalid
entry can never be produced.
"""

import os

TEXT = "Fixed: 2 a.m. cringe replay no longer autoplays."


def main():
    text = TEXT.strip()
    assert text, "entry text must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, "entry must be 1 to 160 characters"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
