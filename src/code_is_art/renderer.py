"""Utilities for validating and displaying pixel matrices."""

from __future__ import annotations

from collections.abc import Sequence

PixelMatrix = Sequence[Sequence[bool]]


def matrix_dimensions(matrix: PixelMatrix) -> tuple[int, int]:
    """Return (height, width), rejecting empty or ragged matrices."""
    if not matrix:
        raise ValueError("Pixel matrix must not be empty.")
    width = len(matrix[0])
    if width == 0:
        raise ValueError("Pixel matrix rows must not be empty.")
    if any(len(row) != width for row in matrix):
        raise ValueError("Pixel matrix must be rectangular.")
    return len(matrix), width


def render_ascii(
    matrix: PixelMatrix,
    filled: str = "#",
    empty: str = ".",
    separator: str = "",
) -> str:
    """Render a Boolean matrix as readable text."""
    matrix_dimensions(matrix)
    if len(filled) != 1 or len(empty) != 1:
        raise ValueError("Pixel symbols must each be one character.")
    return "\n".join(
        separator.join(filled if pixel else empty for pixel in row)
        for row in matrix
    )


def count_active_pixels(matrix: PixelMatrix) -> int:
    """Count filled cells in a pixel matrix."""
    matrix_dimensions(matrix)
    return sum(bool(pixel) for row in matrix for pixel in row)
