# 06 — Troubleshooting

## Python is too old

Check:

```bash
python3 --version
```

Use Python 3.10 or newer.

## The package cannot be imported

Install the local project from its root directory:

```bash
python -m pip install -e .
```

Alternatively, run the script from the repository root; it adds the source directory to the import path.

## Unsupported character

The font supports uppercase A–Z, digits, and the punctuation listed in `04-font-reference.md`. Remove the unsupported character or add a glyph to `FONT`.

## Artwork does not fit

The calendar mapper checks the width before planning commits. Shorten the text, use a shorter phrase, or choose a wider date window. The program does not silently crop artwork.

## Date outside the configured window

Every active pixel must map to a date between the inclusive start and end dates. Check the date arguments and the calendar offset.

## Git identity is missing

Configure Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use an email associated with your GitHub account if you expect eligible commits to appear on your contribution graph.

## Execution refuses to run

The script requires `--execute` and a valid Git working tree. Run it from inside a cloned Git repository. It intentionally does not push commits.

## Tests

Run all tests:

```bash
python -m unittest discover -s tests -v
```
