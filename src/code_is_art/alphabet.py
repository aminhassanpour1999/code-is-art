"""Bitmap fonts and text-to-matrix conversion for Code Is Art."""

from __future__ import annotations

FONT: dict[str, tuple[str, ...]] = {
    "A": (".###.", "#...#", "#...#", "#####", "#...#"),
    "B": ("####.", "#...#", "####.", "#...#", "####."),
    "C": (".####", "#....", "#....", "#....", ".####"),
    "D": ("####.", "#...#", "#...#", "#...#", "####."),
    "E": ("#####", "#....", "####.", "#....", "#####"),
    "F": ("#####", "#....", "####.", "#....", "#...."),
    "G": (".####", "#....", "#.###", "#...#", ".###."),
    "H": ("#...#", "#...#", "#####", "#...#", "#...#"),
    "I": ("#####", "..#..", "..#..", "..#..", "#####"),
    "J": ("..###", "...#.", "...#.", "#..#.", ".##.."),
    "K": ("#...#", "#..#.", "###..", "#..#.", "#...#"),
    "L": ("#....", "#....", "#....", "#....", "#####"),
    "M": ("#...#", "##.##", "#.#.#", "#...#", "#...#"),
    "N": ("#...#", "##..#", "#.#.#", "#..##", "#...#"),
    "O": (".###.", "#...#", "#...#", "#...#", ".###."),
    "P": ("####.", "#...#", "####.", "#....", "#...."),
    "Q": (".###.", "#...#", "#...#", "#..##", ".####"),
    "R": ("####.", "#...#", "####.", "#..#.", "#...#"),
    "S": (".####", "#....", ".###.", "....#", "####."),
    "T": ("#####", "..#..", "..#..", "..#..", "..#.."),
    "U": ("#...#", "#...#", "#...#", "#...#", ".###."),
    "V": ("#...#", "#...#", "#...#", ".#.#.", "..#.."),
    "W": ("#...#", "#...#", "#.#.#", "##.##", "#...#"),
    "X": ("#...#", ".#.#.", "..#..", ".#.#.", "#...#"),
    "Y": ("#...#", ".#.#.", "..#..", "..#..", "..#.."),
    "Z": ("#####", "...#.", "..#..", ".#...", "#####"),
    "0": (".###.", "#..##", "#.#.#", "##..#", ".###."),
    "1": ("..#..", ".##..", "..#..", "..#..", ".###."),
    "2": (".###.", "#...#", "...#.", "..#..", "#####"),
    "3": ("####.", "....#", ".###.", "....#", "####."),
    "4": ("#...#", "#...#", "#####", "....#", "....#"),
    "5": ("#####", "#....", "####.", "....#", "####."),
    "6": (".###.", "#....", "####.", "#...#", ".###."),
    "7": ("#####", "...#.", "..#..", ".#...", ".#..."),
    "8": (".###.", "#...#", ".###.", "#...#", ".###."),
    "9": (".###.", "#...#", ".####", "....#", ".###."),
    ".": (".....", ".....", ".....", ".....", "..##."),
    ",": (".....", ".....", ".....", "..##.", "...#."),
    "!": ("..#..", "..#..", "..#..", ".....", "..#.."),
    "?": (".###.", "#...#", "...#.", "..#..", "..#.."),
    ":": (".....", "..#..", ".....", "..#..", "....."),
    ";": (".....", "..#..", ".....", "..#..", "...#."),
    "-": (".....", ".....", "#####", ".....", "....."),
    "+": (".....", "..#..", "#####", "..#..", "....."),
    "/": ("....#", "...#.", "..#..", ".#...", "#...."),
    "'": ("..#..", "..#..", ".....", ".....", "....."),
}

