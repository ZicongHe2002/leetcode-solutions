from itertools import product
import unittest

from python.p0006_zigzag_conversion import Solution


def periodic_row_oracle(value, row_count):
    if row_count == 1:
        return value
    period = 2 * row_count - 2
    buckets = [[] for _ in range(row_count)]
    for index, character in enumerate(value):
        phase = index % period
        row = min(phase, period - phase)
        buckets[row].append(character)
    return ''.join(''.join(bucket) for bucket in buckets)


class ZigzagPeriodicCoordinateTests(unittest.TestCase):
    def check(self, value, rows, expected=None):
        if expected is None:
            expected = periodic_row_oracle(value, rows)
        result = Solution().convert(value, rows)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(len(result), len(value))

    def test_all_small_strings_and_row_counts_against_periodic_coordinates(self):
        strings = checks = 0
        for length in range(1, 7):
            for characters in product('aB,.', repeat=length):
                value = ''.join(characters)
                strings += 1
                for rows in range(1, 8):
                    self.check(value, rows)
                    checks += 1
        self.assertEqual((strings, checks), (5460, 38220))

    def test_maximum_length_rows_punctuation_and_fixed_layouts(self):
        for rows in (1, 2, 3, 999, 1000):
            self.check('aB,.' * 250, rows)
        self.check('a', 1000, 'a')
        self.check('PAYPALISHIRING', 3, 'PAHNAPLSIIGYIR')
        self.check('PAYPALISHIRING', 4, 'PINALSIGYAHRPI')


if __name__ == '__main__':
    unittest.main()
