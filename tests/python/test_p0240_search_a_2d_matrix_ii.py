import unittest
from itertools import combinations_with_replacement, product

from python.p0240_search_a_2d_matrix_ii import Solution


def small_sorted_matrices():
    for height in range(1, 4):
        for width in range(1, 4):
            rows = list(combinations_with_replacement((-1, 0, 1), width))
            for matrix in product(rows, repeat=height):
                if all(matrix[row][column] <= matrix[row + 1][column]
                       for row in range(height - 1) for column in range(width)):
                    yield [list(row) for row in matrix]


class StaircaseSearchTests(unittest.TestCase):
    def check(self, matrix, target):
        before = [row[:] for row in matrix]
        expected = any(value == target for row in matrix for value in row)
        result = Solution().searchMatrix(matrix, target)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)

    def test_all_small_ordered_rectangles_against_full_scan(self):
        arrays = checks = 0
        for matrix in small_sorted_matrices():
            arrays += 1
            for target in range(-2, 3):
                self.check(matrix, target)
                checks += 1
        self.assertEqual((arrays, checks), (330, 1650))

    def test_maximum_dimensions_overlap_and_value_extremes(self):
        matrix = [[row * 600 + column * 2 for column in range(300)]
                  for row in range(300)]
        for target in (0, 179998, 90000, 1, -10**9, 10**9):
            self.check(matrix, target)
        self.check([[-10**9] * 300 for _ in range(300)], -10**9)
        self.check([[10**9] * 300 for _ in range(300)], 0)
        self.check([[1, 4], [2, 5]], 2)
        self.check([[-10**9, 0, 10**9]], 0)
        self.check([[-10**9], [0], [10**9]], 1)


if __name__ == '__main__':
    unittest.main()
