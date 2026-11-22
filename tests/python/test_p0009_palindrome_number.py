import unittest

from python.p0009_palindrome_number import Solution


class PalindromeIntegerTests(unittest.TestCase):
    def check(self, value):
        text = str(value)
        expected = value >= 0 and text == text[::-1]
        result = Solution().isPalindrome(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_every_small_signed_integer_against_string_reversal(self):
        for value in range(-10000, 10001):
            self.check(value)

    def test_32_bit_endpoints_large_palindromes_zero_and_trailing_zeroes(self):
        for value in (-2**31, 2**31 - 1, 2147447412, 2000000002, 1000000001, 0, 11, 121, 12321, 12331):
            self.check(value)
        for exponent in range(10):
            self.check(10**exponent)


if __name__ == '__main__':
    unittest.main()
