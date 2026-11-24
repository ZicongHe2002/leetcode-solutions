import unittest
from itertools import product

from python.p0542_zero_one_matrix import Solution


def manhattan_oracle(mat):
    zeros = [(r, c) for r, row in enumerate(mat) for c, value in enumerate(row) if value == 0]
    return [[min(abs(r - zr) + abs(c - zc) for zr, zc in zeros)
             for c in range(len(row))] for r, row in enumerate(mat)]


class MatrixDistanceTests(unittest.TestCase):
    def check(self, mat, expected):
        before, rows = [row[:] for row in mat], mat[:]
        result = Solution().updateMatrix(mat)
        self.assertEqual(result, expected)
        self.assertEqual(mat, before)
        self.assertIsNot(result, mat)
        self.assertEqual(len({id(row) for row in result}), len(result))
        self.assertFalse({id(row) for row in mat} & {id(row) for row in result})
        for actual, original in zip(mat, rows):
            self.assertIs(actual, original)

    def test_all_small_valid_matrices_against_manhattan_oracle(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]:
            for values in product(range(2), repeat=height * width):
                if 0 not in values:
                    continue
                mat = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(mat, manhattan_oracle(mat))
                checks += 1
        self.assertEqual(checks, 66195)

    def test_examples_empty_and_maximum_cell_count(self):
        self.check([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]])
        self.check([[0, 0], [0, 0]], [[0, 0], [0, 0]])
        self.check([], [])
        self.check([[]], [[]])
        self.check([[0] + [1] * 9999], [list(range(10000))])
        self.check([[0]] + [[1] for _ in range(9999)], [[r] for r in range(10000)])
        mat = [[1] * 100 for _ in range(100)]
        mat[0][0] = 0
        self.check(mat, [[r + c for c in range(100)] for r in range(100)])


if __name__ == '__main__':
    unittest.main()
