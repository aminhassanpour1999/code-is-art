import unittest
from datetime import date

from code_is_art.alphabet import render_text
from code_is_art.generator import build_commit_plan, summarize_plan


START = date(2026, 1, 1)
END = date(2026, 9, 30)


class GeneratorTests(unittest.TestCase):
    def test_one_commit_per_active_pixel(self):
        matrix = render_text("A")
        plan = build_commit_plan(
            matrix, START, END, commits_per_pixel=1
        )
        active = sum(sum(row) for row in matrix)
        self.assertEqual(len(plan), active)

    def test_plan_dates_are_inside_requested_window(self):
        plan = build_commit_plan(render_text("A"), START, END)
        self.assertTrue(all(START <= item.date <= END for item in plan))

    def test_default_artwork_fits_and_uses_one_commit_per_pixel(self):
        matrix = render_text("CODE IS ART", compact=True)
        plan = build_commit_plan(matrix, START, END)
        active = sum(sum(row) for row in matrix)
        self.assertGreater(active, 0)
        self.assertEqual(len(plan), active)
        self.assertTrue(all(START <= item.date <= END for item in plan))
        self.assertTrue(all(item.date.weekday() < 5 for item in plan))

    def test_summary(self):
        plan = build_commit_plan(render_text("A"), START, END)
        summary = summarize_plan(plan)
        self.assertGreater(summary["active_pixels"], 0)
        self.assertEqual(
            summary["planned_commits"], summary["active_pixels"]
        )


if __name__ == "__main__":
    unittest.main()
