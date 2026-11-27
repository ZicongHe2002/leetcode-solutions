import unittest
from itertools import product

from python.p0727_minimum_window_subsequence import Solution


def every_actual_window(source, target):
    for length in range(1, len(source) + 1):
        for left in range(len(source) - length + 1):
            window = source[left:left + length]
            unread = iter(window)
            if all(char in unread for char in target):
                return window
    return ''


class MinimumWindowSubsequenceTests(unittest.TestCase):
    def check(self, source, target, expected=None):
        result = Solution().minWindow(source, target)
        self.assertIs(type(result), str)
        self.assertEqual(result, every_actual_window(source, target) if expected is None else expected,
                         (source[:100], target))

    def test_all_short_binary_source_target_pairs_against_literal_window_enumeration(self):
        sources = [''.join(chars) for size in range(1, 8) for chars in product('ab', repeat=size)]
        targets = [''.join(chars) for size in range(1, 5) for chars in product('ab', repeat=size)]
        checked = 0
        for source, target in product(sources, targets):
            self.check(source, target)
            checked += 1
        self.assertEqual(checked, 7620)

    def test_leftmost_ties_order_repeated_characters_and_contract_boundaries(self):
        self.check('abcdebdde', 'bde', 'bcde')
        self.check('jmeqksfrsdcmsiwvaovztaqenprpvnbstl', 'u', '')
        self.check('a', 'aa', '')
        self.check('ab', 'ba', '')
        self.check('axbyaab', 'ab', 'ab')
        self.check('a' * 20000, 'a' * 100, 'a' * 100)
        self.check('a' * 19999 + 'b', 'a' * 99 + 'b', 'a' * 99 + 'b')
        self.check('ab' * 10000, 'z' * 100, '')


if __name__ == '__main__':
    unittest.main()
