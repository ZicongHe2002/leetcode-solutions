import unittest
from itertools import product

from python.p1277_count_square_submatrices_with_all_ones import Solution


def enumerate_all_squares(matrix):
    rows, columns = len(matrix), len(matrix[0])
    return sum(all(matrix[row + dr][column + dc] == 1 for dr in range(side) for dc in range(side))
               for side in range(1, min(rows, columns) + 1)
               for row in range(rows - side + 1) for column in range(columns - side + 1))


class SquareSubmatrixTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = enumerate_all_squares(matrix)
        result = Solution().countSquares(matrix)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_binary_rectangles_against_direct_square_checks(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product((0, 1), repeat=rows * columns):
                    self.check([list(values[row * columns:(row + 1) * columns]) for row in range(rows)])
                    checks += 1
        self.assertEqual(checks, 682)

    def test_maximum_dimensions_full_empty_checkerboard_single_row_and_column(self):
        self.check([[1] * 300 for _ in range(300)], 9045050)
        self.check([[0] * 300 for _ in range(300)], 0)
        self.check([[(row + column) % 2 for column in range(300)] for row in range(300)], 45000)
        self.check([[1] * 300], 300)
        self.check([[1] for _ in range(300)], 300)
        self.check([[1, 0, 1], [1, 1, 0], [1, 1, 0]])


if __name__ == '__main__':
    unittest.main()
