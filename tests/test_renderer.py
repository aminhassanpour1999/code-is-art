import unittest

from code_is_art.alphabet import render_text
from code_is_art.renderer import count_active_pixels, matrix_dimensions, render_ascii


class RendererTests(unittest.TestCase):
    def test_dimensions(self):
        self.assertEqual(matrix_dimensions(render_text("A")), (5, 5))

    def test_ascii_has_five_lines(self):
        self.assertEqual(len(render_ascii(render_text("A")).splitlines()), 5)

    def test_counts_active_pixels(self):
        self.assertEqual(count_active_pixels([[True, False], [True, True]]), 3)

    def test_rejects_ragged_matrix(self):
        with self.assertRaises(ValueError):
            matrix_dimensions([[True, False], [True]])

    def test_rejects_empty_matrix(self):
        with self.assertRaises(ValueError):
            matrix_dimensions([])


if __name__ == "__main__":
    unittest.main()
