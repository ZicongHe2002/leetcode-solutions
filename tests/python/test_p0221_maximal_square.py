import unittest
from itertools import product

from python.p0221_maximal_square import Solution


def all_squares_oracle(matrix):
    rows, columns = len(matrix), len(matrix[0])
    largest = 0
    for side in range(1, min(rows, columns) + 1):
        for row in range(rows - side + 1):
            for column in range(columns - side + 1):
                if all(matrix[r][c] == '1' for r in range(row, row + side)
                       for c in range(column, column + side)):
                    largest = side * side
    return largest


class MaximalSquareTests(unittest.TestCase):
    def check(self, matrix, expected):
        before, rows = [row[:] for row in matrix], matrix[:]
        self.assertEqual(Solution().maximalSquare(matrix), expected)
        self.assertEqual(matrix, before)
        for actual, original in zip(matrix, rows):
            self.assertIs(actual, original)

    def test_all_small_binary_matrices_against_complete_square_enumeration(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]:
            for values in product('01', repeat=height * width):
                matrix = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(matrix, all_squares_oracle(matrix))
                checks += 1
        self.assertEqual(checks, 66202)

    def test_examples_maximum_matrix_and_empty_extensions(self):
        self.check([list('10100'), list('10111'), list('11111'), list('10010')], 4)
        self.check([['1'] * 300 for _ in range(300)], 90000)
        self.check([['0'] * 300 for _ in range(300)], 0)
        self.check([[str((r + c) % 2) for c in range(300)] for r in range(300)], 1)
        self.check([['1'] * 300], 1)
        self.check([list('10'), list('11')], 1)
        self.check([], 0)
        self.check([[]], 0)


if __name__ == '__main__':
    unittest.main()
