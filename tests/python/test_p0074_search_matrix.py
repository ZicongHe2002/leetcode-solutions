import unittest
from itertools import combinations_with_replacement

from python.p0074_search_matrix import Solution


def scan(matrix, target):
    return any(value == target for row in matrix for value in row)


class MatrixTests(unittest.TestCase):
    def check(self, matrix, target, expected):
        before = [row[:] for row in matrix]
        rows = matrix[:]
        self.assertIs(Solution().searchMatrix(matrix, target), expected)
        self.assertEqual(matrix, before)
        self.assertTrue(all(row is original for row, original in zip(matrix, rows)))

    def test_all_small_legal_matrices_against_element_scan(self):
        matrices = queries = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in combinations_with_replacement(range(-2, 3), rows * columns):
                    if any(values[row * columns - 1] >= values[row * columns] for row in range(1, rows)):
                        continue
                    matrix = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                    matrices += 1
                    for target in range(-3, 4):
                        self.check(matrix, target, scan(matrix, target))
                        queries += 1
        self.assertEqual((matrices, queries), (277, 1939))

    def test_rectangles_duplicates_empty_extensions_and_largest_shape(self):
        for matrix, target, expected in [([[1, 3, 5], [7, 9, 11]], 9, True),
                                         ([[1, 3, 5], [7, 9, 11]], 6, False),
                                         ([[1, 1, 1], [2, 2, 3]], 2, True), ([[1], [3], [5]], 3, True),
                                         ([[-10000, 0, 10000]], 10000, True), ([], 0, False), ([[]], 0, False)]:
            self.check(matrix, target, expected)
        matrix = [[row * 100 + column - 5000 for column in range(100)] for row in range(100)]
        for target in (-5001, -5000, -4901, -4900, 0, 4999, 5000):
            self.check(matrix, target, scan(matrix, target))
        matrix = [[row - 50] * 100 for row in range(100)]
        for target in range(-51, 51):
            self.check(matrix, target, scan(matrix, target))


if __name__ == '__main__':
    unittest.main()
