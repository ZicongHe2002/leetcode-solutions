from itertools import product
import unittest

from python.p0562_longest_line_of_consecutive_one_in_matrix import Solution


def walk_every_ray(mat):
    rows, columns = len(mat), len(mat[0])
    best = 0
    for row in range(rows):
        for column in range(columns):
            for dr, dc in ((0, 1), (1, 0), (1, 1), (1, -1)):
                r, c, length = row, column, 0
                while 0 <= r < rows and 0 <= c < columns and mat[r][c] == 1:
                    length += 1
                    r, c = r + dr, c + dc
                best = max(best, length)
    return best


class MatrixLineTests(unittest.TestCase):
    def check(self, mat, expected):
        before = [row[:] for row in mat]
        result = Solution().longestLine(mat)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(mat, before)

    def test_exhaustive_small_matrices_against_ray_walking(self):
        checks = 0
        shapes = [(m, n) for m in range(1, 4) for n in range(1, 4)] + [(2, 4), (4, 2)]
        for rows, columns in shapes:
            for bits in product((0, 1), repeat=rows * columns):
                mat = [list(bits[r * columns:(r + 1) * columns]) for r in range(rows)]
                self.check(mat, walk_every_ray(mat))
                checks += 1
        self.assertEqual(checks, 1194)

    def test_maximum_cells_both_diagonals_and_zero_breaks(self):
        self.check([[1] * 10000], 10000)
        self.check([[1] for _ in range(10000)], 10000)
        self.check([[1] * 100 for _ in range(100)], 100)
        self.check([[int(r == c) for c in range(100)] for r in range(100)], 100)
        self.check([[int(r + c == 99) for c in range(100)] for r in range(100)], 100)
        self.check([[1] * 4999 + [0] + [1] * 5000], 5000)
        self.check([[0] * 100 for _ in range(100)], 0)
        self.check([], 0)
        self.check([[]], 0)


if __name__ == '__main__':
    unittest.main()
