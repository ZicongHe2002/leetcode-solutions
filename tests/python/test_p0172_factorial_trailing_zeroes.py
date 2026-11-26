import unittest
from math import factorial

from python.p0172_factorial_trailing_zeroes import Solution


def trailing_zeroes_of_actual_factorial(value):
    result = factorial(value)
    zeroes = 0
    while result % 10 == 0:
        zeroes += 1
        result //= 10
    return zeroes


class FactorialZeroTests(unittest.TestCase):
    def check(self, value, expected=None):
        if expected is None:
            expected = trailing_zeroes_of_actual_factorial(value)
        result = Solution().trailingZeroes(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_input_against_actual_factorial_last_digits(self):
        for value in range(301):
            self.check(value)

    def test_powers_of_five_repeated_factors_and_maximum_input(self):
        for value, expected in ((0, 0), (4, 0), (5, 1), (25, 6), (125, 31),
                                (625, 156), (3125, 781), (9999, 2495), (10000, 2499)):
            self.check(value, expected)


if __name__ == '__main__':
    unittest.main()
