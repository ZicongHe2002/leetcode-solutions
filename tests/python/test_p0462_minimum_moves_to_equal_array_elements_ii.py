from itertools import product
import unittest

from python.p0462_minimum_moves_to_equal_array_elements_ii import Solution


def every_integer_target_oracle(nums):
    return min(sum(abs(value - target) for value in nums) for target in range(min(nums), max(nums) + 1))


class MedianAbsoluteDistanceTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().minMoves2(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_integer_target_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_signed_arrays_against_every_integer_target(self):
        arrays = 0
        for size in range(1, 8):
            for nums in product((-2, 0, 3), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 3279)

    def test_maximum_length_even_medians_and_value_bounds(self):
        self.check([1, 10, 2, 9], 16)
        self.check([-10**9, 10**9], 2 * 10**9)
        self.check([0] * 50000 + [10000] * 50000, 500000000)
        self.check([-10**9] * 100000, 0)
        self.check([10**9], 0)


if __name__ == '__main__':
    unittest.main()
