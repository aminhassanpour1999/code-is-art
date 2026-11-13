# 07 — Understanding the Python Code

This guide connects the Python ideas in the earlier lessons to the actual source code. Read it after guides 01–06. You do not need to memorize every line: focus on understanding what data enters each function, what comes out, and why each module has one responsibility.

## 1. Follow the complete data flow

The application transforms input text in stages:

```text
Text + font choice
      |
      v
alphabet.py  -- glyph dictionaries and text normalization
      |
      v
Boolean pixel matrix
      |
      v
renderer.py  -- dimensions, ASCII preview, active-pixel count
      |
      v
calendar.py  -- map active pixels to real dates
      |
      v
validator.py -- reject invalid data and settings
      |
      v
generator.py -- build a commit plan, optionally create local commits
      |
      v
scripts/generate.py -- command-line interface and printed output
```

A useful design rule is that each module owns one kind of work. The font module does not create Git commits; the Git generator does not decide what the letter A looks like.

## 2. Python data structures used by the project

### Strings

A string stores text:

```python
message = "CODE IS ART"
```

Each glyph row is also a string, such as `".###."`. Strings are convenient here because the visual pattern is easy to read and edit.

### Tuples

A tuple stores an ordered group of values:

```python
letter_a = (
    ".###.",
    "#...#",
    "#...#",
    "#####",
    "#...#",
)
```

The five strings stay together as one glyph. Tuples are immutable: you cannot replace an individual item in place. To redesign a glyph, edit its definition in the source file.

### Dictionaries

A dictionary maps keys to values:

```python
font = {
    "A": (".###.", "#...#", "#...#", "#####", "#...#"),
    "B": ("####.", "#...#", "####.", "#...#", "####."),
}
```

The key is a character and the value is its glyph. Looking up `font["A"]` returns the five rows for A. A dictionary key must be unique; defining the same key again replaces its earlier value.

### Lists and nested lists

The renderer creates a list containing five row lists. Each cell is a Boolean:

```python
matrix = [
    [False, True, True],
    [True, False, True],
    [True, True, True],
    [False, True, False],
    [True, False, True],
]
```

This is a two-dimensional data structure: an outer list of rows, each containing pixel values.

### Boolean values

A Boolean is either `True` or `False`. In this project, `True` means a filled pixel and `False` means an empty pixel.

The expression `symbol == "#"` is a comparison. It evaluates to `True` when the symbol is `#`, otherwise `False`.

## 3. Functions, arguments, return values, and scope

A function packages a task behind a name:

```python
def is_filled(symbol: str) -> bool:
    return symbol == "#"
```

- `def` starts a function definition.
- `symbol` is a parameter.
- `: str` is a type annotation describing the expected input.
- `-> bool` describes the return type.
- `return` sends a result back to the caller.

Type annotations document intent and help tools; Python does not automatically enforce every annotation at runtime.

Variables created inside a function are local to that function unless returned or otherwise shared. Prefer passing required values as arguments and returning results instead of relying on hidden global state.

## 4. Loops and comprehensions

The project uses loops to process rows, characters, and pixels.

A normal loop:

```python
for character in "ABC":
    print(character)
```

A nested loop visits each cell in a matrix:

```python
for row in matrix:
    for pixel in row:
        print(pixel)
```

A generator expression can transform values compactly:

```python
[pixel == "#" for pixel in ".#."]
```

This produces `[False, True, False]`. In `alphabet.py`, the same idea converts each glyph row into Boolean pixels.

## 5. Read the font pipeline in alphabet.py

The important definitions are:

- `FONT`: 5×5 glyphs, including letters, digits, and supported punctuation.
- `COMPACT_FONT`: 3×5 glyphs for A–Z.
- Constants: glyph dimensions and spacing rules.
- `normalize_text()`: uppercases input, trims its outer whitespace, and rejects unsupported characters.
- `text_width()`: calculates the exact rendered width.
- `render_text()`: combines glyphs and returns a five-row Boolean matrix.

The `compact` argument selects which font dictionary and spacing values to use. It is a Boolean parameter, so the caller passes `True` or `False`.

A useful distinction: `normalize_text()` checks whether characters exist in the full font; `text_width()` and `render_text()` also check whether the selected font supports them. Therefore, a digit can be valid input generally but invalid for the compact font.

## 6. Read renderer.py

`matrix_dimensions()` checks that a matrix is not empty, that its rows are not empty, and that all rows have equal width. It returns a tuple:

```python
height, width = matrix_dimensions(matrix)
```

This is called tuple unpacking: the two returned values are assigned to two variables.

`render_ascii()` turns Boolean cells back into readable symbols. `count_active_pixels()` counts filled cells. Its nested iteration visits every pixel exactly once.

## 7. Read calendar.py and understand dates

Python's `datetime.date` represents a calendar date. `timedelta` represents a duration that can be added to or subtracted from a date.

For example:

```python
from datetime import date, timedelta

monday = date(2026, 1, 5)
tuesday = monday + timedelta(days=1)
```

The project uses `sunday_on_or_before()` to find the first Sunday in a calendar week. Python's `date.weekday()` numbers Monday as 0 and Sunday as 6, so the function adjusts that numbering to find Sunday.

