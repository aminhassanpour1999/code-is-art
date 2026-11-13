# 03 — Designing Letters

This guide teaches you to create or edit a glyph without changing the renderer.

## The rules

Every glyph must:

1. Contain exactly five strings (five rows).
2. Have exactly five characters in every row.
3. Use only `#` and `.`.
4. Be readable at a small size.

## Example: design the letter T

Start with a five-by-five grid:

```text
#####
..#..
..#..
..#..
..#..
```

Translate each row into a Python string:

```python
"T": (
    "#####",
    "..#..",
    "..#..",
    "..#..",
    "..#..",
),
```

## Add a new glyph

1. Open `src/code_is_art/alphabet.py`.
2. Add the character as a key in `FONT`.
3. Enter five rows of five cells.
4. Run the alphabet tests:

```bash
python -m unittest tests.test_alphabet -v
```

If the tests report an invalid glyph, check row count, row width, and allowed symbols.

## Designing punctuation

Punctuation uses the same 5×5 grid. Keep important marks visually distinct. For example, a period should sit near the bottom of the grid, while a hyphen should be centered.

## Design checklist

- Is the glyph recognizable?
- Does it have five rows?
- Does every row have five columns?
- Does it use only `#` and `.`?
- Does the complete word fit the available calendar width?

## Exercise

Design a question mark (`?`) and add it to the font. Run the tests, then preview:

```bash
python scripts/generate.py --text "A?"
```
