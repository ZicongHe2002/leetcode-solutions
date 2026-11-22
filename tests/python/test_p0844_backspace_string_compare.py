from itertools import product
import unittest

from python.p0844_backspace_string_compare import Solution


def edited_text(text):
    visible = ''
    for letter in text:
        visible = visible[:-1] if letter == '#' else visible + letter
    return visible


class ReverseBackspaceComparisonTests(unittest.TestCase):
    def check(self, left, right):
        result = Solution().backspaceCompare(left, right)
        self.assertIs(type(result), bool)
        self.assertEqual(result, edited_text(left) == edited_text(right))

    def test_all_small_text_pairs_against_literal_editor(self):
        words = [''.join(chars) for size in range(1, 5)
                 for chars in product('ab#', repeat=size)]
        for left in words:
            for right in words:
                self.check(left, right)
        self.assertEqual(len(words) ** 2, 14400)

    def test_maximum_length_empty_edits_and_late_visible_characters(self):
        self.check('#' * 200, 'a#' * 100)
        self.check('a' * 99 + '#' * 99 + 'bc', 'bc')
        self.check('a' * 200, 'b' * 200)
        self.check('#' * 199 + 'a', 'a')
        self.check('ab#c', 'ad#c')
        self.check('a#c', 'b')


if __name__ == '__main__':
    unittest.main()
