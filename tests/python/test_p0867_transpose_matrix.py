from itertools import product
import unittest

from python.p0867_transpose_matrix import Solution


def column_zip_reference(matrix):
    return [list(column) for column in zip(*matrix)]


class MatrixTransposeOwnershipTests(unittest.TestCase):
    def check(self, matrix):
        before = [row[:] for row in matrix]
        result = Solution().transpose(matrix)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        self.assertEqual(result, column_zip_reference(matrix))
        self.assertEqual(matrix, before)
        self.assertEqual(len({id(row) for row in result}), len(result))
        self.assertFalse({id(row) for row in matrix} & {id(row) for row in result})

    def test_small_binary_rectangles_and_unique_coordinate_shapes(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for flat in product((0, 1), repeat=rows * columns):
                    self.check([list(flat[start:start + columns])
                                for start in range(0, len(flat), columns)])
                    checks += 1
        self.assertEqual(checks, 682)
        for rows in range(1, 8):
            for columns in range(1, 8):
                self.check([[row * columns + column for column in range(columns)] for row in range(rows)])

    def test_maximum_cell_counts_rectangles_and_value_endpoints(self):
        for rows, columns in ((100, 1000), (1000, 100), (250, 400), (400, 250), (1, 1000), (1000, 1)):
            self.check([[((row * columns + column) * 104729) % 2000000001 - 1000000000
                         for column in range(columns)] for row in range(rows)])
        self.check([[-10**9, 10**9]])


if __name__ == '__main__':
    unittest.main()
