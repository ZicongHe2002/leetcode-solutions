import unittest
from itertools import product

from python.p0042_trapping_rain_water import Solution


class WaterTests(unittest.TestCase):
    def check(self, height, expected):
        before = height[:]
        self.assertEqual(Solution().trap(height), expected)
        self.assertEqual(height, before)

    def test_small_arrays_against_full_left_right_maxima(self):
        checked = 0
        for size in range(1, 8):
            for values in product(range(4), repeat=size):
                expected = sum(min(max(values[:i + 1]), max(values[i:])) - values[i] for i in range(size))
                self.check(list(values), expected)
                checked += 1
        self.assertEqual(checked, 21844)

    def test_basins_empty_extension_and_maximum_water(self):
        for height, expected in [([], 0), ([100000], 0), ([4, 2, 0, 3, 2, 5], 9),
                                 ([5, 1, 2, 1, 4], 8), ([3, 0, 3], 3)]:
            self.check(height, expected)
        self.check([100000] + [0] * 19998 + [100000], 1999800000)
        self.check(list(range(20000)), 0)
        self.check([5] * 20000, 0)


if __name__ == '__main__':
    unittest.main()
