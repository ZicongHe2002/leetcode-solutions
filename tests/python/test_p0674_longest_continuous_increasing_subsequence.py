import unittest
from itertools import product

from python.p0674_longest_continuous_increasing_subsequence import Solution


def all_intervals(values):
    return max((end - start for start in range(len(values))
                for end in range(start + 1, len(values) + 1)
                if all(values[first] < values[second]
                       for first in range(start, end)
                       for second in range(first + 1, end))), default=0)


class ContinuousIncreaseTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        result = Solution().findLengthOfLCIS(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_intervals(values) if expected is None else expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_all_interval_pairs(self):
        checked = 0
        for size in range(9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 9841)

    def test_maximum_length_strictness_contiguity_and_signed_boundaries(self):
        self.check(list(range(-5000, 5000)), 10000)
        self.check(list(range(10000, 0, -1)), 1)
        self.check([7] * 10000, 1)
        self.check(list(range(5000)) * 2, 5000)
        self.check([-10**9, 10**9] * 5000, 2)
        self.check([1, 3, 5, 4, 7], 3)


if __name__ == '__main__':
    unittest.main()
