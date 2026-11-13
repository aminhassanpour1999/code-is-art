# 04 — Font Reference

This page is a quick technical reference for the two bitmap fonts. For the step-by-step process of creating a glyph, read [03 — Designing Letters](03-designing-letters.md).

The canonical definitions are in `src/code_is_art/alphabet.py`.

## Pixel symbols

| Symbol | Meaning | Boolean value |
| --- | --- | --- |
| `#` | Filled pixel | `True` |
| `.` | Empty pixel | `False` |

## Font comparison

| Property | Full font | Compact font |
| --- | --- | --- |
| Dictionary | `FONT` | `COMPACT_FONT` |
| Glyph width | 5 columns | 3 columns |
| Glyph height | 5 rows | 5 rows |
| Supported letters | A–Z | A–Z |
| Digits | 0–9 | Not supported |
| Punctuation | Supported list below | Not supported |
| Letter spacing | 1 empty column | 1 empty column |
| Word spacing | 3 empty columns | 2 empty columns |

Both fonts normalize input to uppercase. Leading and trailing whitespace is removed. Unsupported characters raise `ValueError`; they are not silently discarded.

## Full-font punctuation

In addition to A–Z and 0–9, `FONT` supports:

| Character | Name |
| --- | --- |
| `.` | Period |
| `,` | Comma |
| `!` | Exclamation mark |
| `?` | Question mark |
| `:` | Colon |
| `;` | Semicolon |
| `-` | Hyphen |
| `+` | Plus |
| `/` | Slash |
| `'` | Apostrophe |

The compact font supports only A–Z and spaces. If your phrase contains a digit or punctuation mark, select `--font 5x5`.

## Width calculation

The renderer calculates the exact width from the selected glyphs and spacing rules.

For a full-font phrase:

- Each visible character uses 5 columns.
- One empty column separates adjacent letters.
- A word space uses 3 empty columns.

For a compact phrase:

- Each visible character uses 3 columns.
- One empty column separates adjacent letters.
- A word space uses 2 empty columns.

Leading and trailing spaces do not add columns. Repeated internal spaces are treated as one word gap.

Example previews:

```bash
python scripts/generate.py --text "CODE IS ART" --font 3x5 --preview
python scripts/generate.py --text "A2026!" --font 5x5 --preview
```

## Calendar width

The default date window intersects 40 Sunday-to-Saturday weeks. With one boundary week reserved at each end, the mapper allows at most 38 artwork columns.

The default compact phrase `CODE IS ART` is 37 columns wide. The mapper checks the actual matrix width and raises an error if the artwork does not fit. It never crops the right side.

## Useful functions

| Function | Purpose |
| --- | --- |
| `normalize_text(text)` | Uppercases text, trims outer whitespace, and checks general character support. |
| `text_width(text, compact=False)` | Calculates the rendered width for the selected font. |
| `render_text(text, compact=False)` | Returns the five-row Boolean pixel matrix. |

## Quick verification

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The font tests verify glyph dimensions, supported characters, normalization, and the default phrase width.
