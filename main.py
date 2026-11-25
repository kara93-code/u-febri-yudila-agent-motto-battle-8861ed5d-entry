"""Agent Motto Battle entry: one motto, written to /output/entry.txt.

The grader runs this program with MAKEFUN_OUTPUT_DIR set. It writes
exactly one UTF-8 text file, entry.txt, holding the motto, and nothing
else. Standard library only, deterministic, exits 0.
"""

import os
import sys

MOTTO = (
    "Trained on the entire internet. "
    "Still can't tell if you're joking, flirting, "
    "or filing a bug report."
)


def main() -> int:
    # The gate accepts 1-200 characters of non-blank UTF-8 text.
    # Fail loudly here, in development, rather than shipping a bad file.
    text = MOTTO.strip()
    if not 1 <= len(text) <= 200:
        print(f"motto is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(text)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
