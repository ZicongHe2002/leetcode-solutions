from itertools import combinations_with_replacement
import unittest

from python.p0977_squares_of_a_sorted_array import Solution


class SortedSquaresTests(unittest.TestCase):
    def check_values(self, values):
        nums = list(values)
        result = Solution().sortedSquares(nums)
        self.assertEqual(result, sorted(value * value for value in values))
        self.assertEqual(nums, list(values))
        self.assertIsNot(result, nums)

    def test_small_sorted_arrays_and_integer_bounds(self):
        checked = 0
        for length in range(7):
            for values in combinations_with_replacement(range(-3, 4), length):
                with self.subTest(values=values):
                    self.check_values(values)
                    checked += 1
        self.assertEqual(checked, 1716)
        self.check_values((-10000, -10000, 0, 10000))


if __name__ == "__main__":
    unittest.main()
