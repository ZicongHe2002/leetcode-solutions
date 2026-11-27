from itertools import groupby, product
import unittest

from python.p0443_string_compression import Solution


def grouped_reference(value):
    result = []
    for character, group in groupby(value):
        count = len(list(group))
        result.append(character + (str(count) if count > 1 else ''))
    return ''.join(result)


class InPlaceCompressionTests(unittest.TestCase):
    def check(self, value):
        expected = grouped_reference(value)
        chars = list(value)
        size = Solution().compress(chars)
        self.assertIs(type(size), int)
        self.assertEqual(size, len(expected))
        self.assertEqual(''.join(chars[:size]), expected)
        self.assertEqual(len(chars), len(value))
        self.assertLessEqual(size, len(value))

    def test_all_small_character_arrays_against_grouped_text(self):
        checks = 0
        for size in range(1, 8):
            for value in product('aA1!', repeat=size):
                self.check(''.join(value))
                checks += 1
        self.assertEqual(checks, 21844)

    def test_decimal_transitions_maximum_length_and_literal_digits(self):
        for count in (9, 10, 99, 100, 999, 1000, 2000):
            self.check('1' * count)
        self.check('a1' * 1000)
        self.check('a' * 1000 + '1' * 999 + '!')
        self.check('ab' + '!' * 12)


if __name__ == '__main__':
    unittest.main()
