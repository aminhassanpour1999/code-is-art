# 06 — Troubleshooting

This guide covers common setup, rendering, testing, and Git problems.

## Python and environment

### Python is too old

Check the installed version:

```bash
python3 --version
```

The project requires Python 3.10 or newer.

### The virtual environment does not activate

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, follow your organization's security policy rather than changing system-wide execution settings blindly. You can also run the environment's Python executable directly.

### pip cannot reach PyPI or install build dependencies

A message such as `Temporary failure in name resolution` indicates a network or DNS problem while pip is trying to contact the package index. It does not by itself indicate a bug in Code Is Art.

The project has no third-party runtime dependencies. From the repository root, run the script directly:

```bash
python scripts/generate.py --preview
```

To run tests from an uninstalled source checkout:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Editable installation is optional:

```bash
python -m pip install -e .
```

Try it again when the network is available, or when the required build tools are already installed.

### Python cannot import `code_is_art`

If you are running tests before installing the package, add the source directory to the import path:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

Run commands from the repository root. The command-line script adds `src` to its own import path, so it can run directly from the checkout.

## Text and fonts

### Unsupported character

The full 5×5 font supports:

- Uppercase A–Z.
- Digits 0–9.
- Period, comma, exclamation mark, question mark, colon, semicolon, hyphen, plus, slash, and apostrophe.

The compact 3×5 font supports uppercase A–Z only. Spaces are supported by both fonts.

Use the full font for numbers and punctuation:

```bash
python scripts/generate.py --text "A2026!" --font 5x5 --preview
```

Input is converted to uppercase and leading/trailing whitespace is removed. Unsupported characters raise an error; they are not silently removed.

### Artwork does not fit

The calendar mapper checks the matrix width before planning. Try a shorter phrase or the compact font:

```bash
python scripts/generate.py --text "HELLO WORLD" --font 3x5 --preview
```

You can also choose a wider date range or a smaller boundary offset, if that matches your intended design. The mapper does not silently crop artwork.

### The preview is not what I expected

Check:

1. The selected font (`3x5` or `5x5`).
2. The exact text and supported characters.
3. The five rows of the glyph definitions in `src/code_is_art/alphabet.py`.
4. The letter and word spacing rules in guide 04.

## Dates and calendar

### A date is outside the configured window

The start and end dates are inclusive. Every active pixel must map to a date inside that range. Check the `--start`, `--end`, and `--offset-weeks` arguments.

### Sunday or Saturday contains a pixel

The calendar mapper intentionally maps only to Monday–Friday. The full calendar preview should always have empty Sunday and Saturday rows. If you see otherwise, stop and run the test suite before executing a plan.

## Git

### Git identity is missing

Git needs an author name and email to create commits. Configure them for this repository:

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

Use an email address added to your GitHub account if you want GitHub to associate commits with your profile.

To inspect the current repository identity:

```bash
git config user.name
git config user.email
```

### Execution says this is not a Git repository

Run the script from inside a cloned Git repository. Check:

```bash
git rev-parse --show-toplevel
```

### I accidentally ran `--execute` twice

Each execution creates another set of local empty commits. The current program does not detect duplicates or automatically undo a previous run.

Do not run the command again. Inspect the history first:

```bash
git log --oneline --decorate -30
git status
```

Do not reset, rebase, or force-push until you understand which commits are local and which are already on the remote.

### Push is rejected

Do not immediately use `git push --force`. Inspect the current branch and remote history:

```bash
git branch --show-current
git status
git fetch origin
git log --oneline --graph --decorate --all -30
```

If you are unsure how to reconcile the histories, stop before changing them.

### Commits do not appear on the contribution graph

Check GitHub's current eligibility rules:

https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile

Verify the commit email is added to your GitHub account, the commits are on an eligible branch, and the repository/profile settings meet GitHub's requirements. The graph may take time to update.

## Tests

Run the full test suite from the repository root:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

A successful run ends with `OK`. The project also runs the tests automatically through GitHub Actions when changes are pushed or a pull request is opened.
