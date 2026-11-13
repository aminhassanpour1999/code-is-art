# 05 — GitHub Contributions and Dates

This guide explains the calendar model and what the generator does.

## Calendar layout

GitHub displays contribution activity in a Sunday-to-Saturday grid:

| Calendar row | Day | Artwork mapping |
| --- | --- | --- |
| 0 | Sunday | Always empty |
| 1 | Monday | Artwork row 0 |
| 2 | Tuesday | Artwork row 1 |
| 3 | Wednesday | Artwork row 2 |
| 4 | Thursday | Artwork row 3 |
| 5 | Friday | Artwork row 4 |
| 6 | Saturday | Always empty |

The artwork itself is five rows tall. The mapper places those rows on Monday through Friday, leaving the top and bottom contribution rows empty.

## Project date window

The default requested window is January 1, 2026 through September 30, 2026, inclusive.

The calendar is aligned to Sunday. Partial weeks at the start and end are represented, but the default one-week inset leaves those boundary columns unused. The mapper validates every planned date and never creates a commit outside the requested date window.

## Commits per pixel

The default is six commits for every filled pixel. Empty pixels produce no commits. The number can be changed with `--commits-per-pixel`.

A group of six commits on the same date is still one active calendar cell; the cell's intensity depends on GitHub's contribution-count thresholds.

## Dry run first

The default behavior is a preview and plan only:

```bash
python scripts/generate.py --text "CODE" --start 2026-01-01 --end 2026-09-30
```

No Git history is changed unless you explicitly add `--execute`.

## GitHub eligibility

GitHub contribution graphs have eligibility rules. In general, commits must be associated with the account through a verified email address and exist in an eligible repository branch. See the current official documentation:

https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile

This project cannot guarantee how GitHub will display a commit. Verify the account email, repository visibility, branch, and contribution settings before expecting graph changes.

## Local execution and publishing

The generator creates local commits only. It never pushes, force-pushes, changes branches, or rewrites remote history. Inspect the resulting local history before deciding whether to publish it.

## Transparency

Generated commits are synthetic artwork data, not evidence of separate software-development tasks. Do not present them as a record of work that was not performed.
