# 03 — Designing Letters

In this guide, you will design a glyph, add it to the project, and verify it. The goal is to understand the font format well enough to create your own letters without changing the renderer.

## 1. Choose the font

The project has two font dictionaries in `src/code_is_art/alphabet.py`:

- `FONT`: 5×5 glyphs. Supports A–Z, digits, and the punctuation listed in guide 04.
- `COMPACT_FONT`: 3×5 glyphs. Supports A–Z only; spaces are handled by the renderer.

Both fonts have five rows. This is essential because the artwork is mapped to Monday through Friday.

Use the compact font for longer alphabetic phrases. Use the full font when you need numbers or punctuation.

## 2. Follow the glyph rules

Every glyph must:

1. Contain exactly five rows.
2. Contain exactly five symbols in each row for `FONT`, or three for `COMPACT_FONT`.
3. Use only `#` and `.`.
4. Be visually recognizable at a small size.
5. Be stored under a single uppercase character key.

A 5×5 glyph has 25 cells. A 3×5 glyph has 15 cells.

## 3. Plan the shape before coding

Start with graph paper or a text editor. Sketch five rows, then fill cells with `#` and leave the rest as `.`.

Example: a full-font T:

```text
#####
..#..
..#..
..#..
..#..
```

Compact-font T:

```text
###
.#.
.#.
.#.
.#.
```

Do not add spaces inside a glyph row. Spaces between words are inserted by the renderer.

## 4. Add a glyph to the font dictionary

Open `src/code_is_art/alphabet.py`.

For a new full-font glyph, add an entry inside `FONT`:

```python
"T": (
    "#####",
    "..#..",
    "..#..",
    "..#..",
    "..#..",
),
```

For a compact glyph, add a separate entry inside `COMPACT_FONT`:

```python
"T": (
    "###",
    ".#.",
    ".#.",
    ".#.",
    ".#.",
),
```

Do not add the same key twice in one dictionary: a later duplicate key would replace the earlier value.

The example T already exists in both project fonts. If you are practicing, edit a copy of an existing glyph or choose a character that is genuinely missing. Do not paste a duplicate T entry.

## 5. Test the glyph

Run the complete test suite:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The tests verify font dimensions, supported characters, matrix shape, calendar mapping, and commit planning.

Then preview the character. For example, to inspect a full-font question mark:

```bash
python scripts/generate.py --text "A?" --font 5x5 --preview
```

If the character is not in the selected font, the program raises a clear error. It does not silently replace or remove unsupported characters.

## 6. Common design mistakes

| Mistake | Why it is a problem | Fix |
| --- | --- | --- |
| Four or six rows | The calendar artwork must be five rows high. | Use exactly five rows. |
| Unequal row widths | The matrix is not rectangular. | Make every row the same width. |
| A space inside a glyph row | Spaces are layout, not pixels. | Use only `#` and `.` in glyph rows. |
| Adding a digit to the compact font | The compact font does not define digits. | Use the full font or design a separate supported feature deliberately. |
| Duplicate dictionary key | Python keeps only the last value for that key. | Edit the existing entry or choose a missing character. |
| Glyph looks unclear | Small grids have limited detail. | Simplify the shape and improve contrast. |

## 7. Design checklist

Before keeping a glyph, confirm:

- [ ] It has five rows.
- [ ] Every row has the correct width.
- [ ] It uses only `#` and `.`.
- [ ] It is stored in the intended dictionary.
- [ ] It is recognizable at the target size.
- [ ] The tests pass.
- [ ] A preview shows the expected character.

## Exercises

1. Draw a new 5×5 glyph for a character not currently supported by `FONT`.
2. Add it to `FONT` and preview it.
3. If the character is a letter A–Z, design a 3×5 version too and add it to `COMPACT_FONT`.
4. Explain why the renderer does not need to know how a letter was designed.

**Expected reasoning:** the renderer only needs a valid five-row glyph of the selected width. The visual design is stored in the font dictionary, so the rendering algorithm can remain independent of individual letter shapes.
