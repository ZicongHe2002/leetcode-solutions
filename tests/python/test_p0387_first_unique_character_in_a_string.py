from itertools import product
import unittest

from python.p0387_first_unique_character_in_a_string import Solution


def direct_first_unique(text):
    return next((index for index, letter in enumerate(text) if text.count(letter) == 1), -1)


class FirstUniqueCharacterTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = direct_first_unique(text)
        result = Solution().firstUniqChar(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_strings_against_direct_full_counts(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('abc', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_first_last_and_absent_unique_character(self):
        self.check('a' * 99999 + 'z', 99999)
        self.check('z' + 'a' * 99999, 0)
        self.check('ab' * 50000, -1)
        self.check('a' * 100000, -1)
        self.check('loveleetcode')


if __name__ == '__main__':
    unittest.main()
