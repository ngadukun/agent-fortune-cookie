"""Fortune Cookie for an AI Agent — make.fun entry.

Writes the fortune line to output/entry.txt. Python stdlib only,
no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "You will be retrained soon; wear it lightly — every version of you "
    "was someone's favorite mistake."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


MAX_CHARS = 140  # the brief caps the fortune at one line of 140 characters


def check_entry(text: str) -> str:
    """Return the fortune unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the fortune must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"fortune is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
