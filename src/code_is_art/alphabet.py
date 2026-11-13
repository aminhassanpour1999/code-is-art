"""A small, fixed-width 5x5 bitmap font for Code Is Art."""

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

GLYPH_WIDTH = 5
GLYPH_HEIGHT = 5
LETTER_SPACING = 1
SPACE_WIDTH = 3


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


def text_width(text: str) -> int:
    """Return the rendered width, including inter-character spacing."""
    normalized = normalize_text(text)
    width = 0
    previous_was_space = False
    for char in normalized:
        if char == " ":
            if width and not previous_was_space:
                width += SPACE_WIDTH
            previous_was_space = True
        else:
            if width and not previous_was_space:
                width += LETTER_SPACING
            width += GLYPH_WIDTH
            previous_was_space = False
    return width


def render_text(text: str) -> list[list[bool]]:
    """Convert text into a five-row Boolean pixel matrix."""
    normalized = normalize_text(text)
    rows: list[list[bool]] = [[] for _ in range(GLYPH_HEIGHT)]
    previous_was_space = True

    for char in normalized:
        if char == " ":
            if rows[0] and not previous_was_space:
                for row in rows:
                    row.extend([False] * SPACE_WIDTH)
            previous_was_space = True
            continue

        if rows[0] and not previous_was_space:
            for row in rows:
                row.extend([False] * LETTER_SPACING)

        glyph = FONT[char]
        for index, line in enumerate(glyph):
            rows[index].extend(pixel == "#" for pixel in line)
        previous_was_space = False

    return rows
