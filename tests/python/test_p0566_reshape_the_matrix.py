from itertools import product
import unittest

from python.p0566_reshape_the_matrix import Solution


def flatten_and_chunk_reference(matrix, rows, columns):
    flat = [value for row in matrix for value in row]
    if len(flat) != rows * columns:
        return matrix
    return [flat[start:start + columns] for start in range(0, len(flat), columns)]


class RowMajorReshapeTests(unittest.TestCase):
    def check(self, matrix, rows, columns):
        before = [row[:] for row in matrix]
        result = Solution().matrixReshape(matrix, rows, columns)
        self.assertIs(type(result), list)
        self.assertEqual(result, flatten_and_chunk_reference(matrix, rows, columns))
        self.assertEqual(matrix, before)
        if len(matrix) * len(matrix[0]) != rows * columns:
            self.assertIs(result, matrix)
        else:
            self.assertEqual((len(result), len(result[0])), (rows, columns))
            self.assertTrue(all(type(row) is list for row in result))
            self.assertEqual(len({id(row) for row in result}), rows)
            self.assertFalse({id(row) for row in matrix} & {id(row) for row in result})

    def test_small_binary_matrices_and_all_small_requested_shapes(self):
        checks = 0
        for old_rows in range(1, 4):
            for old_columns in range(1, 4):
                for flat in product((0, 1), repeat=old_rows * old_columns):
                    matrix = [list(flat[start:start + old_columns])
                              for start in range(0, len(flat), old_columns)]
                    for rows in range(1, 5):
                        for columns in range(1, 5):
                            self.check(matrix, rows, columns)
                            checks += 1
        self.assertEqual(checks, 10912)

    def test_maximum_source_and_target_dimensions_with_row_order(self):
        for old_rows, old_columns, rows, columns in ((100, 100, 250, 40), (100, 99, 300, 33),
                                                    (99, 100, 33, 300), (100, 100, 100, 100)):
            matrix = [[(row * old_columns + column) % 2001 - 1000
                       for column in range(old_columns)] for row in range(old_rows)]
            self.check(matrix, rows, columns)
        self.check([[-1000, 1000, 7], [3, 4, 5]], 3, 2)
        self.check([[1]], 300, 300)


if __name__ == '__main__':
    unittest.main()
