# 02 — Pixel-Art Fundamentals

## What is a pixel?

A pixel is one small cell in a digital image. In this project, each pixel is represented by a Boolean value:

- `1` or `True`: filled pixel.
- `0` or `False`: empty pixel.

A character is a two-dimensional grid of pixels.

## A 5×5 example

The letter A can be represented as:

```text
.###.
#...#
#...#
#####
#...#
```

This grid has five rows and five columns. The first row is `.###.`: the middle three pixels are filled.

## Matrix representation

The same letter can be stored as a tuple of strings:

```python
LETTER_A = (
    ".###.",
    "#...#",
    "#...#",
    "#####",
    "#...#",
)
```

A matrix is useful because we can access a pixel by its row and column:

```python
pixel = LETTER_A[2][3]
```

Python indexes start at zero, so this reads row 3, column 4.

## Combining letters

To write a word, place glyphs side by side and insert a column gap between them. Each glyph has the same height, so the resulting artwork remains rectangular.

## Mapping pixels to dates

GitHub's contribution calendar is arranged in columns of weeks and rows of weekdays. The top row is Sunday and the bottom row is Saturday.

This project maps its five artwork rows to Monday, Tuesday, Wednesday, Thursday, and Friday. Sunday and Saturday are deliberately never assigned pixels.

A filled pixel on a date becomes a planned commit group for that date. The default group size is six commits.

## Previewing the complete calendar

A normal artwork preview displays only the five rows of letters. A dry run also prints the full seven-row contribution calendar, including empty Sunday and Saturday rows and the reserved boundary weeks:

```bash
python scripts/generate.py
```

The full calendar preview has one column for every Sunday-to-Saturday week intersecting the requested date range.

## Important distinction

A pixel is an artwork cell. A commit is a Git object. The program keeps these concepts separate: the renderer creates pixels, the calendar maps pixels to dates, and the generator creates a commit plan.
