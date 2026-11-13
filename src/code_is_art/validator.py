"""Validation helpers for artwork and commit plans."""

from __future__ import annotations

from datetime import date
from collections.abc import Sequence

from .renderer import matrix_dimensions

PixelMatrix = Sequence[Sequence[bool]]


def validate_matrix(matrix: PixelMatrix) -> None:
    """Raise ValueError unless matrix is a rectangular five-row bitmap."""
    height, _ = matrix_dimensions(matrix)
    if height != 5:
        raise ValueError("Artwork must contain exactly five rows.")
    if any(not isinstance(pixel, bool) for row in matrix for pixel in row):
        raise ValueError("Every matrix cell must be a Boolean value.")


def validate_date_window(start: date, end: date) -> None:
    """Validate an inclusive, forward-moving date range."""
    if end < start:
        raise ValueError("End date must not be earlier than start date.")


def validate_commits_per_pixel(count: int) -> None:
    """Require a positive number of commits per active pixel."""
    if isinstance(count, bool) or count < 1:
        raise ValueError("commits_per_pixel must be a positive integer.")
