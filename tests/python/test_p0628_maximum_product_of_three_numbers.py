import unittest
from itertools import combinations, product

from python.p0628_maximum_product_of_three_numbers import Solution


def every_index_triple(values):
    return max(values[a] * values[b] * values[c]
               for a, b, c in combinations(range(len(values)), 3))


class ThreeNumberProductTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = every_index_triple(values)
        actual = Solution().maximumProduct(values)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected, values if len(values) < 10 else None)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_index_triples(self):
        checks = 0
        for size in range(3, 7):
            for values in product(range(-3, 4), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 137200)

    def test_maximum_length_signs_zeros_and_multiplicity(self):
        self.check([-1000, -1000] + [1] * 9997 + [1000], 10**9)
        self.check([-1000] * 9997 + [-3, -2, -1], -6)
        self.check([1000] * 10000, 10**9)
        self.check([0] * 10000, 0)
        self.check([-1000, 0, 1000], 0)
        self.check([1, 2, -3], -6)
        self.check([-10, -10, 5, 2], 500)


if __name__ == '__main__':
    unittest.main()
