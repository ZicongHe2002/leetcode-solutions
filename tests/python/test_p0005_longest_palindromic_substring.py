import unittest
from itertools import product

from python.p0005_longest_palindromic_substring import Solution


def all_intervals_oracle(text):
    best = ''
    for left in range(len(text)):
        for right in range(left + 1, len(text) + 1):
            candidate = text[left:right]
            if candidate == candidate[::-1] and len(candidate) > len(best):
                best = candidate
    return best


class LongestPalindromeTests(unittest.TestCase):
    def test_all_small_alphanumeric_strings_against_all_intervals(self):
        checks = 0
        for size in range(9):
            for letters in product('ab0', repeat=size):
                text = ''.join(letters)
                self.assertEqual(Solution().longestPalindrome(text), all_intervals_oracle(text))
                checks += 1
        self.assertEqual(checks, 9841)

    def test_centers_leftmost_ties_character_contract_and_maximum_length(self):
        for text, expected in [('babad', 'bab'), ('cbbd', 'bb'), ('Aa', 'A'),
                               ('A1b1A', 'A1b1A'), ('a' * 1000, 'a' * 1000),
                               ('a' * 500 + 'b' * 500, 'a' * 500), ('', '')]:
            self.assertEqual(Solution().longestPalindrome(text), expected)


if __name__ == '__main__':
    unittest.main()
