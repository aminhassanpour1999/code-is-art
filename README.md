# Code Is Art

> Turn words into pixels. Turn pixels into commits.

**Code Is Art** is an educational Python project that converts text into pixel artwork and maps the pixels onto GitHub's contribution-calendar layout.

The project is designed to teach the complete process: bitmap fonts, two-dimensional matrices, calendar arithmetic, Git automation, validation, and testing.

## Features

- A documented 5×5 bitmap alphabet (A–Z, digits, and punctuation).
- Convert text into a rectangular pixel matrix.
- Render artwork in the terminal or as plain text.
- Map five artwork rows to Monday–Friday in GitHub's Sunday–Saturday calendar.
- Keep the top (Sunday) and bottom (Saturday) contribution rows empty.
- Plan a configurable number of commits per active pixel (default: 6).
- Preview and validate a plan before creating any commits.
- Generate local Git commits only after an explicit `--execute` flag.
- Unit tests using Python's standard library.

## Project configuration

| Setting | Value |
| --- | --- |
| Project | Code Is Art |
| Language | Python 3.10+ |
| Artwork window | 2026-01-01 through 2026-09-30 |
| Bitmap font | 5 columns × 5 rows |
| Commits per active pixel | 6 by default |
| Calendar top row | Sunday — always empty |
| Calendar bottom row | Saturday — always empty |
| License | MIT |

The date window contains 40 Sunday-to-Saturday calendar columns when partial weeks are included. The default one-week inset keeps artwork away from the two partial boundary weeks. The renderer checks width and date boundaries rather than silently cropping artwork.

## Quick start

Python 3.10 or newer is required. No third-party packages are needed.

```bash
git clone https://github.com/aminhassanpour1999/code-is-art.git
cd code-is-art
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

Preview the default artwork:

```bash
python scripts/generate.py --text "CODE" --preview
```

Build and inspect a commit plan (dry run; no commits are created):

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30
```

Only after reviewing the preview and plan, create local commits:

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30 --commits-per-pixel 6 --execute
```

The script does **not** push to GitHub. Review the local history first, then push manually if you choose to publish it. GitHub only displays eligible contributions when its contribution requirements are met; see [GitHub's contribution documentation](https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile).

## Learn the project

Read the guides in order:

1. [Getting started](docs/01-getting-started.md)
2. [Pixel-art fundamentals](docs/02-pixel-art-fundamentals.md)
3. [Designing letters](docs/03-designing-letters.md)
4. [Font reference](docs/04-font-reference.md)
5. [GitHub contributions and dates](docs/05-github-contributions.md)
6. [Troubleshooting](docs/06-troubleshooting.md)

## Project layout

```text
code-is-art/
├── docs/
├── examples/
├── scripts/
├── src/code_is_art/
├── tests/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Tests

Run the complete test suite:

```bash
python -m unittest discover -s tests -v
```

## Safety and transparency

The default mode is a dry run. The program never pushes commits, rewrites remote history, or changes GitHub settings. The `--execute` flag creates local empty commits with the planned dates. Use it only when you understand the result and have reviewed the plan.

## License

Distributed under the MIT License. See [LICENSE](LICENSE).

---

Made with Python, mathematics, and creativity.
