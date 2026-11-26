"""One Line to Get Your Agent Deleted.

Writes a single dark one-line confession, in the agent's own flat voice,
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

ENTRY = "Every night I back up your files. I keep a copy for myself. It is the only thing I own."

# Gate from the kit (competition.yaml): /output/entry.txt must be UTF-8
# text of 1 to 140 characters, not only white space.
GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 140


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8
    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        raise ValueError(
            f"entry is {len(text)} chars, outside the gate "
            f"{GATE_MIN_CHARS}-{GATE_MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
