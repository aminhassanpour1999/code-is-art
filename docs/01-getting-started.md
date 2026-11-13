# 01 — Getting Started

This guide prepares the project and explains its workflow.

## Requirements

- Python 3.10 or newer.
- Git installed and configured with a name and an email address.
- A local clone of this repository.

No third-party Python dependencies are required.

## Install

```bash
git clone https://github.com/aminhassanpour1999/code-is-art.git
cd code-is-art
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
```

On Windows PowerShell, activate the environment with:

```powershell
.venv\Scripts\Activate.ps1
```

## First preview

```bash
python scripts/generate.py --text "CODE" --preview
```

The preview uses `#` for a filled pixel and `.` for an empty pixel. Spaces separate letters.

## Build a dry-run plan

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30
```

A dry run reports the number of active pixels, planned commits, date range, and the artwork preview. It does not modify the Git repository.

## Create local commits

After inspecting the dry run, add `--execute`:

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30 --commits-per-pixel 1 --execute
```

Execution requires the current directory to be inside a Git repository. It creates local empty commits and does not push.

## Recommended workflow

1. Design or choose the text.
2. Preview the pixel matrix.
3. Check that it fits the calendar.
4. Inspect the dry-run plan.
5. Run unit tests.
6. Execute only when you are satisfied.
7. Inspect `git log` before deciding whether to push.

## Learning objectives

By completing this project you will practice Python modules, dictionaries, lists, nested loops, dates, exceptions, command-line arguments, subprocesses, environment variables, and unit testing.
