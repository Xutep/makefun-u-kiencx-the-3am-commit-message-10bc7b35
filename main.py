"""Write one 3am git commit message to /output/entry.txt.

Deterministic, stdlib-only: the same single line every run.
"""

import os

LINE = (
    "fix: the bug was a typo i wrote at 2am, so i deleted the feature, "
    "the tests, and my will to live. it passes now"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
