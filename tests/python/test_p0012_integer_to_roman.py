import unittest

from python.p0012_integer_to_roman import Solution


def roman_by_decimal_places(value):
    thousands = ('', 'M', 'MM', 'MMM')
    hundreds = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')
    tens = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')
    ones = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')
    return thousands[value // 1000] + hundreds[value // 100 % 10] + tens[value // 10 % 10] + ones[value % 10]


class IntegerRomanTests(unittest.TestCase):
    def test_complete_original_domain_against_decimal_place_table(self):
        encodings = set()
        for value in range(1, 4000):
            result = Solution().intToRoman(value)
            self.assertIs(type(result), str)
            self.assertEqual(result, roman_by_decimal_places(value))
            encodings.add(result)
        self.assertEqual(len(encodings), 3999)

    def test_subtractive_boundaries_largest_value_and_longest_output(self):
        for value, expected in ((1, 'I'), (4, 'IV'), (9, 'IX'), (40, 'XL'), (90, 'XC'),
                                (400, 'CD'), (900, 'CM'), (3999, 'MMMCMXCIX'),
                                (3888, 'MMMDCCCLXXXVIII')):
            self.assertEqual(Solution().intToRoman(value), expected)
        self.assertEqual(len(Solution().intToRoman(3888)), 15)


if __name__ == '__main__':
    unittest.main()
