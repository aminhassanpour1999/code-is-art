# 03 — Designing Letters

This guide teaches you to create or edit a glyph without changing the renderer.

## Choose a font first

The project has two independent bitmap fonts:

- `FONT`: full 5×5 glyphs. Supports A–Z, digits, and punctuation.
- `COMPACT_FONT`: compact 3×5 glyphs. Supports A–Z and spaces, for longer phrases.

The renderer uses five rows in both fonts, so both fit the five weekday rows in the contribution calendar.

## The rules

Every glyph must:

1. Contain exactly five strings (five rows).
2. Have exactly five characters per row in `FONT`, or three in `COMPACT_FONT`.
3. Use only `#` and `.`.
4. Be recognizable at a small size.

## Example: design the letter T

For the full 5×5 font:

```text
#####
..#..
..#..
..#..
..#..
```

Add it to `FONT` in `src/code_is_art/alphabet.py`:

```python
"T": (
    "#####",
    "..#..",
    "..#..",
    "..#..",
    "..#..",
),
```

For the compact font, design a separate 3×5 version and add it to `COMPACT_FONT`:

```python
"T": (
    "###",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
),
```

## Add or edit a glyph

1. Open `src/code_is_art/alphabet.py`.
2. Choose `FONT` or `COMPACT_FONT`.
3. Add the character as a dictionary key.
4. Enter five rows with the correct width.
5. Run the full test suite:

```bash
python -m unittest discover -s tests -v
```

The tests check glyph dimensions, supported characters, and text rendering.

## Designing punctuation

Punctuation is currently supported by the full 5×5 font. Keep important marks visually distinct. For example, a period should sit near the bottom of the grid, while a hyphen should be centered.

## Design checklist

- Is the glyph recognizable?
- Does it have exactly five rows?
- Does every row have the correct number of columns?
- Does it use only `#` and `.`?
- Is it in the correct font dictionary?
- Does the complete phrase fit the available calendar width?

## Exercise

Design a question mark (`?`) and add it to the full `FONT`. Run the tests, then preview:

```bash
python scripts/generate.py --text "A?" --font 5x5 --preview
```
