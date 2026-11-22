import unittest

from python.p0263_ugly_number import Solution


def general_prime_factor_reference(value):
    if value <= 0:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            if divisor not in (2, 3, 5):
                return False
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    return value in (1, 2, 3, 5)


class AllowedPrimeFactorTests(unittest.TestCase):
    def check(self, value):
        result = Solution().isUgly(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, general_prime_factor_reference(value))

    def test_every_small_signed_value_against_general_prime_discovery(self):
        for value in range(-1000, 10001):
            self.check(value)

    def test_large_prime_powers_mixed_factors_and_signed_endpoints(self):
        for value in (1, 2**30, 3**19, 5**13, 2**10 * 3**10 * 5**2,
                      7 * 3**17, 11 * 2**27, -2**31, -2**31 + 1, 2**31 - 1):
            self.check(value)


if __name__ == '__main__':
    unittest.main()
