import unittest
from itertools import product

from python.p0525_contiguous_array import Solution


def all_balanced_slices(values):
    return max((end - start for start in range(len(values))
                for end in range(start + 1, len(values) + 1)
                if values[start:end].count(0) == values[start:end].count(1)), default=0)


class BalancedPrefixTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_balanced_slices(values)
        result = Solution().findMaxLength(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_binary_arrays_against_direct_counts(self):
        checks = 0
        for size in range(13):
            for values in product((0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 8191)

    def test_maximum_lengths_first_prefix_and_unequal_blocks(self):
        self.check([0] * 100000, 0)
        self.check([1] * 100000, 0)
        self.check([0, 1] * 50000, 100000)
        self.check([0] * 49999 + [1] * 50001, 99998)
        self.check([0, 1, 1, 0], 4)


if __name__ == '__main__':
    unittest.main()
