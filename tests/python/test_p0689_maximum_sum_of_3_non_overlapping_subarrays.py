import random
import unittest
from itertools import combinations, product

from python.p0689_maximum_sum_of_3_non_overlapping_subarrays import Solution


def all_three_intervals(nums, k):
    choices = (starts for starts in combinations(range(len(nums) - k + 1), 3)
               if starts[0] + k <= starts[1] and starts[1] + k <= starts[2])
    return list(min(choices, key=lambda starts: (-sum(sum(nums[i:i + k]) for i in starts), starts)))


class ThreeSubarraySumTests(unittest.TestCase):
    def check(self, nums, k, expected=None):
        before = nums[:]
        result = Solution().maxSumOfThreeSubarrays(nums, k)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(index) is int for index in result))
        self.assertEqual(result, all_three_intervals(nums, k) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_positive_arrays_and_lengths_against_every_interval_triple(self):
        arrays = checked = 0
        for size in range(3, 11):
            for values in product((1, 2), repeat=size):
                arrays += 1
                for k in range(1, size // 3 + 1):
                    self.check(list(values), k)
                    checked += 1
        self.assertEqual((arrays, checked), (2040, 5560))
        rng = random.Random(689)
        for _ in range(200):
            size = rng.randrange(3, 21)
            self.check([rng.randrange(1, 65536) for _ in range(size)], rng.randrange(1, size // 3 + 1))

    def test_twenty_thousand_elements_extreme_k_ties_and_sparse_peaks(self):
        self.check([65535] * 20000, 1, [0, 1, 2])
        self.check([65535] * 20000, 6666, [0, 6666, 13332])
        peaks = [1] * 20000
        for index in (0, 10000, 19999):
            peaks[index] = 65535
        self.check(peaks, 1, [0, 10000, 19999])
        self.check(peaks, 2, [0, 9999, 19998])
        self.check([1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5])
        self.check([1, 2, 1, 2, 1, 2, 1, 2, 1], 2, [0, 2, 4])


if __name__ == '__main__':
    unittest.main()
