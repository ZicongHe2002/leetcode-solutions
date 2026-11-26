import unittest

from python.p0415_add_strings import Solution


class DecimalStringCarryTests(unittest.TestCase):
    def check(self, first, second, expected):
        actual = Solution().addStrings(first, second)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, expected)
        self.assertTrue(actual.isascii() and actual.isdecimal())
        self.assertTrue(actual == '0' or actual[0] != '0')

    def test_every_small_integer_pair_against_integer_addition(self):
        checks = 0
        for first in range(201):
            for second in range(201):
                self.check(str(first), str(second), str(first + second))
                checks += 1
        self.assertEqual(checks, 40401)

    def test_zero_unequal_lengths_and_maximum_digit_carries(self):
        self.check('0', '0', '0')
        self.check('0', '12345', '12345')
        self.check('1', '999', '1000')
        self.check('999', '1', '1000')
        self.check('9' * 10000, '1', '1' + '0' * 10000)
        self.check('9' * 10000, '9' * 10000, '1' + '9' * 9999 + '8')
        self.check('1' + '0' * 9999, '0', '1' + '0' * 9999)


if __name__ == '__main__':
    unittest.main()
