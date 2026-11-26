from itertools import product
import unittest

from python.p0507_perfect_number import Solution


def every_proper_divisor_oracle(number):
    return sum(divisor for divisor in range(1, number) if number % divisor == 0) == number


class ProperDivisorPairTests(unittest.TestCase):
    def check(self, number, expected=None):
        actual = Solution().checkPerfectNumber(number)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, every_proper_divisor_oracle(number) if expected is None else expected)

    def test_every_small_positive_integer_against_all_proper_divisors(self):
        for number in range(1, 3001):
            self.check(number)

    def test_large_perfect_numbers_maximum_prime_power_and_square_boundaries(self):
        for number in (6, 28, 496, 8128, 33550336):
            self.check(number, True)
        maximum = 100000000
        proper_sum = sum(2**a * 5**b for a, b in product(range(9), repeat=2) if (a, b) != (8, 8))
        self.assertNotEqual(proper_sum, maximum)
        self.check(maximum, False)
        self.check(1 << 26, False)
        for number in (1, 2, 4, 9, 16, 25, 36, 49, 81, 121):
            self.check(number)


if __name__ == '__main__':
    unittest.main()
