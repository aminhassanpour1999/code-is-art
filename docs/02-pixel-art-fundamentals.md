# 02 — Pixel-Art Fundamentals

This guide explains the visual model behind Code Is Art. Before editing Python code, learn how a small grid can represent a letter.

## 1. What is a pixel?

A pixel is one cell in a digital image. A bitmap stores whether each cell is on or off.

In this project:

| Symbol | Meaning | Python value |
| --- | --- | --- |
| `#` | Filled pixel | `True` |
| `.` | Empty pixel | `False` |

A letter is a grid of these cells. The grid is called a *bitmap* or *glyph*.

## 2. Read a 5×5 glyph

Here is the letter A:

```text
.###.
#...
#...#
#####
#...#
```

It has five rows and five columns. In the first row, the three middle cells are filled and the two outer cells are empty.

Count both dimensions carefully: 5 rows × 5 columns = 25 cells.

## 3. Represent the glyph in Python

The font file stores each glyph as a tuple of five strings:

```python
LETTER_A = (
    ".###.",
    "#...#",
    "#...#",
    "#####",
    "#...#",
)
```

Each string is one row. Each character in the string is one pixel.

The project later converts these symbols into Boolean values. For example, `#` becomes `True` and `.` becomes `False`.

## 4. Understand rows, columns, and indexes

Python uses zero-based indexing. The first item has index 0, not index 1.

```python
row = LETTER_A[2]       # third row: "#...#"
pixel = LETTER_A[2][3]  # fourth cell in that row: "."
```

The first index selects a row; the second selects a column.

For a matrix named `matrix`, use:

```python
matrix[row_index][column_index]
```

In this project, artwork coordinates are written as `(x, y)`: `x` is the column and `y` is the row. This is the reverse order from Python's access syntax, so the corresponding access is `matrix[y][x]`.

## 5. Why must a matrix be rectangular?

A matrix is rectangular when every row has the same number of columns.

Valid:

```text
.#.
###
..#
```

Invalid:

```text
.#.
###
.. 
```

The invalid example has rows of different widths. A rectangular matrix makes it possible to map each column to a calendar week without ambiguity.

## 6. Combine glyphs into text

To render a word, the program places glyphs side by side:

1. Start with five empty output rows.
2. Read one character from the input text.
3. Find its five-row glyph in the selected font.
4. Append each glyph row to the matching output row.
5. Insert the configured horizontal gap between characters.
6. Insert a wider gap for a word space.

The result is still five rows high, but its width depends on the text.

The full font uses 5-column glyphs, a 1-column letter gap, and a 3-column word gap. The compact font uses 3-column glyphs, a 1-column letter gap, and a 2-column word gap.

## 7. From text symbols to Boolean pixels

The renderer converts each row into Boolean values:

```python
pixel = (symbol == "#")
```

This expression evaluates to `True` when the symbol is `#`, and `False` otherwise.

The complete artwork is therefore a list of five lists. Each inner list represents one row of pixels.

## 8. Count the active pixels

An active pixel is a cell whose value is `True`.

For example:

```python
sample = [
    [True, False, True],
    [False, True, False],
]
```

There are three active pixels. The project's renderer provides `count_active_pixels()` to calculate this total.

## 9. Preview the result

From the repository root:

```bash
python scripts/generate.py --text "A" --font 5x5 --preview
python scripts/generate.py --text "CODE" --font 3x5 --preview
```

The first command uses the full font; the second uses the compact font.

## Key ideas to remember

- A glyph is a small bitmap representing one character.
- A matrix is a rectangular arrangement of rows and columns.
- `matrix[y][x]` accesses row `y`, column `x`.
- `True` means filled; `False` means empty.
- Combining glyphs means joining their rows horizontally.
- The artwork always has five rows because it will map to five weekdays.

## Exercises

1. Count the filled pixels in the letter A shown above.
2. In `LETTER_A[4][0]`, which row and column are selected?
3. Explain why a row with four cells cannot be combined safely with rows that have five cells.
4. Draw a 5×5 letter of your choice using only `#` and `.`.

**Answers:** 1. 14. 2. The fifth row and first column. 3. The matrix would not be rectangular, so column positions would not line up. 4. Answers vary; check that your glyph has exactly five rows and five symbols in each row.
