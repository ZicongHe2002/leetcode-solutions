import unittest
from itertools import product

from python.p0712_minimum_ascii_delete_sum_for_two_strings import Solution


def subsequence_set(word):
    return {''.join(character for index, character in enumerate(word) if mask & (1 << index))
            for mask in range(1 << len(word))}


def maximum_kept_weight(first, second):
    common = subsequence_set(first) & subsequence_set(second)
    kept = max(sum(map(ord, word)) for word in common)
    return sum(map(ord, first)) + sum(map(ord, second)) - 2 * kept


class AsciiDeleteCostTests(unittest.TestCase):
    def check(self, first, second, expected=None):
        if expected is None:
            expected = maximum_kept_weight(first, second)
        result = Solution().minimumDeleteSum(first, second)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_string_pairs_against_weighted_common_subsequences(self):
        words = [''.join(chars) for size in range(5) for chars in product('ab', repeat=size)]
        checks = 0
        for first in words:
            for second in words:
                self.check(first, second)
                checks += 1
        self.assertEqual(checks, 961)

    def test_maximum_lengths_weights_blocks_and_empty_extension(self):
        self.check('a' * 1000, 'a' * 1000, 0)
        self.check('a' * 1000, 'z' * 1000, 219000)
        self.check('a' * 500 + 'z' * 500, 'z' * 500 + 'a' * 500, 97000)
        self.check('a' * 1000, 'a' * 999, 97)
        self.check('az', 'za', 194)
        self.check('sea', 'eat', 231)
        self.check('', 'z' * 1000, 122000)


if __name__ == '__main__':
    unittest.main()