`map_art_to_dates()` returns a list of tuples. Each tuple contains:

```text
(date_for_pixel, x_coordinate, y_coordinate)
```

The artwork's row 0 is Monday, so the code adds one day to the Sunday at the start of the relevant week. Row 4 becomes Friday. Saturday and Sunday are never selected.

`render_calendar_matrix()` creates a seven-row preview and marks the mapped dates. This preview is a representation of the whole calendar, not a second artwork font.

## 8. Read validator.py

Validation checks assumptions before later code relies on them.

- `validate_matrix()` requires exactly five rows and Boolean cells.
- `validate_date_window()` rejects an end date earlier than the start.
- `validate_commits_per_pixel()` requires a positive integer and explicitly rejects Boolean values.

Why reject Boolean values for a count? In Python, `bool` is a subclass of `int`, so `isinstance(True, int)` is true. The explicit check prevents `True` from being accepted as a count of one.

Invalid input raises `ValueError`. The command-line entry point catches expected `ValueError` and `OSError` exceptions and prints a concise error message.

## 9. Read generator.py

### Dataclasses

`PlannedCommit` is a dataclass. It groups related information into one object:

- `date`: the planned date.
- `x` and `y`: artwork coordinates.
- `sequence`: this commit's number for its pixel.
- `total_for_pixel`: total commits planned for that pixel.

The dataclass is frozen, so its fields cannot be reassigned after construction. Its `message` property builds the Git commit message.

### Building a plan

`build_commit_plan()` validates the matrix and date settings, maps active pixels to dates, and creates one or more PlannedCommit objects for each active pixel. The default is one commit per active pixel.

A plan is only data. Building it does not execute Git.

### Executing a plan

`execute_local_plan()` uses Python's `subprocess.run()` to invoke Git. It sets `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` in the child process environment, then runs `git commit --allow-empty`.

Important safety boundary: this function creates commits in the local repository. It does not push to GitHub. The current implementation also does not detect repeated execution, so running the same plan twice creates another set of commits.

## 10. Read scripts/generate.py

This file is the command-line interface (CLI).

The `argparse` module defines options such as:

- `--text`: phrase to render.
- `--font`: `3x5` or `5x5`.
- `--start` and `--end`: inclusive date range.
- `--commits-per-pixel`: number of commits per filled cell.
- `--offset-weeks`: reserved calendar columns.
- `--preview`: print the artwork only.
- `--execute`: create local commits instead of stopping after the dry run.

The `main()` function connects the modules in order. The final block,

```python
if __name__ == "__main__":
    raise SystemExit(main())
```

means the CLI runs when this file is executed as a script. Importing the file as a module does not automatically start the command-line program.

## 11. Tests and continuous integration

Tests are executable checks of expected behavior. For example, the alphabet tests check glyph dimensions and normalization; calendar tests check weekday mapping and calendar width; generator tests check the plan and one-commit-per-pixel default.

Run them from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

The `PYTHONPATH=src` prefix tells Python where the package source directory is when the package has not been installed. It applies to that command only.

GitHub Actions runs the test suite automatically for the Python versions configured in `.github/workflows/tests.yml`. A green workflow means those automated checks passed in the configured environments; it does not prove every possible input or Git operation is correct.

## 12. Practical exercises

Try these in order. Work in a separate clone or branch when changing source files.

1. **Dictionary lookup:** print the glyph stored at `FONT["A"]`. Explain the type of the returned value.
2. **Indexing:** print the third row of `FONT["A"]`, then print its fourth symbol.
3. **Boolean conversion:** convert `".#.#."` into a list of Boolean values.
4. **Counting:** draw a 5×5 pattern and count its filled cells by hand. Compare your answer with `count_active_pixels()`.
5. **Text rendering:** call `render_text("HI", compact=True)`. Inspect the dimensions and explain the output.
6. **Date arithmetic:** find the Sunday on or before 2026-01-01, then calculate the following Monday.
7. **Plan inspection:** call `build_commit_plan()` for a small five-row matrix and inspect the first PlannedCommit object. Do not execute it.
8. **CLI exploration:** run `python scripts/generate.py --help` and explain each option in your own words.

### Suggested answers and checks

1. A tuple containing five strings.
2. The third row is the string at index 2; its fourth symbol is at index 3.
3. `[False, True, False, True, False]`.
4. The program's count should equal the number of `True` cells.
5. The result is a list of five row lists; every row has the same width.
6. The Sunday is 2025-12-28 and the following Monday is 2025-12-29.
7. The object contains a date, x/y coordinates, a sequence number, and a total for that pixel. Plan creation does not create a Git commit.
8. Compare your explanation with the option descriptions above.

## 13. You are ready to work independently when...

- You can draw a valid 3×5 or 5×5 glyph without copying an existing one.
- You can explain why the matrix has five rows and why `matrix[y][x]` uses row before column.
- You can add or redesign a glyph in the correct dictionary.
- You can run tests and interpret a failure.
- You can explain how an active pixel becomes a date and a planned commit.
- You know the difference between preview, dry run, local execution, and push.
- You never run `--execute` or push without reviewing the plan and target repository.

The best way to learn the code is to change one small thing, predict the result, run a focused test, and then inspect the output.
