import re
import unittest

from python.p0168_excel_sheet_column_title import Solution


def column_place_value(title):
    return sum((ord(letter) - ord('A') + 1) * 26**place
               for place, letter in enumerate(reversed(title)))


class ExcelColumnTitlePlaceValueTests(unittest.TestCase):
    def check(self, number, expected=None):
        result = Solution().convertToTitle(number)
        self.assertIs(type(result), str)
        self.assertIsNotNone(re.fullmatch('[A-Z]+', result))
        self.assertLessEqual(len(result), 7)
        self.assertEqual(column_place_value(result), number)
        if expected is not None:
            self.assertEqual(result, expected)

    def test_first_20000_columns_against_independent_place_value_sum(self):
        for number in range(1, 20001):
            self.check(number)

    def test_carry_boundaries_and_largest_column_number(self):
        for number, expected in ((1, 'A'), (26, 'Z'), (27, 'AA'), (52, 'AZ'),
                                 (53, 'BA'), (702, 'ZZ'), (703, 'AAA'),
                                 (2**31 - 1, 'FXSHRXW')):
            self.check(number, expected)


if __name__ == '__main__':
    unittest.main()
