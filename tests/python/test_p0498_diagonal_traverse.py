from itertools import product
import unittest

from python.p0498_diagonal_traverse import Solution


def coordinate_sort_reference(matrix):
    coordinates = [(row, column) for row in range(len(matrix))
                   for column in range(len(matrix[0]))]
    coordinates.sort(key=lambda point: (sum(point), -point[0] if sum(point) % 2 == 0 else point[0]))
    return [matrix[row][column] for row, column in coordinates]


class AlternatingDiagonalTraversalTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = coordinate_sort_reference(matrix)
        result = Solution().findDiagonalOrder(matrix)
        self.assertIs(type(result), list)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_small_rectangles_binary_assignments_and_unique_coordinates(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for flat in product((0, 1), repeat=rows * columns):
                    self.check([list(flat[start:start + columns])
                                for start in range(0, len(flat), columns)])
                    checks += 1
        self.assertEqual(checks, 682)
        for rows in range(1, 7):
            for columns in range(1, 7):
                self.check([[row * columns + column for column in range(columns)] for row in range(rows)])

    def test_maximum_cell_counts_degenerate_axes_and_value_endpoints(self):
        for rows, columns in ((1, 10000), (10000, 1), (100, 100), (2, 5000), (5000, 2)):
            self.check([[row * columns + column for column in range(columns)] for row in range(rows)])
        self.check([[-100000, 100000]])
        self.check([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9])


if __name__ == '__main__':
    unittest.main()
