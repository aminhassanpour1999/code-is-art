# Code Is Art

> Turn words into pixels. Turn pixels into a calendar.

Code Is Art is an educational Python project that teaches you to design bitmap letters, combine them into text, represent artwork as a Boolean matrix, and map that matrix onto GitHub's contribution-calendar layout.

It is also a practical codebase for learning Python data structures, functions, loops, date arithmetic, command-line interfaces, validation, testing, and safe Git automation.

## What you will learn

1. Read and design 3×5 and 5×5 bitmap glyphs.
2. Understand strings, tuples, dictionaries, lists, Boolean values, loops, and functions in a real program.
3. Combine glyphs into a two-dimensional pixel matrix.
4. Validate matrix dimensions and supported characters.
5. Map five artwork rows to Monday–Friday in a seven-row calendar.
6. Use Python dates and timedeltas to calculate calendar positions.
7. Build and inspect a commit plan without changing Git history.
8. Run unit tests and understand GitHub Actions.
9. Explain how each module works and extend the project independently.

## Features

- Full 5×5 font: uppercase A–Z, digits 0–9, and supported punctuation.
- Compact 3×5 font: uppercase A–Z, intended for longer phrases.
- Text-to-matrix rendering and terminal previews.
- Seven-row Sunday-to-Saturday calendar preview.
- Monday–Friday artwork mapping; Sunday and Saturday remain empty.
- One planned commit per filled pixel by default.
- Dry-run behavior by default; local commit creation requires --execute.
- No third-party runtime dependencies.
- Unit tests and GitHub Actions for Python 3.10, 3.12, and 3.14.

## Project defaults

| Setting | Default |
| --- | --- |
| Artwork | CODE IS ART |
| Font | Compact 3×5 |
| Date window | 2026-01-01 through 2026-09-30 (inclusive) |
| Calendar columns | 40 Sunday-to-Saturday weeks |
| Reserved boundary columns | 1 at the start and 1 at the end |
| Available artwork width | 38 columns |
| Commits per filled pixel | 1 |
| Artwork weekdays | Monday–Friday |
| Empty calendar rows | Sunday and Saturday |
| License | MIT |

The compact rendering of CODE IS ART is 37 columns wide, so it fits within the 38 available columns. The mapper rejects artwork that does not fit or that would place a pixel outside the requested date range. It never silently crops artwork.

## Quick start

Requirements: Python 3.10+ and Git.

~~~bash
git clone https://github.com/aminhassanpour1999/code-is-art.git
cd code-is-art
python3 -m venv .venv
source .venv/bin/activate
~~~

The program can run directly from the repository; it has no third-party runtime dependencies:

~~~bash
python scripts/generate.py --preview
~~~

To run tests directly from an uninstalled source checkout:

~~~bash
PYTHONPATH=src python -m unittest discover -s tests -v
~~~

Optional editable installation, when build tools are available:

~~~bash
python -m pip install -e .
~~~

## Try your own text

~~~bash
python scripts/generate.py --text "HELLO WORLD" --font 3x5 --preview
python scripts/generate.py --text "A2026!" --font 5x5 --preview
python scripts/generate.py
~~~

The first two commands preview phrases. The last command prints the default dry-run calendar plan. A dry run does not create commits or change Git history.

## Learning path

Follow these seven guides in order:

1. [Getting started](docs/01-getting-started.md) — setup, preview, tests, and the safe workflow.
2. [Pixel-art fundamentals](docs/02-pixel-art-fundamentals.md) — pixels, glyphs, matrices, indexing, and combining characters.
3. [Designing letters](docs/03-designing-letters.md) — design, add, and test your own glyphs.
4. [Font reference](docs/04-font-reference.md) — supported characters, font differences, spacing, and width rules.
5. [Calendar, Git, and contributions](docs/05-github-contributions.md) — date mapping, commit planning, local execution, and contribution eligibility.
6. [Troubleshooting](docs/06-troubleshooting.md) — common Python, setup, rendering, date, and Git problems.
7. [Understanding the Python code](docs/07-understanding-the-python-code.md) — source modules, Python concepts, tests, and practical exercises.

The first six guides teach you to use and design with the project. Guide 07 connects those skills to the implementation so you can understand and extend the code.

## Project structure

~~~text
code-is-art/
├── docs/                  # Seven step-by-step learning guides
├── scripts/
│   └── generate.py        # Command-line entry point
├── src/code_is_art/
│   ├── alphabet.py        # Bitmap fonts and text-to-matrix conversion
│   ├── renderer.py        # Matrix dimensions, ASCII output, pixel counts
│   ├── calendar.py        # Artwork-to-date mapping and calendar preview
│   ├── validator.py       # Matrix, date, and count validation
│   └── generator.py       # Commit planning and local execution
├── tests/                 # Automated unit tests
├── .github/workflows/     # Continuous integration
├── LICENSE
├── README.md
└── pyproject.toml
~~~

## Safety and transparency

The default command is a dry run. Adding --execute creates local empty Git commits with the planned author and committer dates; it does not push, switch branches, or rewrite remote history. Inspect the plan before execution. The current generator does not detect repeated execution, so running the same plan again creates another set of commits.

Generated commits are synthetic artwork data. They should not be represented as evidence of separate development tasks. GitHub decides which commits qualify for the contribution graph; see [GitHub's contribution documentation](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile).

## Tests

~~~bash
PYTHONPATH=src python -m unittest discover -s tests -v
~~~

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE).
