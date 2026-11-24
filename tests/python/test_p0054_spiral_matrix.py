import unittest
from itertools import product

from python.p0054_spiral_matrix import Solution


def walking_oracle(matrix):
    rows, columns = len(matrix), len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    row = column = direction = 0
    result = []
    for _ in range(rows * columns):
        result.append(matrix[row][column])
        visited.add((row, column))
        dr, dc = directions[direction]
        nr, nc = row + dr, column + dc
        if not (0 <= nr < rows and 0 <= nc < columns) or (nr, nc) in visited:
            direction = (direction + 1) % 4
            dr, dc = directions[direction]
            nr, nc = row + dr, column + dc
        row, column = nr, nc
    return result


class SpiralTests(unittest.TestCase):
    def check(self, matrix, expected):
        before, rows = [row[:] for row in matrix], matrix[:]
        self.assertEqual(Solution().spiralOrder(matrix), expected)
        self.assertEqual(matrix, before)
        for actual, original in zip(matrix, rows):
            self.assertIs(actual, original)

    def test_all_legal_shapes_and_small_binary_values_against_walking(self):
        shapes = checks = 0
        for height in range(1, 11):
            for width in range(1, 11):
                matrix = [[r * width + c - 50 for c in range(width)] for r in range(height)]
                self.check(matrix, walking_oracle(matrix))
                shapes += 1
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
            for values in product(range(2), repeat=height * width):
                matrix = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(matrix, walking_oracle(matrix))
                checks += 1
        self.assertEqual((shapes, checks), (100, 666))

    def test_single_rows_columns_value_bounds_and_empty_extension(self):
        self.check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5])
        self.check([[-100, 0, 100]], [-100, 0, 100])
        self.check([[-100], [0], [100]], [-100, 0, 100])
        self.check([[100]], [100])
        self.check([], [])
        self.check([[]], [])


if __name__ == '__main__':
    unittest.main()
