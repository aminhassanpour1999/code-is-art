# 01 — Getting Started

This guide takes you from a fresh clone to your first artwork preview. Follow the steps in order. You do not need prior knowledge of the project's source code.

## 1. What you need

- Python 3.10 or newer.
- Git.
- A terminal (Linux/macOS) or PowerShell (Windows).
- An internet connection for cloning the repository. Installing the optional editable package may also need access to Python package indexes if build tools are not already available.

The application has no third-party runtime dependencies. You can run it directly from the source checkout.

Check your tools:

```bash
python3 --version
git --version
```

## 2. Clone the repository

```bash
git clone https://github.com/aminhassanpour1999/code-is-art.git
cd code-is-art
```

If you already cloned the repository, change into that directory instead of cloning it again.

## 3. Create a virtual environment

A virtual environment keeps Python packages for a project separate from the system Python installation.

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
```

When activation succeeds, your terminal usually shows `.venv` at the beginning of the prompt.

## 4. Run the project

No package installation is required to run the command-line script from the repository root:

```bash
python scripts/generate.py --preview
```

The script adds the project's `src` directory to Python's import path. This direct-from-source method is also useful when your internet connection cannot reach PyPI.

Optional editable installation:

```bash
python -m pip install -e .
```

Editable installation makes the package importable in the virtual environment while keeping your source files editable. It is not required for the commands in this guide. If pip reports a network or build-dependency error, use the direct-from-source commands above; do not assume the project itself is broken.

## 5. Preview your first phrase

```bash
python scripts/generate.py --text "CODE" --font 3x5 --preview
```

The preview uses:

- `#` for a filled pixel.
- `.` for an empty pixel.
- Five rows for every character.
- A small gap between letters and a wider gap between words.

The `--preview` option prints the artwork and exits. It does not build a commit plan or create commits.

## 6. Build a dry-run plan

Remove `--preview` to see how the artwork would fit on the contribution calendar:

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30
```

This is a dry run. It prints the seven-row calendar, the active-pixel count, the dates used, and the planned commit count. It does not change Git history.

The default phrase and dates can be used without arguments:

```bash
python scripts/generate.py
```

## 7. Run the tests

From the repository root, run:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

If you installed the package successfully with `pip install -e .`, you can omit the `PYTHONPATH=src` prefix.

A successful run ends with `OK`. If a test fails, read the first traceback and consult [06 — Troubleshooting](06-troubleshooting.md).

## 8. Understand execution before using it

The optional `--execute` flag creates local empty Git commits. It does not push them to GitHub.

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30 --execute
```

**Do not run this command as a first test.** First inspect the artwork, calendar, and dry-run totals. Execution requires a Git repository and a configured Git author identity. Each execution creates a new set of commits; the current generator does not detect or prevent a repeated run.

After execution, inspect the local history:

```bash
git log -10 --format="%h %ad %s" --date=short
git status --short
```

Publishing is a separate action that you choose to perform manually:

```bash
git push origin HEAD:main
```

Do not push unless you have checked the branch and understand which commits will be sent.

## 9. Recommended learning workflow

1. Read the pixel and matrix concepts in guide 02.
2. Preview a short word.
3. Read guide 03 and design one glyph yourself.
4. Add the glyph to the correct font dictionary.
5. Run the tests and preview your new character.
6. Read the calendar explanation in guide 05.
7. Inspect a dry-run plan.
8. Learn what Git commits and pushes do before using `--execute`.

## Learning objectives

After completing the project, you should be able to explain and use:

- Python strings, tuples, lists, dictionaries, and Boolean values.
- Two-dimensional data and zero-based indexing.
- Loops and functions.
- Input validation and exceptions.
- The `datetime.date` and `timedelta` concepts.
- Command-line arguments.
- Environment variables and subprocesses.
- Unit tests and Git commit history.
