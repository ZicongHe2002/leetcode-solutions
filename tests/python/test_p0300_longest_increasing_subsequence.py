import unittest
from itertools import product

from python.p0300_longest_increasing_subsequence import Solution


def subsequence_oracle(nums):
    largest = 0
    for mask in range(1 << len(nums)):
        selected = [value for index, value in enumerate(nums) if mask & (1 << index)]
        if all(a < b for a, b in zip(selected, selected[1:])):
            largest = max(largest, len(selected))
    return largest


class IncreasingSubsequenceTests(unittest.TestCase):
    def check(self, nums, expected):
        before = nums[:]
        self.assertEqual(Solution().lengthOfLIS(nums), expected)
        self.assertEqual(nums, before)

    def test_all_small_arrays_against_index_subsequence_oracle(self):
        checks = 0
        for size in range(7):
            for values in product(range(-1, 3), repeat=size):
                self.check(list(values), subsequence_oracle(values))
                checks += 1
        self.assertEqual(checks, 5461)

    def test_examples_strictness_and_maximum_length(self):
        self.check([10, 9, 2, 5, 3, 7, 101, 18], 4)
        self.check([], 0)
        self.check([2, 2, 2], 1)
        self.check(list(range(2500)), 2500)
        self.check(list(range(2499, -1, -1)), 1)
        self.check([10000] * 2500, 1)
        self.check([-10000, 10000] * 1250, 2)


if __name__ == '__main__':
    unittest.main()
