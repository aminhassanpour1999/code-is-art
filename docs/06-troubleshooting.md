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

The full 5×5 font supports uppercase A–Z, digits 0–9, and the punctuation listed in `04-font-reference.md`.

The compact 3×5 font supports uppercase A–Z and spaces only. If your phrase contains digits or punctuation, use `--font 5x5`.

Text is converted to uppercase automatically. Unsupported characters produce an error instead of being silently removed.

## Artwork does not fit

The calendar mapper checks the width before planning commits. Shorten the text, use the compact font, or choose a wider date window. The program does not silently crop artwork.

Example:

```bash
python scripts/generate.py --text "HELLO WORLD" --font 3x5 --preview
```

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
