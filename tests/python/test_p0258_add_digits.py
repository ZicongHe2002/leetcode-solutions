import unittest

from python.p0258_add_digits import Solution


def repeated_string_digit_sum(value):
    while value >= 10:
        value = sum(int(character) for character in str(value))
    return value


class DigitalRootTests(unittest.TestCase):
    def check(self, value, expected=None):
        if expected is None:
            expected = repeated_string_digit_sum(value)
        result = Solution().addDigits(value)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_integer_against_repeated_digit_sums(self):
        for value in range(10001):
            self.check(value)

    def test_maximum_integer_zero_nine_multiples_and_powers_of_ten(self):
        self.check(2**31 - 1, 1)
        self.check(2**31 - 2, 9)
        self.check(0, 0)
        for value in (9, 99, 999, 999999999):
            self.check(value, 9)
        for exponent in range(10):
            self.check(10**exponent, 1)


if __name__ == '__main__':
    unittest.main()
