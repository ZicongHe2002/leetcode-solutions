import unittest
from itertools import product

from python.p0459_repeated_substring_pattern import Solution


def repeated_by_direct_blocks(text):
    return any(len(text) % length == 0 and text[:length] * (len(text) // length) == text
               for length in range(1, len(text) // 2 + 1))


class RepeatedSubstringTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = repeated_by_direct_blocks(text)
        result = Solution().repeatedSubstringPattern(text)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_binary_strings_against_direct_repetition(self):
        checks = 0
        for size in range(1, 13):
            for values in product('ab', repeat=size):
                self.check(''.join(values))
                checks += 1
        self.assertEqual(checks, 8190)

    def test_maximum_length_incomplete_period_wrong_tail_and_single_character(self):
        self.check('a' * 10000, True)
        self.check('ab' * 5000, True)
        self.check('abca' * 2500, True)
        self.check('a' * 9999 + 'b', False)
        self.check('abc' * 3333 + 'a', False)
        self.check('a', False)


if __name__ == '__main__':
    unittest.main()
