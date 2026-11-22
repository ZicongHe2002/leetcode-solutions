import unittest
from itertools import product

from python.p0239_sliding_window_maximum import Solution


class SlidingMaximumTests(unittest.TestCase):
    def check(self, nums, k, expected=None):
        before = nums[:]
        if expected is None:
            expected = [max(nums[start:start + k]) for start in range(len(nums) - k + 1)]
        result = Solution().maxSlidingWindow(nums, k)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_and_window_sizes_against_direct_maxima(self):
        arrays = checks = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                arrays += 1
                for k in range(1, size + 1):
                    self.check(list(values), k)
                    checks += 1
        self.assertEqual((arrays, checks), (3279, 21324))

    def test_maximum_lengths_duplicate_expiry_periodic_values_and_window_endpoints(self):
        values = [10000, -10000] * 50000
        self.check(values, 1, values[:])
        self.check(values, 100000, [10000])
        self.check(values, 2, [10000] * 99999)
        periodic = [index % 20001 - 10000 for index in range(100000)]
        self.check(periodic, 20001, [10000] * 80000)
        decreasing = list(range(10000, -10001, -1))
        self.check(decreasing, 10000, decreasing[:10002])


if __name__ == '__main__':
    unittest.main()
