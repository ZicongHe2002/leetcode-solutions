import unittest
from itertools import product

from python.p0084_largest_rectangle_in_histogram import Solution


def all_interval_rectangles(values):
    return max((min(values[left:right]) * (right - left) for left in range(len(values))
                for right in range(left + 1, len(values) + 1)), default=0)


class HistogramAreaTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_interval_rectangles(values)
        result = Solution().largestRectangleArea(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_heights_against_all_interval_rectangles(self):
        checks = 0
        for size in range(8):
            for values in product(range(4), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 21845)

    def test_maximum_length_height_plateaus_zeros_and_monotonic_shapes(self):
        self.check([10000] * 100000, 10**9)
        self.check([0] * 100000, 0)
        self.check([0, 10000] * 50000, 10000)
        self.check(list(range(1, 10001)), (10001**2) // 4)
        self.check(list(range(10000, 0, -1)), (10001**2) // 4)
        self.check([2, 1, 5, 6, 2, 3], 10)


if __name__ == '__main__':
    unittest.main()
