import unittest
from math import isqrt

from python.p0204_count_primes import Solution


def count_by_trial_division(limit):
    return sum(all(value % divisor for divisor in range(2, isqrt(value) + 1))
               for value in range(2, limit))


def count_by_euler_sieve(limit):
    composite = bytearray(limit)
    primes = []
    for value in range(2, limit):
        if not composite[value]:
            primes.append(value)
        for prime in primes:
            product = prime * value
            if product >= limit:
                break
            composite[product] = 1
            if value % prime == 0:
                break
    return len(primes)


class PrimeCountTests(unittest.TestCase):
    def check(self, value, expected):
        result = Solution().countPrimes(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_limit_against_trial_division(self):
        for value in range(501):
            self.check(value, count_by_trial_division(value))

    def test_maximum_limit_linear_sieve_and_strict_boundary(self):
        for value, known in ((1000000, 78498), (5000000, 348513)):
            expected = count_by_euler_sieve(value)
            self.assertEqual(expected, known)
            self.check(value, expected)
        for value, expected in ((0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (5, 2), (6, 3), (10, 4)):
            self.check(value, expected)


if __name__ == '__main__':
    unittest.main()
