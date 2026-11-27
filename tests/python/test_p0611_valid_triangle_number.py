from itertools import combinations, product
from math import comb
import unittest

from python.p0611_valid_triangle_number import Solution


def every_index_triple(values):
    return sum(a + b > c and a + c > b and b + c > a for a, b, c in combinations(values, 3))


class TriangleCountTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        result = Solution().triangleNumber(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_nonnegative_arrays_against_every_index_triple(self):
        cases = 0
        for size in range(9):
            for values in product((0, 1, 2, 3), repeat=size):
                self.check(list(values), every_index_triple(values))
                cases += 1
        self.assertEqual(cases, 87381)

    def test_thousand_elements_zero_sides_multiplicity_and_strict_equality(self):
        self.check([1000] * 1000, comb(1000, 3))
        self.check([0] * 1000, 0)
        self.check([0] * 500 + [1000] * 500, comb(500, 3))
        self.check([0] * 997 + [3, 4, 5], 1)
        self.check([1, 1, 2], 0)
        self.check([2, 2, 3, 4], 3)
        self.check([4, 2, 3, 4], 4)


if __name__ == '__main__':
    unittest.main()
