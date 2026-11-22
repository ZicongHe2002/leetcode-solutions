import unittest

from python.p0007_reverse_integer import Solution


def wide_integer_text_oracle(number):
    reversed_value = int(str(abs(number))[::-1]) * (-1 if number < 0 else 1)
    return reversed_value if -2**31 <= reversed_value <= 2**31 - 1 else 0


class ReverseIntegerTextOracleTests(unittest.TestCase):
    def check(self, number):
        result = Solution().reverse(number)
        self.assertIs(type(result), int)
        self.assertEqual(result, wide_integer_text_oracle(number))
        self.assertGreaterEqual(result, -2**31)
        self.assertLessEqual(result, 2**31 - 1)

    def test_all_small_signed_integers_against_text_reversal(self):
        for number in range(-10000, 10001):
            self.check(number)

    def test_int32_limits_near_overflow_and_trailing_zeros(self):
        for number in (-2**31, 2**31 - 1, 1534236469, 1463847412, 1563847412,
                       -1463847412, -1563847412, 120, -120, 0, 1000000000):
            self.check(number)


if __name__ == '__main__':
    unittest.main()
