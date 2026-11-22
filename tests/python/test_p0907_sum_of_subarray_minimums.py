import unittest
from itertools import product

from python.p0907_sum_of_subarray_minimums import Solution


def all_slice_minimum_sums(values):
    return sum(min(values[left:right]) for left in range(len(values))
               for right in range(left + 1, len(values) + 1)) % (10**9 + 7)


class MinimumContributionTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = all_slice_minimum_sums(values)
        result = Solution().sumSubarrayMins(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertGreaterEqual(result, 0)
        self.assertLess(result, 10**9 + 7)
        self.assertEqual(values, before)

    def test_all_small_positive_arrays_against_direct_slice_minima(self):
        checks = 0
        for size in range(9):
            for values in product((1, 2, 3), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 9841)

    def test_maximum_length_values_equal_ties_and_modulo(self):
        count, modulus = 30000, 10**9 + 7
        self.check([30000] * count, (30000 * count * (count + 1) // 2) % modulus)
        self.check([1] * count, count * (count + 1) // 2)
        expected = (count * (count + 1) * (count + 2) // 6) % modulus
        self.check(list(range(1, count + 1)), expected)
        self.check(list(range(count, 0, -1)), expected)
        self.check([2, 2, 2], 12)
        self.check([3, 1, 2, 4], 17)


if __name__ == '__main__':
    unittest.main()
