import unittest
from itertools import product

from python.p0730_count_different_palindromic_subsequences import Solution


def actual_distinct_palindromes(text):
    strings = set()
    for mask in range(1, 1 << len(text)):
        candidate = ''.join(char for index, char in enumerate(text) if mask >> index & 1)
        if candidate == candidate[::-1]:
            strings.add(candidate)
    return len(strings)


class DistinctPalindromicSubsequenceTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().countPalindromicSubsequences(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_distinct_palindromes(text) if expected is None else expected, text[:100])
        self.assertTrue(0 <= result < 10**9 + 7)

    def test_all_short_ternary_strings_against_actual_subsequence_string_set(self):
        checked = 0
        for size in range(1, 8):
            for chars in product('abc', repeat=size):
                self.check(''.join(chars))
                checked += 1
        self.assertEqual(checked, 3279)

    def test_modular_example_duplicate_branches_and_thousand_character_certificates(self):
        self.check('bccb', 6)
        self.check('abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba', 104860361)
        for text in ('a', 'aa', 'aaa', 'aaaa', 'abca', 'abcda', 'abcdcba'):
            self.check(text)
        self.check('a' * 1000, 1000)
        self.check('a' * 500 + 'b' * 500, 1000)
        self.check('a' * 250 + 'b' * 500 + 'a' * 250, 126000)


if __name__ == '__main__':
    unittest.main()
