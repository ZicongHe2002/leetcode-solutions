import unittest
from itertools import product

from python.p0058_length_of_last_word import Solution


class LastWordTests(unittest.TestCase):
    def check(self, value):
        words = value.split()
        expected = len(words[-1]) if words else 0
        result = Solution().lengthOfLastWord(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_legal_letter_space_inputs_against_split(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('ab ', repeat=size):
                value = ''.join(letters)
                if value.strip():
                    self.check(value)
                    checks += 1
        self.assertEqual(checks, 9832)

    def test_maximum_lengths_trailing_spaces_and_empty_extensions(self):
        self.check('a' * 10000)
        self.check(' ' * 9999 + 'a')
        self.check('Word' + ' ' * 9996)
        self.check('Hello World')
        for size in range(9):
            self.check(' ' * size)


if __name__ == '__main__':
    unittest.main()
