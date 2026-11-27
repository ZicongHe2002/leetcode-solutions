import unittest

from python.p0504_base_7 import Solution


class BaseSevenStandardParserTests(unittest.TestCase):
    def check(self, number, expected=None):
        result = Solution().convertToBase7(number)
        self.assertIs(type(result), str)
        self.assertEqual(result.startswith('-'), number < 0)
        unsigned = result[1:] if result.startswith('-') else result
        self.assertTrue(unsigned and all(character in '0123456' for character in unsigned))
        self.assertTrue(unsigned == '0' or not unsigned.startswith('0'))
        self.assertLessEqual(len(unsigned), 9)
        self.assertEqual(int(result, 7), number)
        if number == 0:
            self.assertEqual(result, '0')
        if expected is not None:
            self.assertEqual(result, expected)

    def test_all_small_signed_values_against_standard_base7_parser(self):
        for number in range(-10000, 10001):
            self.check(number)

    def test_value_limits_power_carries_and_fixed_examples(self):
        self.check(-10**7)
        self.check(10**7)
        for exponent in range(9):
            for number in (7**exponent - 1, 7**exponent, 7**exponent + 1):
                self.check(number)
                self.check(-number)
        self.check(100, '202')
        self.check(-7, '-10')
        self.check(0, '0')


if __name__ == '__main__':
    unittest.main()
