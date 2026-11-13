# Code Is Art

> Turn words into pixels. Turn pixels into a calendar.

Code Is Art is an educational Python project that teaches you to design bitmap letters, combine them into text, represent artwork as a Boolean matrix, and map that matrix onto GitHub's contribution-calendar layout.

The project is also a practical introduction to Python modules, dictionaries, lists, nested loops, date arithmetic, command-line interfaces, validation, testing, and safe Git automation.

## What you will learn

By following the guides in order, you will learn how to:

1. Understand pixels, bitmap glyphs, rows, columns, and two-dimensional matrices.
2. Design and validate your own 3×5 and 5×5 letter patterns.
3. Combine glyphs into words and render text as a Boolean matrix.
4. Map five artwork rows to Monday–Friday in a seven-row calendar.
5. Calculate dates and check whether artwork fits a chosen date window.
6. Preview a plan, test the code, and understand what local Git commits do.

## Features

- Full 5×5 font: uppercase A–Z, digits 0–9, and common punctuation.
- Compact 3×5 font: uppercase A–Z, intended for longer phrases.
- Text-to-matrix rendering and terminal previews.
- Seven-row Sunday-to-Saturday calendar preview.
- Monday–Friday artwork mapping; Sunday and Saturday remain empty.
- One planned commit per filled pixel by default.
- Dry-run behavior by default; local commit creation requires `--execute`.
- No third-party runtime dependencies.
- Unit tests and GitHub Actions for Python 3.10, 3.12, and 3.14.

## Project defaults

| Setting | Default |
| --- | --- |
| Artwork | `CODE IS ART` |
| Font | Compact 3×5 |
| Date window | 2026-01-01 through 2026-09-30 (inclusive) |
| Calendar columns | 40 Sunday-to-Saturday weeks |
| Reserved boundary columns | 1 at the start and 1 at the end |
| Available artwork width | 38 columns |
| Commits per filled pixel | 1 |
| Artwork weekdays | Monday–Friday |
| Empty calendar rows | Sunday and Saturday |
| License | MIT |

The compact rendering of `CODE IS ART` is 37 columns wide, so it fits within the 38 available columns. The mapper rejects artwork that does not fit or that would place a pixel outside the requested date range. It never silently crops artwork.

## Quick start

Requirements: Python 3.10+ and Git.

```bash
git clone https://github.com/aminhassanpour1999/code-is-art.git
cd code-is-art
python3 -m venv .venv
source .venv/bin/activate
```

The program can run directly from the repository; it has no third-party runtime dependencies:

```bash
python scripts/generate.py --preview
```

To run the tests directly from an uninstalled source checkout:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Optional: install the local package in editable mode when build tools are available:

```bash
python -m pip install -e .
```

## Try your own text

Preview a phrase with the compact font:

```bash
python scripts/generate.py --text "HELLO WORLD" --font 3x5 --preview
```

Use the full font for digits or punctuation:

```bash
python scripts/generate.py --text "A2026!" --font 5x5 --preview
```

Create a dry-run calendar plan:

```bash
python scripts/generate.py
```

A dry run does not create commits or change Git history. Read the complete preview and plan before considering execution.

## Learning path

Read the guides in order:

1. [Getting started](docs/01-getting-started.md) — setup, commands, and the safe workflow.
2. [Pixel-art fundamentals](docs/02-pixel-art-fundamentals.md) — pixels, matrices, indexing, and glyph composition.
3. [Designing letters](docs/03-designing-letters.md) — create, add, and test your own glyphs.
4. [Font reference](docs/04-font-reference.md) — supported characters, spacing, and width rules.
5. [GitHub contributions and dates](docs/05-github-contributions.md) — calendar mapping, date arithmetic, commits, and contribution eligibility.
6. [Troubleshooting](docs/06-troubleshooting.md) — common setup, Python, Git, and test issues.

## Project structure

```text
code-is-art/
├── docs/                  # Step-by-step learning guides
├── scripts/
│   └── generate.py        # Command-line entry point
├── src/code_is_art/
│   ├── alphabet.py        # Bitmap fonts and text rendering
│   ├── renderer.py        # Matrix validation and ASCII output
│   ├── calendar.py         # Artwork-to-date mapping
│   ├── validator.py        # Input and matrix validation
│   └── generator.py        # Commit planning and local execution
├── tests/                 # Automated unit tests
├── .github/workflows/     # Continuous integration
├── LICENSE
├── README.md
└── pyproject.toml
```

## Safety and transparency

The default command is a dry run. Adding `--execute` creates local empty Git commits with the planned author and committer dates; it does not push, switch branches, or rewrite remote history. Inspect the plan and understand the effect before execution. Do not run the same plan repeatedly: each execution creates another set of commits.

Generated commits are synthetic artwork data. They should not be represented as evidence of separate development tasks. GitHub decides which commits qualify for the contribution graph; see [GitHub's contribution documentation](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile).

## Tests

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
