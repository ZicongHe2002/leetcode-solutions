from itertools import product
import unittest

from python.p0171_excel_sheet_column_number import Solution


def direct_column_weights(title):
    return sum((ord(letter) - 64) * 26**(len(title) - index - 1)
               for index, letter in enumerate(title))


class ExcelColumnNumberWeightsTests(unittest.TestCase):
    def check(self, title, expected=None):
        if expected is None:
            expected = direct_column_weights(title)
        result = Solution().titleToNumber(title)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 2**31 - 1)

    def test_every_column_title_with_up_to_three_letters(self):
        checked = 0
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for length in range(1, 4):
            for letters in product(alphabet, repeat=length):
                self.check(''.join(letters))
                checked += 1
        self.assertEqual(checked, 18278)

    def test_bijective_digit_boundaries_and_maximum_legal_title(self):
        for title, expected in (('A', 1), ('Z', 26), ('AA', 27), ('ZZ', 702),
                                 ('AAA', 703), ('FXSHRXW', 2**31 - 1)):
            self.check(title, expected)
        self.check('AAAAAAA')


if __name__ == '__main__':
    unittest.main()
