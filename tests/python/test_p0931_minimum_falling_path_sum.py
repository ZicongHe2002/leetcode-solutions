import unittest
from itertools import product

from python.p0931_minimum_falling_path_sum import Solution


def minimum_by_all_column_sequences(matrix):
    size = len(matrix)
    best = float('inf')

    def walk(columns):
        nonlocal best
        if len(columns) == size:
            best = min(best, sum(matrix[row][column] for row, column in enumerate(columns)))
            return
        options = range(size) if not columns else range(max(0, columns[-1] - 1), min(size, columns[-1] + 2))
        for column in options:
            walk(columns + (column,))

    walk(())
    return best


class FallingPathTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = minimum_by_all_column_sequences(matrix)
        result = Solution().minFallingPathSum(matrix)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_ternary_square_matrices_against_complete_paths(self):
        checks = 0
        for size in range(1, 4):
            for values in product((-1, 0, 2), repeat=size * size):
                self.check([list(values[row * size:(row + 1) * size]) for row in range(size)])
                checks += 1
        self.assertEqual(checks, 19767)

    def test_maximum_dimensions_negative_positive_diagonal_edge_and_single_cell(self):
        self.check([[-100] * 100 for _ in range(100)], -10000)
        self.check([[100] * 100 for _ in range(100)], 10000)
        self.check([[-100 if row == column else 100 for column in range(100)] for row in range(100)], -10000)
        self.check([[-100] + [100] * 99 for _ in range(100)], -10000)
        self.check([[1, -2], [-3, 4]], -5)
        self.check([[-100]], -100)


if __name__ == '__main__':
    unittest.main()
