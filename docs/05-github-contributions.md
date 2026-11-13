# 05 — Calendar Mapping, Git, and GitHub Contributions

This guide explains how a five-row artwork becomes dates in a seven-row calendar, how the program plans commits, and what happens when you publish them.

## 1. Understand the calendar

GitHub's contribution calendar is arranged in columns of weeks. Each column contains seven weekday rows, Sunday through Saturday.

| Calendar row | Weekday | Artwork row |
| --- | --- | --- |
| 0 | Sunday | Always empty |
| 1 | Monday | 0 |
| 2 | Tuesday | 1 |
| 3 | Wednesday | 2 |
| 4 | Thursday | 3 |
| 5 | Friday | 4 |
| 6 | Saturday | Always empty |

The artwork is five rows high, so it maps to Monday–Friday. Sunday and Saturday are deliberately excluded.

## 2. Understand calendar columns

The default date range is inclusive:

- Start: 2026-01-01
- End: 2026-09-30

The first Sunday on or before the start date is 2025-12-28. The last Sunday starting a week that intersects the end date is 2026-09-27. Therefore, the requested range intersects 40 Sunday-to-Saturday calendar columns.

The default `offset-weeks` value is 1. It reserves the first and last calendar columns, leaving:

```text
40 total columns - 1 first boundary column - 1 last boundary column
= 38 available artwork columns
```

The mapper places the artwork beginning one week after the first Sunday. Every active pixel must still map to a date inside the inclusive requested date range. If a pixel would land outside the range, planning fails with an error.

## 3. How a pixel becomes a date

The artwork uses coordinates `(x, y)`:

- `x` is the horizontal column in the artwork.
- `y` is the vertical row, where 0 is Monday and 4 is Friday.

For each active pixel, the mapper:

1. Finds the Sunday at or before the start date.
2. Moves forward by the reserved offset plus the pixel's `x` column.
3. Adds `y + 1` days to reach Monday through Friday.
4. Checks that the resulting date is inside the requested range.

The calendar module uses Python's `date` and `timedelta` objects to perform this arithmetic. It does not guess weekday positions from the current month view.

## 4. Preview the complete calendar

Run a dry run:

```bash
python scripts/generate.py
```

The output contains:

- The five-row artwork.
- A seven-row Sunday-to-Saturday calendar preview.
- One column for each of the 40 calendar weeks.
- The active-pixel count.
- The number of dates used.
- The planned commit count.

A dry run only calculates and prints a plan. It does not create commits.

## 5. Understand commits per pixel

By default, every filled pixel produces exactly one planned commit. Empty pixels produce none.

For the default artwork:

```text
Active pixels:  78
Dates used:     78
Commits planned: 78
```

These numbers are specific to the default `CODE IS ART` artwork and date settings. A different phrase or font can produce a different number.

The `--commits-per-pixel` option changes the number of commits planned for each filled pixel. The default is 1; increasing it is not necessary to mark a contribution date.

## 6. Local commits are not the same as a push

A Git commit is stored in the local repository. A push sends local commits to a remote repository such as GitHub.

Dry run:

```bash
python scripts/generate.py
```

Create local commits only after reviewing the plan:

```bash
python scripts/generate.py --execute
```

Inspect the result:

```bash
git log -10 --format="%h | %ad | %s" --date=short
git status --short
```

The generator does not push, switch branches, or rewrite remote history. Each execution creates a new set of empty commits. The current version does not detect a repeated execution, so do not run `--execute` again for the same plan unless you intentionally want another set of commits.

If you decide to publish, first confirm that you are on the intended branch and that the commits you want to send are the only outgoing commits:

```bash
git status
git branch --show-current
git log --oneline origin/main..HEAD
```

Only then push deliberately:

```bash
git push origin HEAD:main
```

Never use `--force` as a routine fix for a rejected push. Stop and inspect the branch histories first.

## 7. GitHub contribution eligibility

A commit appearing in repository history does not automatically guarantee that it appears on a profile contribution graph. GitHub applies eligibility rules. Among other requirements, the commit must be associated with the account through an email address added to that account, and it must be on an eligible branch or otherwise meet GitHub's contribution rules.

Check GitHub's current documentation before troubleshooting the graph:

https://docs.github.com/en/account-and-profile/concepts/contributions-on-your-profile

Also check the repository's visibility and your profile's contribution settings. The graph may take time to refresh.

## 8. Be transparent about generated activity

The commits produced by this project are synthetic artwork data. They are generated to map a visual pattern onto dates; they are not evidence that separate software-development tasks were performed on those dates.

Use this project as a programming and pixel-art experiment, and describe the generated history honestly.

## Key ideas to remember

- A calendar column represents one Sunday-to-Saturday week.
- Artwork row 0 maps to Monday, not Sunday.
- Artwork row 4 maps to Friday.
- Sunday and Saturday remain empty.
- A filled pixel becomes a planned commit; an empty pixel does not.
- Dry run, local commit creation, and pushing are three separate stages.
