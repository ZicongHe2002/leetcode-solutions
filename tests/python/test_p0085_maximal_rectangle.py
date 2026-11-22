import unittest
from itertools import product

from python.p0085_maximal_rectangle import Solution


def all_binary_rectangles(matrix):
    rows, columns = len(matrix), len(matrix[0])
    best = 0
    for top in range(rows):
        for bottom in range(top + 1, rows + 1):
            for left in range(columns):
                for right in range(left + 1, columns + 1):
                    if all(matrix[i][j] == '1' for i in range(top, bottom) for j in range(left, right)):
                        best = max(best, (bottom - top) * (right - left))
    return best


class MatrixRectangleTests(unittest.TestCase):
    def check(self, matrix, expected=None):
        before = [row[:] for row in matrix]
        if expected is None:
            expected = all_binary_rectangles(matrix)
        result = Solution().maximalRectangle(matrix)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_binary_matrices_against_all_boundary_choices(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product('01', repeat=rows * columns):
                    matrix = [list(values[i * columns:(i + 1) * columns]) for i in range(rows)]
                    self.check(matrix)
                    checks += 1
        self.assertEqual(checks, 682)

    def test_maximum_dimensions_stripes_checkerboard_and_empty_extensions(self):
        self.check([['1'] * 200 for _ in range(200)], 40000)
        self.check([['0'] * 200 for _ in range(200)], 0)
        self.check([['1' if i % 2 else '0'] * 200 for i in range(200)], 200)
        self.check([list('10' * 100) for _ in range(200)], 200)
        self.check([['1' if (i + j) % 2 else '0' for j in range(200)] for i in range(200)], 1)
        self.check([list(row) for row in ['10100', '10111', '11111', '10010']], 6)
        self.check([], 0)
        self.check([[]], 0)


if __name__ == '__main__':
    unittest.main()
