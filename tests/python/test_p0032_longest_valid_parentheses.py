import unittest
from itertools import product

from python.p0032_longest_valid_parentheses import Solution


def all_balanced_substrings(text):
    longest = 0
    for start in range(len(text)):
        balance = 0
        for end in range(start, len(text)):
            balance += 1 if text[end] == '(' else -1
            if balance < 0:
                break
            if balance == 0:
                longest = max(longest, end - start + 1)
    return longest


class LongestParenthesesTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = all_balanced_substrings(text)
        result = Solution().longestValidParentheses(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_parenthesis_string_against_substring_balances(self):
        checks = 0
        for size in range(11):
            for values in product('()', repeat=size):
                self.check(''.join(values))
                checks += 1
        self.assertEqual(checks, 2047)

    def test_maximum_lengths_deep_nesting_disjoint_pairs_and_invalid_boundaries(self):
        self.check('(' * 15000 + ')' * 15000, 30000)
        self.check('()' * 15000, 30000)
        self.check(')(' * 15000, 29998)
        self.check('(' * 30000, 0)
        self.check(')()())', 4)
        self.check('', 0)


if __name__ == '__main__':
    unittest.main()
