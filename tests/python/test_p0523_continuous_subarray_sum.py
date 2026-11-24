import unittest
from itertools import product

from python.p0523_continuous_subarray_sum import Solution


def all_intervals_at_least_two(values, divisor):
    return any(sum(values[start:end]) % divisor == 0 for start in range(len(values))
               for end in range(start + 2, len(values) + 1))


class DivisibleIntervalTests(unittest.TestCase):
    def check(self, values, divisor, expected=None):
        before = values[:]
        if expected is None:
            expected = all_intervals_at_least_two(values, divisor)
        result = Solution().checkSubarraySum(values, divisor)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_nonnegative_arrays_against_direct_slice_sums(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(4), repeat=size):
                arrays += 1
                for divisor in range(1, 9):
                    self.check(list(values), divisor)
                    checks += 1
        self.assertEqual((arrays, checks), (5461, 43688))

    def test_maximum_length_large_divisor_zero_and_distance(self):
        self.check([1] * 100000, 100000, True)
        self.check([1] * 99999, 100000, False)
        self.check([10**9, 10**9, 147483647], 2**31 - 1, True)
        self.check([10**9, 10**9, 147483646], 2**31 - 1, False)
        self.check([0, 0], 2**31 - 1, True)
        self.check([0], 1, False)
        self.check([6], 6, False)
        self.check([1, 0], 2, False)


if __name__ == '__main__':
    unittest.main()
