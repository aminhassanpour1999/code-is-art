#!/usr/bin/env python3
"""Command-line entry point for Code Is Art."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from code_is_art.alphabet import render_text  # noqa: E402
from code_is_art.calendar import calendar_week_count  # noqa: E402
from code_is_art.generator import (  # noqa: E402
    build_commit_plan,
    execute_local_plan,
    summarize_plan,
)
from code_is_art.renderer import render_ascii  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Turn text into pixel art and a Git commit plan."
    )
    parser.add_argument(
        "--text", default="CODE IS ART",
        help="Text to render (default: CODE IS ART).",
    )
    parser.add_argument(
        "--font", choices=("3x5", "5x5"), default="3x5",
        help="3x5 fits longer phrases; 5x5 supports digits and punctuation.",
    )
    parser.add_argument(
        "--start", type=date.fromisoformat, default=date(2026, 1, 1),
        help="Inclusive start date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--end", type=date.fromisoformat, default=date(2026, 9, 30),
        help="Inclusive end date (YYYY-MM-DD).",
    )
    parser.add_argument(
        "--commits-per-pixel", type=int, default=6,
        help="Number of local commits for each filled pixel (default: 6).",
    )
    parser.add_argument(
        "--offset-weeks", type=int, default=1,
        help="Empty calendar columns reserved at each boundary (default: 1).",
    )
    parser.add_argument(
        "--preview", action="store_true",
        help="Print the artwork and exit without building a commit plan.",
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Actually create local commits. Without this flag, the run is a dry run.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        matrix = render_text(args.text, compact=args.font == "3x5")
        print(f"\nArtwork: {args.text.upper()} ({args.font})")
        print(render_ascii(matrix))
        if args.preview:
            return 0

        weeks = calendar_week_count(args.start, args.end)
        plan = build_commit_plan(
            matrix, args.start, args.end,
            args.commits_per_pixel, args.offset_weeks,
        )
        summary = summarize_plan(plan)
        print("\nPlan")
        print(f"  Date window:     {args.start} through {args.end}")
        print(f"  Calendar weeks:  {weeks}")
        print(f"  Offset weeks:    {args.offset_weeks}")
        print(f"  Active pixels:   {summary['active_pixels']}")
        print(f"  Dates used:      {summary['dates_used']}")
        print(f"  Commits planned: {summary['planned_commits']}")

        if not args.execute:
            print("\nDRY RUN: no Git commits were created.")
            print("Review the plan, then add --execute to create local commits.")
            return 0

        created = execute_local_plan(plan, ROOT)
        print(f"\nCreated {created} local commits. Nothing was pushed to GitHub.")
        return 0
    except (ValueError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
