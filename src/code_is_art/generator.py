"""Build and optionally execute a local Git commit plan."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from datetime import date, datetime, time, timezone
from pathlib import Path

from .calendar import map_art_to_dates
from .renderer import count_active_pixels
from .validator import (
    validate_commits_per_pixel,
    validate_date_window,
    validate_matrix,
)


@dataclass(frozen=True)
class PlannedCommit:
    date: date
    x: int
    y: int
    sequence: int
    total_for_pixel: int

    @property
    def message(self) -> str:
        return (
            f"art: pixel ({self.x},{self.y}) "
            f"{self.sequence}/{self.total_for_pixel}"
        )


def build_commit_plan(
    matrix: list[list[bool]],
    start: date,
    end: date,
    commits_per_pixel: int = 6,
    offset_weeks: int = 1,
) -> list[PlannedCommit]:
    """Create one planned commit per configured count for each active pixel."""
    validate_matrix(matrix)
    validate_date_window(start, end)
    validate_commits_per_pixel(commits_per_pixel)

    pixels = map_art_to_dates(matrix, start, end, offset_weeks)
    plan = [
        PlannedCommit(day, x, y, sequence, commits_per_pixel)
        for day, x, y in pixels
        for sequence in range(1, commits_per_pixel + 1)
    ]
    return sorted(plan, key=lambda item: (item.date, item.y, item.x, item.sequence))


def _git_root(cwd: Path) -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip())


def execute_local_plan(plan: list[PlannedCommit], cwd: Path | None = None) -> int:
    """Create local empty commits with explicit author and committer dates.

    This function never pushes, changes branches, or rewrites existing history.
    """
    working_directory = (cwd or Path.cwd()).resolve()
    _git_root(working_directory)

    for item in plan:
        timestamp = datetime.combine(
            item.date, time(hour=12), tzinfo=timezone.utc
        ).isoformat()
        environment = os.environ.copy()
        environment["GIT_AUTHOR_DATE"] = timestamp
        environment["GIT_COMMITTER_DATE"] = timestamp
        subprocess.run(
            ["git", "commit", "--allow-empty", "-m", item.message],
            cwd=working_directory,
            env=environment,
            check=True,
            capture_output=True,
            text=True,
        )
    return len(plan)


def summarize_plan(plan: list[PlannedCommit]) -> dict[str, int]:
    """Return useful totals for a dry-run summary."""
    return {
        "active_pixels": len({(item.x, item.y) for item in plan}),
        "planned_commits": len(plan),
        "dates_used": len({item.date for item in plan}),
    }
