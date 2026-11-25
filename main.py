"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Fixed: 2 a.m. cringe replay no longer autoplays."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
