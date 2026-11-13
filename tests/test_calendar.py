import unittest
from datetime import date

from code_is_art.alphabet import render_text
from code_is_art.calendar import (
    calendar_week_count,
    map_art_to_dates,
    render_calendar_matrix,
    sunday_on_or_before,
)


class CalendarTests(unittest.TestCase):
    def test_sunday_alignment(self):
        self.assertEqual(sunday_on_or_before(date(2026, 1, 1)), date(2025, 12, 28))

    def test_project_window_has_forty_calendar_columns(self):
        self.assertEqual(calendar_week_count(date(2026, 1, 1), date(2026, 9, 30)), 40)

    def test_mapping_uses_weekdays_only(self):
        matrix = [[True] for _ in range(5)]
        mapped = map_art_to_dates(
            matrix, date(2026, 1, 1), date(2026, 9, 30), offset_weeks=1
        )
        self.assertEqual(len(mapped), 5)
        self.assertTrue(all(day.weekday() < 5 for day, _, _ in mapped))
        self.assertTrue(all(date(2026, 1, 1) <= day <= date(2026, 9, 30)
                            for day, _, _ in mapped))

    def test_full_calendar_preview_has_seven_rows_and_forty_columns(self):
        artwork = render_text("CODE IS ART", compact=True)
        calendar = render_calendar_matrix(
            artwork, date(2026, 1, 1), date(2026, 9, 30)
        )
        self.assertEqual(len(calendar), 7)
        self.assertTrue(all(len(row) == 40 for row in calendar))
        self.assertFalse(any(calendar[0]))
        self.assertFalse(any(calendar[6]))

    def test_calendar_preview_preserves_active_pixel_count(self):
        artwork = render_text("CODE IS ART", compact=True)
        calendar = render_calendar_matrix(
            artwork, date(2026, 1, 1), date(2026, 9, 30)
        )
        artwork_pixels = sum(sum(row) for row in artwork)
        calendar_pixels = sum(sum(row) for row in calendar)
        self.assertEqual(calendar_pixels, artwork_pixels)

    def test_rejects_artwork_that_does_not_fit(self):
        matrix = [[True] * 40 for _ in range(5)]
        with self.assertRaises(ValueError):
            map_art_to_dates(matrix, date(2026, 1, 1), date(2026, 9, 30), 1)

    def test_rejects_wrong_height(self):
        with self.assertRaises(ValueError):
            map_art_to_dates([[True]], date(2026, 1, 1), date(2026, 9, 30))


if __name__ == "__main__":
    unittest.main()
