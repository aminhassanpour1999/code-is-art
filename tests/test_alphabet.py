import unittest

from code_is_art.alphabet import FONT, normalize_text, render_text, text_width


class AlphabetTests(unittest.TestCase):
    def test_every_glyph_is_five_by_five(self):
        for character, glyph in FONT.items():
            with self.subTest(character=character):
                self.assertEqual(len(glyph), 5)
                self.assertTrue(all(len(row) == 5 for row in glyph))
                self.assertTrue(all(set(row) <= {".", "#"} for row in glyph))

    def test_normalizes_lowercase_and_surrounding_whitespace(self):
        self.assertEqual(normalize_text("  code  "), "CODE")

    def test_rejects_unsupported_characters(self):
        with self.assertRaises(ValueError):
            render_text("CODE@")

    def test_rejects_blank_text(self):
        with self.assertRaises(ValueError):
            render_text("   ")

    def test_render_has_five_rows(self):
        matrix = render_text("ART")
        self.assertEqual(len(matrix), 5)
        self.assertTrue(all(isinstance(pixel, bool) for row in matrix for pixel in row))

    def test_width_matches_rendered_matrix_for_fixed_width_glyph(self):
        self.assertEqual(text_width("J"), len(render_text("J")[0]))

    def test_width_matches_rendered_matrix_for_words(self):
        self.assertEqual(text_width("CODE"), len(render_text("CODE")[0]))


if __name__ == "__main__":
    unittest.main()
