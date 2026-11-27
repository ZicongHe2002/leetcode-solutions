from itertools import product
import unittest

from python.p0487_max_consecutive_ones_ii import Solution


def explicit_flip_oracle(nums):
    best = 0
    for flip in [-1] + [index for index, value in enumerate(nums) if value == 0]:
        run = 0
        for index, value in enumerate(nums):
            run = run + 1 if value == 1 or index == flip else 0
            best = max(best, run)
    return best


class SingleZeroWindowTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().findMaxConsecutiveOnes(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, explicit_flip_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_short_binary_arrays_against_explicit_flip_positions(self):
        arrays = 0
        for size in range(13):
            for nums in product((0, 1), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 8191)

    def test_maximum_length_zero_boundaries_and_optional_flip(self):
        self.check([0] * 100000, 1)
        self.check([1] * 100000, 100000)
        self.check([1] * 50000 + [0] + [1] * 49999, 100000)
        self.check([1] * 49999 + [0, 0] + [1] * 49999, 50000)
        self.check([1, 0] * 50000, 3)
        self.check([1, 0, 1, 1, 0], 4)


if __name__ == '__main__':
    unittest.main()
