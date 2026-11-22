import statistics
import unittest
from itertools import combinations_with_replacement

from python.p0004_median_of_two_sorted_arrays import Solution


class MedianPartitionTests(unittest.TestCase):
    def check(self, first, second):
        before = (first[:], second[:])
        expected = float(statistics.median(sorted(first + second)))
        actual = Solution().findMedianSortedArrays(first, second)
        self.assertIs(type(actual), float)
        self.assertEqual(actual, expected)
        self.assertEqual((first, second), before)

    def test_all_small_sorted_pairs_against_materialized_median(self):
        arrays = [list(values) for size in range(5)
                  for values in combinations_with_replacement((-1, 0, 2), size)]
        checks = 0
        for first in arrays:
            for second in arrays:
                if first or second:
                    self.check(first, second)
                    checks += 1
        self.assertEqual((len(arrays), checks), (35, 1224))

    def test_length_limits_empty_side_and_value_extremes(self):
        self.check(list(range(-1000, 0)), list(range(1000)))
        self.check([-10**6] * 1000, [10**6] * 1000)
        self.check([], list(range(1000)))
        self.check([10**6], [])
        self.check([-10**6], [0, 10**6])
        self.check([1, 3], [2])
        self.check([1, 2], [3, 4])


if __name__ == '__main__':
    unittest.main()
