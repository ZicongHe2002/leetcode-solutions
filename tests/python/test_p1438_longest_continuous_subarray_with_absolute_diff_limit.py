import unittest
from itertools import product

from python.p1438_longest_continuous_subarray_with_absolute_diff_limit import Solution


def all_interval_ranges(values, limit):
    return max((end - start for start in range(len(values))
                for end in range(start + 1, len(values) + 1)
                if max(values[start:end]) - min(values[start:end]) <= limit), default=0)


class BoundedRangeWindowTests(unittest.TestCase):
    def check(self, values, limit, expected=None):
        before = values[:]
        if expected is None:
            expected = all_interval_ranges(values, limit)
        result = Solution().longestSubarray(values, limit)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_limits_against_direct_extrema(self):
        arrays = checks = 0
        for size in range(8):
            for values in product((1, 2, 3), repeat=size):
                arrays += 1
                for limit in (0, 1, 2, 3, 10**9):
                    self.check(list(values), limit)
                    checks += 1
        self.assertEqual((arrays, checks), (3280, 16400))

    def test_maximum_lengths_duplicate_expiry_and_extreme_limits(self):
        self.check([7] * 100000, 0, 100000)
        self.check([1, 10**9] * 50000, 0, 1)
        self.check([1, 10**9] * 50000, 10**9, 100000)
        self.check(list(range(1, 100001)), 50000, 50001)
        self.check([1] * 49999 + [10**9] * 50001, 0, 50001)
        self.check([10, 1, 2, 4, 7, 2], 5, 4)


if __name__ == '__main__':
    unittest.main()
