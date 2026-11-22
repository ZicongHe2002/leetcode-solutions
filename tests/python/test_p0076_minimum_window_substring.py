import unittest
from collections import Counter
from itertools import product

from python.p0076_minimum_window_substring import Solution


def all_interval_minimum(text, pattern):
    if not pattern:
        return ''
    wanted = Counter(pattern)
    for length in range(1, len(text) + 1):
        for start in range(len(text) - length + 1):
            candidate = text[start:start + length]
            counts = Counter(candidate)
            if all(counts[character] >= count for character, count in wanted.items()):
                return candidate
    return ''


class MinimumWindowTests(unittest.TestCase):
    def check(self, text, pattern, expected=None):
        if expected is None:
            expected = all_interval_minimum(text, pattern)
        result = Solution().minWindow(text, pattern)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)

    def test_all_small_binary_pairs_and_empty_extensions_against_all_intervals(self):
        texts = [''.join(chars) for size in range(7) for chars in product('ab', repeat=size)]
        patterns = [''.join(chars) for size in range(4) for chars in product('ab', repeat=size)]
        checks = 0
        for text in texts:
            for pattern in patterns:
                self.check(text, pattern)
                checks += 1
        self.assertEqual(checks, 1905)

    def test_maximum_lengths_repeated_demands_case_and_impossible_cover(self):
        self.check('a' * 99999 + 'b', 'ab', 'ab')
        self.check('a' * 100000, 'a' * 100000, 'a' * 100000)
        text = 'A' + 'b' * 99998 + 'C'
        self.check(text, 'AC', text)
        self.check('a' * 100000, 'B', '')
        self.check('ADOBECODEBANC', 'ABC', 'BANC')


if __name__ == '__main__':
    unittest.main()
