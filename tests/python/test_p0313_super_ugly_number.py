from itertools import combinations
import unittest

from python.p0313_super_ugly_number import Solution


def allowed_factor_oracle(value, primes):
    for prime in primes:
        while value % prime == 0:
            value //= prime
    return value == 1


def largest_prime_factors(limit):
    factors = [0] * (limit + 1)
    for prime in range(2, limit + 1):
        if factors[prime] == 0:
            for multiple in range(prime, limit + 1, prime):
                factors[multiple] = prime
    return factors


class SuperUglyCandidateStreamTests(unittest.TestCase):
    def check(self, n, primes, expected):
        before = primes[:]
        actual = Solution().nthSuperUglyNumber(n, primes)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected)
        self.assertEqual(primes, before)

    def test_all_small_prime_subsets_against_integer_factorization(self):
        subsets = 0
        for size in range(1, 6):
            for primes in combinations((2, 3, 5, 7, 11), size):
                expected = [value for value in range(1, 501) if allowed_factor_oracle(value, primes)]
                for n, value in enumerate(expected, 1):
                    self.check(n, list(primes), value)
                subsets += 1
        self.assertEqual(subsets, 31)

    def test_maximum_n_against_independent_prime_factor_sieve(self):
        factors = largest_prime_factors(10**6)
        primes = [value for value in range(2, 542) if factors[value] == value]
        self.assertEqual(len(primes), 100)
        expected = [1] + [value for value in range(2, 10**6 + 1) if factors[value] <= primes[-1]]
        self.assertGreaterEqual(len(expected), 100000)
        self.assertLessEqual(expected[99999], 2**31 - 1)
        self.check(100000, primes, expected[99999])
        self.check(31, [2], 1 << 30)
        self.check(1, [997], 1)
        self.check(12, [2, 7, 13, 19], 32)


if __name__ == '__main__':
    unittest.main()
