"""Write the sleeve notes for a jazz trio of frogs to /output/entry.txt."""

import argparse
from pathlib import Path

ENTRY = """Blue Reeds

Three frogs — tenor sax, upright bass, drums — have held the back room of the Weir Tavern on Tuesdays for years. I've had the stool by the radiator since their first set. The tenor stays low and unhurried, the bass walks like he knows a shortcut, the drums brush around the gaps. When they start, the glasses stop clinking."""

DEFAULT_OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 400


def validate(text):
    """Return the text, or raise ValueError if the gate would reject it."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be UTF-8 text") from exc
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1 to 400 characters")
    if not text.strip():
        raise ValueError("entry must not be white space only")
    return text


def write_entry(path=DEFAULT_OUTPUT, text=ENTRY):
    """Validate the entry and write it as UTF-8 text with LF newlines."""
    validated = validate(text)
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(validated)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="path of the entry file (default: /output/entry.txt)",
    )
    args = parser.parse_args()
    write_entry(args.output)


if __name__ == "__main__":
    main()
