import random
import unittest
from fractions import Fraction
from itertools import product

from python.p0644_maximum_average_subarray_ii import Solution


def all_long_enough_intervals(values, minimum_length):
    return max(Fraction(sum(values[start:end]), end - start)
               for start in range(len(values))
               for end in range(start + minimum_length, len(values) + 1))


class VariableAverageTests(unittest.TestCase):
    def check(self, values, minimum_length, expected=None):
        before = values[:]
        if expected is None:
            expected = all_long_enough_intervals(values, minimum_length)
        actual = Solution().findMaxAverage(values, minimum_length)
        self.assertIs(type(actual), float)
        self.assertAlmostEqual(actual, float(expected), delta=10**-5)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_seeded_cases_against_exact_interval_fractions(self):
        arrays = queries = 0
        for length in range(1, 7):
            for values in product((-2, 0, 3), repeat=length):
                arrays += 1
                for minimum_length in range(1, length + 1):
                    self.check(list(values), minimum_length)
                    queries += 1
        self.assertEqual((arrays, queries), (1092, 6015))
        rng = random.Random(644)
        for _ in range(200):
            length = rng.randint(1, 30)
            self.check([rng.randint(-10000, 10000) for _ in range(length)], rng.randint(1, length))

    def test_maximum_length_precision_eligibility_and_longer_optimum(self):
        self.check([-10000] * 10000, 3333, -10000)
        self.check([-10000, 10000] * 5000, 9999, Fraction(10000, 9999))
        self.check([10000] + [-1] * 9999, 10000, Fraction(1, 10000))
        self.check([10000] + [-1] * 9999, 9999, Fraction(2, 9999))
        self.check([-10000] * 9999 + [10000], 1, 10000)
        self.check([5, -10, 5], 2, 0)
        self.check([1, 12, -5, -6, 50, 3], 4, Fraction(51, 4))


if __name__ == '__main__':
    unittest.main()
