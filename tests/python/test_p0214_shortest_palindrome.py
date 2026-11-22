import unittest
from itertools import product

from python.p0214_shortest_palindrome import Solution


def shortest_by_direct_prefix_checks(text):
    for length in range(len(text), -1, -1):
        prefix = text[:length]
        if prefix == prefix[::-1]:
            return text[length:][::-1] + text
    raise AssertionError('The empty prefix is palindromic')


class ShortestPalindromeTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = shortest_by_direct_prefix_checks(text)
        result = Solution().shortestPalindrome(text)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(result, result[::-1])
        self.assertTrue(result.endswith(text))

    def test_all_small_binary_strings_against_direct_prefix_reversals(self):
        checks = 0
        for size in range(11):
            for values in product('ab', repeat=size):
                self.check(''.join(values))
                checks += 1
        self.assertEqual(checks, 2047)

    def test_maximum_length_long_prefix_single_prefix_and_alternation(self):
        self.check('a' * 50000, 'a' * 50000)
        self.check('a' * 49999 + 'b', 'b' + 'a' * 49999 + 'b')
        self.check('b' + 'a' * 49999, 'a' * 49999 + 'b' + 'a' * 49999)
        self.check('ab' * 25000, 'b' + 'ab' * 25000)
        self.check('', '')


if __name__ == '__main__':
    unittest.main()
