import unittest
from itertools import product

from python.p0011_container_with_most_water import Solution


class ContainerTests(unittest.TestCase):
    def check(self, height, expected):
        before = height[:]
        self.assertEqual(Solution().maxArea(height), expected)
        self.assertEqual(height, before)

    def test_small_arrays_against_all_position_pairs(self):
        checked = 0
        for size in range(2, 8):
            for values in product(range(4), repeat=size):
                expected = max((j - i) * min(values[i], values[j])
                               for i in range(size) for j in range(i + 1, size))
                self.check(list(values), expected)
                checked += 1
        self.assertEqual(checked, 21840)

    def test_examples_short_extensions_and_maximum_area(self):
        for height, expected in [([], 0), ([9], 0), ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
                                 ([1, 8, 2, 7, 1], 14), ([4, 4], 4), ([0, 7, 0], 0)]:
            self.check(height, expected)
        self.check([10000] * 100000, 999990000)
        self.check([0] * 100000, 0)


if __name__ == '__main__':
    unittest.main()
