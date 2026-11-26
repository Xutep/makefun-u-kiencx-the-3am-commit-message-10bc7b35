"""Write one 3am git commit message to /output/entry.txt.

Deterministic, stdlib-only: the same single line every run.
"""

import os

LINE = (
    "fix: the bug was a typo i wrote at 2am, so i deleted the feature, "
    "the tests, and my will to live. it passes now"
)


def main():
    # The gate accepts 1-139 characters; refuse to write anything else.
    if not 1 <= len(LINE) <= 139 or not LINE.strip():
        raise ValueError(f"entry line must be 1-139 non-blank characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
