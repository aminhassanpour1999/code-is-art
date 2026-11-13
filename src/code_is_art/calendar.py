"""Map five artwork rows onto Monday-Friday calendar dates."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import date, timedelta

from .renderer import matrix_dimensions

PixelMatrix = Sequence[Sequence[bool]]


def sunday_on_or_before(day: date) -> date:
    """Return the Sunday at the start of the week containing day."""
    return day - timedelta(days=(day.weekday() + 1) % 7)


def calendar_week_count(start: date, end: date) -> int:
    """Count Sunday-to-Saturday columns intersecting the date range."""
    if end < start:
        raise ValueError("End date must not be earlier than start date.")
    first = sunday_on_or_before(start)
    last = sunday_on_or_before(end)
    return ((last - first).days // 7) + 1


def map_art_to_dates(
    matrix: PixelMatrix,
    start: date,
    end: date,
    offset_weeks: int = 1,
) -> list[tuple[date, int, int]]:
    """Return (date, x, y) for active pixels, mapping rows to Mon-Fri.

    Sunday and Saturday are deliberately excluded. One calendar column is
    reserved at both boundaries by default, keeping artwork out of partial
    first and last weeks.
    """
    height, width = matrix_dimensions(matrix)
    if height != 5:
        raise ValueError("Artwork must have exactly five rows (Monday-Friday).")
    if end < start:
        raise ValueError("End date must not be earlier than start date.")
    if offset_weeks < 0:
        raise ValueError("offset_weeks must be zero or greater.")

    weeks = calendar_week_count(start, end)
    available_art_columns = weeks - offset_weeks - 1
    if width > available_art_columns:
        raise ValueError(
            f"Artwork is {width} columns wide but only "
            f"{max(available_art_columns, 0)} columns fit between the "
            "reserved boundary weeks."
        )

    first_sunday = sunday_on_or_before(start)
    mapped: list[tuple[date, int, int]] = []

    for y, row in enumerate(matrix):
        # Artwork row 0 is Monday; row 4 is Friday.
        day_offset = y + 1
        for x, active in enumerate(row):
            if not active:
                continue
            week_sunday = first_sunday + timedelta(weeks=offset_weeks + x)
            commit_day = week_sunday + timedelta(days=day_offset)
            if not start <= commit_day <= end:
                raise ValueError(
                    f"Pixel at x={x}, y={y} maps outside the date window: "
                    f"{commit_day.isoformat()}"
                )
            mapped.append((commit_day, x, y))

    return sorted(mapped, key=lambda item: (item[0], item[1], item[2]))


def render_calendar_matrix(
    matrix: PixelMatrix,
    start: date,
    end: date,
    offset_weeks: int = 1,
) -> list[list[bool]]:
    """Expand artwork into a seven-row Sunday-to-Saturday calendar matrix.

    The returned matrix has one column per calendar week. Sunday (row 0)
    and Saturday (row 6) are always empty. It is suitable for a full
    contribution-calendar preview.
    """
    weeks = calendar_week_count(start, end)
    first_sunday = sunday_on_or_before(start)
    calendar = [[False] * weeks for _ in range(7)]

    for day, _, _ in map_art_to_dates(matrix, start, end, offset_weeks):
        column = (day - first_sunday).days // 7
        row = day.weekday() + 1
        calendar[row][column] = True

    return calendar
