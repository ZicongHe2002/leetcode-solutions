from itertools import product
import unittest

from python.p0456_132_pattern import Solution


def every_ordered_index_triple_oracle(nums):
    return any(nums[first] < nums[third] < nums[second]
               for first in range(len(nums)) for second in range(first + 1, len(nums))
               for third in range(second + 1, len(nums)))


class Strict132WitnessTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().find132pattern(nums)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, every_ordered_index_triple_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_signed_arrays_against_original_triple_condition(self):
        arrays = 0
        for size in range(9):
            for nums in product((-1, 0, 2), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 9841)

    def test_maximum_length_strict_equalities_and_value_bounds(self):
        self.check(list(range(200000)), False)
        self.check(list(range(200000, 0, -1)), False)
        self.check([-10**9, 10**9] + [0] * 199998, True)
        self.check([1, 2, 2], False)
        self.check([2, 2, 1], False)
        self.check([3, 1, 4, 2], True)
        self.check([-1, 3, 2, 0], True)


if __name__ == '__main__':
    unittest.main()
