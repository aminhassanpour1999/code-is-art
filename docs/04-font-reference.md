# 04 — Font Reference

The canonical fonts live in `src/code_is_art/alphabet.py`.

## Pixel symbols

| Symbol | Meaning |
| --- | --- |
| `#` | Filled pixel |
| `.` | Empty pixel |

## Two font sizes

### Full font: 5×5

The full font contains uppercase A–Z, digits 0–9, and common punctuation. Each glyph is five columns wide and five rows high. One empty column separates adjacent characters; word spaces are wider.

### Compact font: 3×5

The compact font contains uppercase A–Z. Each glyph is three columns wide and five rows high. It is designed for longer phrases that need to fit the 38 available calendar columns.

The default artwork, `CODE IS ART`, uses the compact font and occupies 37 columns.

## Supported characters

The 5×5 font includes:

- Uppercase English letters A–Z.
- Digits 0–9.
- Period, comma, exclamation mark, question mark, colon, semicolon, hyphen, plus, slash, and apostrophe.

The compact 3×5 font currently supports A–Z and spaces only. Choose the 5×5 font when your text contains numbers or punctuation.

Text is normalized to uppercase. Unsupported characters raise a clear error rather than being silently discarded.

## Width calculation

For a compact phrase containing N letters and one-column letter spacing, the glyph portion is:

```text
width = (3 × N) + letter gaps + word gaps
```

The renderer calculates the exact width. The calendar mapper rejects artwork that exceeds the available width; it never silently crops it.

## Designing a letter

For a 3×5 glyph, create exactly five strings with three characters each. For a 5×5 glyph, create exactly five strings with five characters each. Use only `#` and `.`.

Edit the appropriate dictionary in `alphabet.py`, then run:

```bash
python -m unittest discover -s tests -v
```
