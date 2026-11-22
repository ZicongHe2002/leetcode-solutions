import unittest
from itertools import product

from python.p0974_subarray_sums_divisible_by_k import Solution


def all_divisible_slices(values, divisor):
    return sum(sum(values[start:end]) % divisor == 0 for start in range(len(values))
               for end in range(start + 1, len(values) + 1))


class RemainderCountTests(unittest.TestCase):
    def check(self, values, divisor, expected=None):
        before = values[:]
        if expected is None:
            expected = all_divisible_slices(values, divisor)
        result = Solution().subarraysDivByK(values, divisor)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_and_divisors_against_slices(self):
        arrays = checks = 0
        for size in range(7):
            for values in product(range(-2, 3), repeat=size):
                arrays += 1
                for divisor in range(2, 9):
                    self.check(list(values), divisor)
                    checks += 1
        self.assertEqual((arrays, checks), (19531, 136717))

    def test_maximum_lengths_negative_remainders_and_large_divisor(self):
        self.check([0] * 30000, 10000, 450015000)
        self.check([-10000] * 30000, 10000, 450015000)
        self.check([1] * 30000, 2, 225000000)
        self.check([-1, 1] * 15000, 10000, 225000000)
        self.check([1] * 30000, 10000, 30003)


if __name__ == '__main__':
    unittest.main()
