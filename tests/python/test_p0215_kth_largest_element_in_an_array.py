import unittest
from itertools import product

from python.p0215_kth_largest_element_in_an_array import Solution


class KthLargestTests(unittest.TestCase):
    def check(self, nums, k, expected=None):
        before = nums[:]
        if expected is None:
            expected = sorted(nums, reverse=True)[k - 1]
        result = Solution().findKthLargest(nums, k)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_and_ranks_against_full_sort(self):
        arrays = checks = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                arrays += 1
                for k in range(1, size + 1):
                    self.check(list(values), k)
                    checks += 1
        self.assertEqual((arrays, checks), (3279, 21324))

    def test_maximum_lengths_rank_endpoints_duplicates_and_extreme_values(self):
        self.check([10000] * 100000, 1, 10000)
        self.check([-10000] * 100000, 100000, -10000)
        values = [-10000, 10000] * 50000
        self.check(values, 50000, 10000)
        self.check(values, 50001, -10000)
        self.check([-3, -2, -1, 0, 1, 2, 3], 7, -3)
        self.check([1, 2, 2, 2, 3], 4, 2)


if __name__ == '__main__':
    unittest.main()
