import unittest
from itertools import product

from python.p0048_rotate_image import Solution


def coordinate_oracle(matrix):
    size = len(matrix)
    result = [[None] * size for _ in range(size)]
    for row in range(size):
        for column in range(size):
            result[column][size - 1 - row] = matrix[row][column]
    return result


class RotateImageTests(unittest.TestCase):
    def check(self, matrix):
        expected, rows = coordinate_oracle(matrix), matrix[:]
        self.assertIsNone(Solution().rotate(matrix))
        self.assertEqual(matrix, expected)
        for actual, original in zip(matrix, rows):
            self.assertIs(actual, original)

    def test_all_small_binary_squares_and_all_legal_sizes_against_coordinate_map(self):
        checks = 0
        for size in range(1, 4):
            for values in product(range(2), repeat=size * size):
                self.check([list(values[r * size:(r + 1) * size]) for r in range(size)])
                checks += 1
        self.assertEqual(checks, 530)
        for size in range(1, 21):
            self.check([[r * size + c - 200 for c in range(size)] for r in range(size)])

    def test_in_place_value_bounds_four_rotations_and_empty_extension(self):
        self.check([[1000, -1000], [-1000, 1000]])
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        before, rows = [row[:] for row in matrix], matrix[:]
        for _ in range(4):
            self.check(matrix)
        self.assertEqual(matrix, before)
        for actual, original in zip(matrix, rows):
            self.assertIs(actual, original)
        self.check([])


if __name__ == '__main__':
    unittest.main()
