import unittest
from itertools import product

from python.p0516_longest_palindromic_subsequence import Solution


def all_palindromic_choices(word):
    best = 0
    for mask in range(1 << len(word)):
        candidate = ''.join(character for index, character in enumerate(word) if mask & (1 << index))
        if candidate == candidate[::-1]:
            best = max(best, len(candidate))
    return best


class PalindromicSubsequenceTests(unittest.TestCase):
    def check(self, word, expected=None):
        if expected is None:
            expected = all_palindromic_choices(word)
        result = Solution().longestPalindromeSubseq(word)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_ternary_strings_against_all_position_masks(self):
        checks = 0
        for size in range(8):
            for characters in product('abc', repeat=size):
                self.check(''.join(characters))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_maximum_lengths_repetition_alternation_and_two_blocks(self):
        self.check('a' * 1000, 1000)
        self.check('ab' * 500, 999)
        self.check('a' * 500 + 'b' * 500, 500)
        self.check('bbbab', 4)
        self.check('cbbd', 2)


if __name__ == '__main__':
    unittest.main()
