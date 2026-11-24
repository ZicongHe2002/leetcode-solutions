import unittest
from itertools import product

from python.p0075_sort_colors import Solution


class ColorSortTests(unittest.TestCase):
    def check(self, nums):
        expected, size = sorted(nums), len(nums)
        self.assertIsNone(Solution().sortColors(nums))
        self.assertEqual(nums, expected)
        self.assertEqual(len(nums), size)

    def test_all_small_color_arrays_against_library_sort(self):
        checks = 0
        for size in range(9):
            for values in product(range(3), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9841)

    def test_examples_maximum_length_and_empty_extension(self):
        self.check([2, 0, 2, 1, 1, 0])
        for value in range(3):
            self.check([value] * 300)
        self.check([2] * 100 + [1] * 100 + [0] * 100)
        self.check([])


if __name__ == '__main__':
    unittest.main()
