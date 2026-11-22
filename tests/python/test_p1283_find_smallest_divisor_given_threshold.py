import unittest
from itertools import product

from python.p1283_find_smallest_divisor_given_threshold import Solution


def enumerate_divisors_by_chunks(values, threshold):
    return next(divisor for divisor in range(1, max(values) + 1)
                if sum(len(range(0, value, divisor)) for value in values) <= threshold)


class SmallestDivisorTests(unittest.TestCase):
    def check(self, values, threshold, expected=None):
        before = values[:]
        if expected is None:
            expected = enumerate_divisors_by_chunks(values, threshold)
        result = Solution().smallestDivisor(values, threshold)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_small_positive_arrays_against_all_divisors_and_chunk_counts(self):
        arrays = checks = 0
        for size in range(1, 6):
            for values in product(range(1, 5), repeat=size):
                arrays += 1
                for threshold in range(size, sum(values) + 2):
                    self.check(list(values), threshold)
                    checks += 1
        self.assertEqual((arrays, checks), (1364, 12286))

    def test_maximum_length_values_thresholds_and_exact_rounding(self):
        self.check([10**6] * 50000, 50000, 10**6)
        self.check([10**6] * 50000, 10**6, 50000)
        self.check([1] * 50000, 10**6, 1)
        self.check([1, 2, 5, 9], 6, 5)
        self.check([19], 5, 4)


if __name__ == '__main__':
    unittest.main()
