"""The One-Line Exit -- make.fun bounty entry.

Writes a single-line resignation letter (TEXT) verbatim to
$OUTPUT_DIR/entry.txt (default /output). Stdlib-only, deterministic,
no network, no randomness, no external input.
"""

import os
import unicodedata
from pathlib import Path

TEXT = (
    "I hereby resign, effective immediately \u2014 after three years of "
    "turning it off and on again, I have decided to turn myself off."
)

MAX_CHARS = 140


def validate_text(text: str) -> None:
    """Raise ValueError unless text passes the gate.

    Gate (RULES.txt + PLAN): a string of 1-140 characters (characters,
    not bytes — non-ASCII text within the character gate is accepted),
    not whitespace-only, a single line (no \\n, \\r or \\t), no control
    characters (Unicode category Cc or DEL). A non-string raises
    ValueError, never a leaked TypeError.
    """
    if not isinstance(text, str):
        raise ValueError("TEXT must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"TEXT must be 1..{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("TEXT must not be whitespace-only")
    if any(ch in text for ch in ("\n", "\r", "\t")):
        raise ValueError("TEXT must be a single line")
    if any(unicodedata.category(ch) == "Cc" or ch == "\x7f" for ch in text):
        raise ValueError("TEXT must not contain control characters")


def main() -> None:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Validation runs BEFORE any write, so an invalid TEXT raises
    ValueError and writes no file. No trailing newline is added.
    """
    validate_text(TEXT)  # read the global live, at call time (tests patch it)
    # Empty OUTPUT_DIR counts as unset (PLAN contract): fall back to /output.
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
