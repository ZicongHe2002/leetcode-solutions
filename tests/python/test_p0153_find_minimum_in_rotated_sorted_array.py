import unittest
from itertools import combinations

from python.p0153_find_minimum_in_rotated_sorted_array import Solution


class MinimumTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        self.assertEqual(Solution().findMin(values), expected)
        self.assertEqual(values, before)

    def test_all_small_subsets_and_rotations_against_linear_min(self):
        checked = 0
        for size in range(1, 8):
            for subset in combinations(range(-3, 4), size):
                for offset in range(size):
                    values = list(subset[offset:] + subset[:offset])
                    self.check(values, min(values))
                    checked += 1
        self.assertEqual(checked, 448)

    def test_value_endpoints_singletons_and_maximum_length(self):
        for values, expected in [([4, 5, 6, 7, 0, 1, 2], 0), ([-5000], -5000),
                                 ([5000, -5000], -5000), ([0, 5000, -5000], -5000)]:
            self.check(values, expected)
        ordered = list(range(-2500, 2500))
        for offset in (0, 1, 1234, 4999):
            self.check(ordered[offset:] + ordered[:offset], -2500)


if __name__ == '__main__':
    unittest.main()
