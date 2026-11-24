import unittest
from itertools import product

from python.p0189_rotate_array import Solution


def coordinate_oracle(nums, steps):
    if not nums:
        return []
    result = [None] * len(nums)
    for index, value in enumerate(nums):
        result[(index + steps) % len(nums)] = value
    return result


class RotateArrayTests(unittest.TestCase):
    def check(self, nums, steps):
        expected, size = coordinate_oracle(nums, steps), len(nums)
        self.assertIsNone(Solution().rotate(nums, steps))
        self.assertEqual(nums, expected)
        self.assertEqual(len(nums), size)

    def test_all_small_arrays_and_multiple_cycles_against_coordinate_map(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(-1, 2), repeat=size):
                arrays += 1
                for steps in range(2 * size + 3):
                    self.check(list(values), steps)
                    checks += 1
        self.assertEqual((arrays, checks), (1093, 15309))

    def test_examples_maximum_length_steps_and_integer_bounds(self):
        self.check([1, 2, 3, 4, 5, 6, 7], 3)
        self.check([-1, -100, 3, 99], 2)
        self.check([-2**31, 0, 2**31 - 1], 100000)
        self.check(list(range(100000)), 100000)
        self.check(list(range(100000)), 99999)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
