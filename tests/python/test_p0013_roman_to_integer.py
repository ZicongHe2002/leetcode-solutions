import unittest

from python.p0013_roman_to_integer import Solution


def valid_roman_from_places(value):
    places = (
        ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
        ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
        ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
        ('', 'M', 'MM', 'MMM'),
    )
    digits = []
    for table in places:
        value, digit = divmod(value, 10)
        digits.append(table[digit])
    return ''.join(reversed(digits))


class RomanIntegerTests(unittest.TestCase):
    def test_every_valid_original_integer_generated_by_place_tables(self):
        for expected in range(1, 4000):
            result = Solution().romanToInt(valid_roman_from_places(expected))
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)

    def test_subtractive_pairs_maximum_and_fifteen_symbol_additive_form(self):
        for text, expected in (('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90),
                               ('CD', 400), ('CM', 900), ('MMMCMXCIX', 3999),
                               ('MMMDCCCLXXXVIII', 3888), ('I', 1)):
            self.assertEqual(Solution().romanToInt(text), expected)


if __name__ == '__main__':
    unittest.main()
