import unittest
from collections import Counter
from itertools import combinations_with_replacement

from python.p0373_find_k_pairs_with_smallest_sums import Solution


class SmallestPairTests(unittest.TestCase):
    def check(self, nums1, nums2, k, expected=None):
        before1, before2 = nums1[:], nums2[:]
        result = Solution().kSmallestPairs(nums1, nums2, k)
        self.assertEqual(len(result), k)
        self.assertTrue(all(type(pair) is list and len(pair) == 2 for pair in result))
        self.assertTrue(all(type(value) is int for pair in result for value in pair))
        actual = Counter(map(tuple, result))
        if expected is None:
            available = Counter((first, second) for first in nums1 for second in nums2)
            self.assertFalse(actual - available)
            expected_sums = sorted(first + second for first in nums1 for second in nums2)[:k]
            self.assertEqual(sorted(sum(pair) for pair in result), expected_sums)
        else:
            self.assertEqual(actual, Counter(map(tuple, expected)))
        self.assertEqual(nums1, before1)
        self.assertEqual(nums2, before2)

    def test_all_small_sorted_array_pairs_against_cartesian_product(self):
        arrays = [values for size in range(1, 5) for values in combinations_with_replacement((-1, 0, 2), size)]
        cases = checks = 0
        for first in arrays:
            for second in arrays:
                cases += 1
                for k in range(1, min(10, len(first) * len(second)) + 1):
                    self.check(list(first), list(second), k)
                    checks += 1
        self.assertEqual((len(arrays), cases, checks), (34, 1156, 9075))

    def test_maximum_lengths_pair_limit_single_row_column_duplicates_and_extremes(self):
        self.check([0] * 100000, [0] * 100000, 10000, [[0, 0]] * 10000)
        self.check([-10**9], [10**9] * 100000, 10000, [[-10**9, 10**9]] * 10000)
        self.check(list(range(100000)), [0], 10000, [[value, 0] for value in range(10000)])
        self.check([-10**9, 10**9], [-10**9, 10**9], 1, [[-10**9, -10**9]])


if __name__ == '__main__':
    unittest.main()
