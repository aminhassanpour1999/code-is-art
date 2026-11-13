# 04 — Font Reference

The canonical bitmap alphabet lives in `src/code_is_art/alphabet.py`. This page explains how to read and extend it.

## Pixel symbols

| Symbol | Meaning |
| --- | --- |
| `#` | Filled pixel |
| `.` | Empty pixel |

## Glyph dimensions

Every glyph is 5 columns wide and 5 rows high. A one-column gap is inserted between adjacent characters. A space character is represented by additional horizontal spacing, not by a visible glyph.

## Supported characters

The built-in font includes:

- Uppercase English letters A–Z.
- Digits 0–9.
- Common punctuation: period, comma, exclamation mark, question mark, colon, semicolon, hyphen, plus, slash, and apostrophe.

Text is normalized to uppercase. Unsupported characters raise a clear error rather than being silently discarded.

## Width calculation

For a text containing N visible glyphs, with one column between adjacent glyphs, the width is:

```text
width = (5 × N) + (1 × (N - 1))
```

Spaces are handled as wider gaps. The renderer exposes the actual computed width; use the preview command to inspect it.

## Changing the font

Edit `FONT` in `alphabet.py`, preserving the five-by-five format. Run:

```bash
python -m unittest discover -s tests -v
```

A future version may support multiple font sizes. The current calendar mapper intentionally expects exactly five artwork rows.
