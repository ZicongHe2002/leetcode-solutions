import unittest
from itertools import combinations_with_replacement

from python.p0154_find_minimum_in_rotated_sorted_array_ii import Solution


class RotatedDuplicateMinimumTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        result = Solution().findMin(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, min(values))
        self.assertEqual(values, before)

    def test_all_small_multisets_and_rotations_against_scan(self):
        arrays = checks = 0
        for size in range(1, 9):
            for values in combinations_with_replacement((-1, 0, 1), size):
                arrays += 1
                for cut in range(size):
                    self.check(list(values[cut:] + values[:cut]))
                    checks += 1
        self.assertEqual((arrays, checks), (164, 990))

    def test_maximum_length_equal_values_and_extreme_minimum(self):
        self.check([5000] * 5000)
        self.check([5000] * 2499 + [-5000] + [5000] * 2500)
        self.check([5000] * 4999 + [-5000])
        self.check([-5000] + [5000] * 4999)
        self.check(list(range(-2500, 2500)))
        self.check([2, 2, 2, 0, 1])


if __name__ == '__main__':
    unittest.main()
