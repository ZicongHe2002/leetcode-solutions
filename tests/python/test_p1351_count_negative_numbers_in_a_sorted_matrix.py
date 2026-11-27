import unittest
from itertools import combinations_with_replacement, product

from python.p1351_count_negative_numbers_in_a_sorted_matrix import Solution


def small_descending_matrices():
    for height in range(1, 4):
        for width in range(1, 4):
            rows = [tuple(reversed(row))
                    for row in combinations_with_replacement((-1, 0, 1), width)]
            for matrix in product(rows, repeat=height):
                if all(matrix[row][column] >= matrix[row + 1][column]
                       for row in range(height - 1) for column in range(width)):
                    yield [list(row) for row in matrix]


class NegativeStaircaseTests(unittest.TestCase):
    def check(self, matrix):
        before = [row[:] for row in matrix]
        expected = sum(value < 0 for row in matrix for value in row)
        result = Solution().countNegatives(matrix)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(matrix, before)
        return result

    def test_all_small_descending_rectangles_against_full_scan(self):
        checks = 0
        for matrix in small_descending_matrices():
            self.check(matrix)
            checks += 1
        self.assertEqual(checks, 330)

    def test_maximum_dimensions_zero_exclusion_and_value_limits(self):
        self.assertEqual(self.check([[-100] * 100 for _ in range(100)]), 10000)
        self.assertEqual(self.check([[0] * 100 for _ in range(100)]), 0)
        matrix = [[100 - row - column for column in range(100)]
                  for row in range(100)]
        self.assertEqual(self.check(matrix), 4851)
        self.check([[100, 0, -1, -100]])
        self.check([[100], [0], [-1], [-100]])
        self.check([[100, 0], [0, -100]])


if __name__ == '__main__':
    unittest.main()
