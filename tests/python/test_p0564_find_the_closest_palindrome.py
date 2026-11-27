from bisect import bisect_left
import unittest

from python.p0564_find_the_closest_palindrome import Solution


class ClosestPalindromeTests(unittest.TestCase):
    def check(self, value, expected):
        text = str(value)
        result = Solution().nearestPalindromic(text)
        self.assertIs(type(result), str)
        self.assertEqual(result, str(expected))
        self.assertEqual(result, result[::-1])
        self.assertNotEqual(result, text)
        self.assertEqual(str(int(result)), result)

    def test_first_hundred_thousand_against_enumerated_palindromes(self):
        palindromes = [value for value in range(200001) if str(value) == str(value)[::-1]]
        for value in range(1, 100001):
            index = bisect_left(palindromes, value)
            smaller = palindromes[index - 1]
            larger = palindromes[index + (palindromes[index] == value)]
            expected = min((smaller, larger), key=lambda x: (abs(x - value), x))
            self.check(value, expected)

    def test_decimal_boundaries_ties_and_eighteen_digit_values(self):
        for exponent in range(1, 18):
            power = 10 ** exponent
            self.check(power, power - 1)
            self.check(power + 1, power - 1)
            if exponent > 1:
                self.check(power - 1, power + 1)
        for value, expected in ((1, 0), (9, 8), (121, 111), (123, 121), (1283, 1331),
                                (10**18 - 1, 10**18 + 1),
                                (100000000000000001, 99999999999999999),
                                (123456789987654321, 123456790097654321)):
            self.check(value, expected)


if __name__ == '__main__':
    unittest.main()
