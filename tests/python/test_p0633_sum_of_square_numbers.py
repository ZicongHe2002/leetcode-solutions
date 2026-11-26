import random
import unittest
from math import isqrt

from python.p0633_sum_of_square_numbers import Solution


def prime_exponent_criterion(value):
    if value == 0:
        return True
    factor = 2
    while factor * factor <= value:
        exponent = 0
        while value % factor == 0:
            value //= factor
            exponent += 1
        if factor % 4 == 3 and exponent % 2:
            return False
        factor = 3 if factor == 2 else factor + 2
    return value % 4 != 3


class TwoSquaresTests(unittest.TestCase):
    def check(self, value, expected):
        actual = Solution().judgeSquareSum(value)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, expected, value)

    def test_all_values_through_20000_against_enumerated_square_sums(self):
        limit = 20000
        squares = [value * value for value in range(isqrt(limit) + 1)]
        sums = {left + right for left in squares for right in squares
                if left + right <= limit}
        for value in range(limit + 1):
            self.check(value, value in sums)

    def test_large_values_against_prime_exponents_and_integer_boundaries(self):
        boundary = [0, 1, 2, 3, 4, 5, 8, 9, 2**31 - 1, 2**31 - 2,
                    46340**2, 46340**2 + 1, 46340**2 - 1, 2 * 32767**2]
        rng = random.Random(633)
        for value in boundary + [rng.randint(10**9, 2**31 - 1) for _ in range(200)]:
            self.check(value, prime_exponent_criterion(value))


if __name__ == '__main__':
    unittest.main()
