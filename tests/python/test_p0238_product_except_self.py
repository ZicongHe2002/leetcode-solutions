import unittest
from itertools import product
from math import prod

from python.p0238_product_except_self import Solution


class SolutionTests(unittest.TestCase):
    def check(self, values, expected, *args):
        before = values[:]
        actual = Solution().productExceptSelf(values, *args)
        self.assertEqual(actual, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_excluded_index_products(self):
        checked = 0
        for size in range(2, 7):
            for values in product((-2, 0, 1, 2), repeat=size):
                expected = [prod(value for index, value in enumerate(values) if index != excluded)
                            for excluded in range(size)]
                self.check(list(values), expected)
                checked += 1
        self.assertEqual(checked, 5456)

    def test_maximum_length_zero_cases_and_integer_boundary(self):
        values = [1] * 100000
        self.check(values, values[:])
        values[50000] = 0
        expected = [0] * 100000
        expected[50000] = 1
        self.check(values, expected)
        values[90000] = 0
        self.check(values, [0] * 100000)
        self.check([-2] * 31, [1073741824] * 31)

if __name__ == '__main__':
    unittest.main()
