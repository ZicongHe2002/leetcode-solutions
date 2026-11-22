import unittest
from itertools import product

from python.p0724_find_pivot_index import Solution


def independent_side_sums(values):
    return next((index for index in range(len(values))
                 if sum(values[:index]) == sum(values[index + 1:])), -1)


class PivotIndexTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = independent_side_sums(values)
        result = Solution().pivotIndex(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_separate_side_sums(self):
        checks = 0
        for size in range(7):
            for values in product(range(-2, 3), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 19531)

    def test_maximum_lengths_leftmost_and_endpoint_pivots(self):
        self.check([0] * 10000, 0)
        self.check([1000, -1000] * 5000, -1)
        self.check([0] * 9999 + [1000], 9999)
        self.check([1000] + [0] * 9999, 0)
        self.check([0] * 5000 + [1000] + [0] * 4999, 5000)
        self.check([1, 7, 3, 6, 5, 6], 3)


if __name__ == '__main__':
    unittest.main()