# Compact 3x5 alphabet: designed for longer phrases on a 38-week canvas.
COMPACT_FONT: dict[str, tuple[str, ...]] = {
    "A": (".#.", "#.#", "###", "#.#", "#.#"),
    "B": ("##.", "#.#", "##.", "#.#", "##."),
    "C": (".##", "#..", "#..", "#..", ".##"),
    "D": ("##.", "#.#", "#.#", "#.#", "##."),
    "E": ("###", "#..", "##.", "#..", "###"),
    "F": ("###", "#..", "##.", "#..", "#.."),
    "G": (".##", "#..", "#.#", "#.#", ".##"),
    "H": ("#.#", "#.#", "###", "#.#", "#.#"),
    "I": ("###", ".#.", ".#.", ".#.", "###"),
    "J": ("..#", "..#", "..#", "#.#", ".#."),
    "K": ("#.#", "#.#", "##.", "#.#", "#.#"),
    "L": ("#..", "#..", "#..", "#..", "###"),
    "M": ("#.#", "###", "###", "#.#", "#.#"),
    "N": ("#.#", "##.", "#.#", ".##", "#.#"),
    "O": (".#.", "#.#", "#.#", "#.#", ".#."),
    "P": ("##.", "#.#", "##.", "#..", "#.."),
    "Q": (".#.", "#.#", "#.#", ".##", "..#"),
    "R": ("##.", "#.#", "##.", "#.#", "#.#"),
    "S": (".##", "#..", ".#.", "..#", "##."),
    "T": ("###", ".#.", ".#.", ".#.", ".#."),
    "U": ("#.#", "#.#", "#.#", "#.#", "###"),
    "V": ("#.#", "#.#", "#.#", "#.#", ".#."),
    "W": ("#.#", "#.#", "###", "###", "#.#"),
    "X": ("#.#", "#.#", ".#.", "#.#", "#.#"),
    "Y": ("#.#", "#.#", ".#.", ".#.", ".#."),
    "Z": ("###", "..#", ".#.", "#..", "###"),
}

GLYPH_HEIGHT = 5
GLYPH_WIDTH = 5
LETTER_SPACING = 1
SPACE_WIDTH = 3
COMPACT_GLYPH_WIDTH = 3
COMPACT_LETTER_SPACING = 1
COMPACT_SPACE_WIDTH = 2


def normalize_text(text: str) -> str:
    """Normalize input to uppercase and trim surrounding whitespace."""
    normalized = text.upper().strip()
    unsupported = sorted(set(normalized) - set(FONT) - {" "})
    if unsupported:
        chars = ", ".join(repr(char) for char in unsupported)
        raise ValueError(f"Unsupported character(s): {chars}")
    if not normalized:
        raise ValueError("Text must contain at least one visible character.")
    return normalized


def text_width(text: str, compact: bool = False) -> int:
    """Return rendered width, including letter and word spacing."""
    normalized = normalize_text(text)
    font = COMPACT_FONT if compact else FONT
    glyph_width = COMPACT_GLYPH_WIDTH if compact else GLYPH_WIDTH
    letter_spacing = COMPACT_LETTER_SPACING if compact else LETTER_SPACING
    space_width = COMPACT_SPACE_WIDTH if compact else SPACE_WIDTH

    unsupported = sorted(set(normalized) - set(font) - {" "})
    if unsupported:
        chars = ", ".join(repr(char) for char in unsupported)
        raise ValueError(f"Selected font does not support: {chars}")

    width = 0
    previous_was_space = False
    for char in normalized:
        if char == " ":
            if width and not previous_was_space:
                width += space_width
            previous_was_space = True
        else:
            if width and not previous_was_space:
                width += letter_spacing
            width += glyph_width
            previous_was_space = False
    return width


def render_text(text: str, compact: bool = False) -> list[list[bool]]:
    """Convert text into a five-row Boolean pixel matrix.

    Set compact=True to use the 3x5 A-Z font for longer phrases.
    """
    normalized = normalize_text(text)
    font = COMPACT_FONT if compact else FONT
    letter_spacing = COMPACT_LETTER_SPACING if compact else LETTER_SPACING
    space_width = COMPACT_SPACE_WIDTH if compact else SPACE_WIDTH

    unsupported = sorted(set(normalized) - set(font) - {" "})
    if unsupported:
        chars = ", ".join(repr(char) for char in unsupported)
        raise ValueError(f"Selected font does not support: {chars}")

    rows: list[list[bool]] = [[] for _ in range(GLYPH_HEIGHT)]
    previous_was_space = True

    for char in normalized:
        if char == " ":
            if rows[0] and not previous_was_space:
                for row in rows:
                    row.extend([False] * space_width)
            previous_was_space = True
            continue

        if rows[0] and not previous_was_space:
            for row in rows:
                row.extend([False] * letter_spacing)

        for index, line in enumerate(font[char]):
            rows[index].extend(pixel == "#" for pixel in line)
        previous_was_space = False

    return rows
