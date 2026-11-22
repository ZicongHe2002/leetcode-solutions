import unittest
from itertools import product

from python.p0073_set_matrix_zeroes import Solution


def original_zero_sets_oracle(matrix):
    zero_rows = {r for r, row in enumerate(matrix) for value in row if value == 0}
    zero_columns = {c for row in matrix for c, value in enumerate(row) if value == 0}
    return [[0 if r in zero_rows or c in zero_columns else value for c, value in enumerate(row)]
            for r, row in enumerate(matrix)]


class MatrixZeroTests(unittest.TestCase):
    def check(self, matrix):
        expected, rows = original_zero_sets_oracle(matrix), matrix[:]
        self.assertIsNone(Solution().setZeroes(matrix))
        self.assertEqual(matrix, expected)
        for actual, original in zip(matrix, rows):
            self.assertIs(actual, original)

    def test_all_small_matrices_against_original_zero_row_column_sets(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
            alphabet = range(2) if (height, width) == (3, 3) else range(-1, 2)
            for values in product(alphabet, repeat=height * width):
                self.check([list(values[r * width:(r + 1) * width]) for r in range(height)])
                checks += 1
        self.assertEqual(checks, 2081)

    def test_first_row_column_numeric_bounds_and_maximum_matrix(self):
        for matrix in [[[1, 0, 3], [4, 5, 6]], [[0, 1], [2, 3]],
                       [[-2**31, 0], [2**31 - 1, -1]], [[0]], [[1], [0], [2]], [], [[]]]:
            self.check(matrix)
        matrix = [[2**31 - 1] * 200 for _ in range(200)]
        matrix[100][150] = 0
        self.check(matrix)


if __name__ == '__main__':
    unittest.main()
