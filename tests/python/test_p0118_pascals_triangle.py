import unittest
from math import comb

from python.p0118_pascals_triangle import Solution


class PascalTriangleTests(unittest.TestCase):
    def check(self, count):
        result = Solution().generate(count)
        expected = [[comb(level, column) for column in range(level + 1)] for level in range(count)]
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        self.assertTrue(all(type(value) is int for row in result for value in row))
        self.assertEqual(result, expected)
        return result

    def test_each_nonmaximum_original_row_count_against_binomial_coefficients(self):
        for count in range(1, 30):
            self.check(count)

    def test_maximum_row_count_and_combinatorial_identities(self):
        result = self.check(30)
        for level, row in enumerate(result):
            self.assertEqual(row, row[::-1])
            self.assertEqual(sum(row), 2**level)
            self.assertEqual((row[0], row[-1]), (1, 1))
        self.assertEqual(result[-1][14], 77558760)


if __name__ == '__main__':
    unittest.main()
