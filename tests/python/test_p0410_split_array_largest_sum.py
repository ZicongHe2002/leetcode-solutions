from itertools import combinations, product
import unittest

from python.p0410_split_array_largest_sum import Solution


def all_cut_sets_oracle(nums, k):
    best = sum(nums)
    for cuts in combinations(range(1, len(nums)), k - 1):
        endpoints = (0, *cuts, len(nums))
        maximum = max(sum(nums[start:end]) for start, end in zip(endpoints, endpoints[1:]))
        best = min(best, maximum)
    return best


class SplitMaximumCapacityTests(unittest.TestCase):
    def check(self, nums, k, expected=None):
        before = nums[:]
        actual = Solution().splitArray(nums, k)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_cut_sets_oracle(nums, k) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_nonnegative_arrays_and_partition_counts(self):
        arrays = queries = 0
        for size in range(1, 8):
            for nums in product((0, 1, 3), repeat=size):
                arrays += 1
                for k in range(1, size + 1):
                    self.check(list(nums), k)
                    queries += 1
        self.assertEqual((arrays, queries), (3279, 21324))

    def test_maximum_lengths_values_and_original_partition_bounds(self):
        self.check([7, 2, 5, 10, 8], 2, 18)
        self.check([10**6] * 1000, 1, 10**9)
        self.check([10**6] * 1000, 50, 20 * 10**6)
        self.check([10**6] * 50, 50, 10**6)
        self.check([0] * 1000, 50, 0)
        self.check([0] * 999 + [10**6], 50, 10**6)


if __name__ == '__main__':
    unittest.main()
