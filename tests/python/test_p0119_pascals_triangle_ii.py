import unittest
from math import comb

from python.p0119_pascals_triangle_ii import Solution


class PascalRowTests(unittest.TestCase):
    def check(self, level):
        result = Solution().getRow(level)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(value) is int for value in result))
        self.assertEqual(result, [comb(level, column) for column in range(level + 1)])
        return result

    def test_every_nonmaximum_original_row_index_against_binomial_coefficients(self):
        for level in range(33):
            self.check(level)

    def test_maximum_row_index_symmetry_sum_and_central_value(self):
        result = self.check(33)
        self.assertEqual(result, result[::-1])
        self.assertEqual(sum(result), 2**33)
        self.assertEqual((result[0], result[-1]), (1, 1))
        self.assertEqual(result[16], 1166803110)


if __name__ == '__main__':
    unittest.main()
