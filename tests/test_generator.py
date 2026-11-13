import unittest
from datetime import date

from code_is_art.alphabet import render_text
from code_is_art.generator import build_commit_plan, summarize_plan


class GeneratorTests(unittest.TestCase):
    def test_six_commits_per_active_pixel(self):
        matrix = render_text("A")
        plan = build_commit_plan(
            matrix, date(2026, 1, 1), date(2026, 9, 30), commits_per_pixel=6
        )
        active = sum(sum(row) for row in matrix)
        self.assertEqual(len(plan), active * 6)

    def test_plan_dates_are_inside_requested_window(self):
        plan = build_commit_plan(
            render_text("A"), date(2026, 1, 1), date(2026, 9, 30)
        )
        self.assertTrue(all(date(2026, 1, 1) <= item.date <= date(2026, 9, 30)
                            for item in plan))

    def test_summary(self):
        plan = build_commit_plan(
            render_text("A"), date(2026, 1, 1), date(2026, 9, 30)
        )
        summary = summarize_plan(plan)
        self.assertGreater(summary["active_pixels"], 0)
        self.assertEqual(summary["planned_commits"], summary["active_pixels"] * 6)


if __name__ == "__main__":
    unittest.main()
