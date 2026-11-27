from itertools import product
import unittest

from python.p0396_rotate_function import Solution


def explicit_rotation_oracle(values):
    if not values:
        return 0
    weights = []
    for shift in range(len(values)):
        rotated = values[-shift:] + values[:-shift] if shift else values[:]
        weights.append(sum(index * value for index, value in enumerate(rotated)))
    return max(weights)


class RotationWeightRecurrenceTests(unittest.TestCase):
    def check(self, nums, expected=None):
        before = nums[:]
        actual = Solution().maxRotateFunction(nums)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, explicit_rotation_oracle(nums) if expected is None else expected)
        self.assertEqual(nums, before)

    def test_all_small_signed_arrays_against_physical_rotations(self):
        arrays = 0
        for size in range(8):
            for nums in product((-2, 0, 3), repeat=size):
                self.check(list(nums))
                arrays += 1
        self.assertEqual(arrays, 3280)

    def test_maximum_length_negative_results_and_value_bounds(self):
        self.check([4, 3, 2, 6], 26)
        self.check([-1, -2, -3], -5)
        self.check([-100, 100], 100)
        self.check([100], 0)
        self.check([0] * 100000, 0)
        self.check([-1, 1] * 50000, 50000)
        self.check([1] + [0] * 99999, 99999)


if __name__ == '__main__':
    unittest.main()
