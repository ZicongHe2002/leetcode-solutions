from itertools import product
import unittest

from python.p0329_longest_increasing_path_matrix import Solution


def all_increasing_paths(matrix):
    rows, columns = len(matrix), len(matrix[0])

    def from_cell(row, column):
        return 1 + max((from_cell(nr, nc)
                        for nr, nc in ((row - 1, column), (row + 1, column),
                                       (row, column - 1), (row, column + 1))
                        if 0 <= nr < rows and 0 <= nc < columns
                        and matrix[nr][nc] > matrix[row][column]), default=0)

    return max(from_cell(row, column) for row in range(rows) for column in range(columns))


class IncreasingPathEnumerationTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = all_increasing_paths(matrix)
        result = Solution().longestIncreasingPath(matrix)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_matrices_against_explicit_path_search(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)):
            for values in product((0, 1, 2), repeat=rows * columns):
                matrix = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                self.check(matrix)
                checked += 1
        self.assertEqual(checked, 1560)

    def test_maximum_matrix_hamiltonian_increase_equal_values_and_thin_shape(self):
        matrix = []
        for row in range(200):
            values = list(range(row * 200, (row + 1) * 200))
            matrix.append(values if row % 2 == 0 else list(reversed(values)))
        self.check(matrix, 40000)
        self.check([[2**31 - 1] * 200 for _ in range(200)], 1)
        self.check([list(range(199, -1, -1))], 200)
        self.check([[0]], 1)


if __name__ == '__main__':
    unittest.main()
