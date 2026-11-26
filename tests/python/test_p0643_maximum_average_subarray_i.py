import unittest
from fractions import Fraction
from itertools import product

from python.p0643_maximum_average_subarray_i import Solution


def all_fixed_windows(values, size):
    return max(Fraction(sum(values[start:start + size]), size)
               for start in range(len(values) - size + 1))


class FixedAverageTests(unittest.TestCase):
    def check(self, values, size, expected=None):
        before = values[:]
        if expected is None:
            expected = all_fixed_windows(values, size)
        actual = Solution().findMaxAverage(values, size)
        self.assertIs(type(actual), float)
        self.assertAlmostEqual(actual, float(expected), delta=10**-5)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_and_window_lengths_against_fractions(self):
        arrays = queries = 0
        for length in range(1, 9):
            for values in product((-3, 0, 4), repeat=length):
                arrays += 1
                for size in range(1, length + 1):
                    self.check(list(values), size)
                    queries += 1
        self.assertEqual((arrays, queries), (9840, 73812))

    def test_maximum_length_negative_initialization_and_extreme_values(self):
        self.check([-10000] * 100000, 33333, -10000)
        values = [10000] * 50000 + [-10000] * 50000
        self.check(values, 50000, 10000)
        self.check(values, 100000, 0)
        self.check(values, 1, 10000)
        self.check([1, 12, -5, -6, 50, 3], 4, Fraction(51, 4))
        self.check([-5], 1, -5)


if __name__ == '__main__':
    unittest.main()
