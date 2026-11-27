from itertools import product
import unittest

from python.p0304_range_sum_query_2d_immutable import NumMatrix


class ImmutableRectanglePrefixTests(unittest.TestCase):
    def test_all_small_three_value_matrices_and_every_rectangle(self):
        matrices = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for flat in product((-1, 0, 1), repeat=rows * columns):
                    source = [list(flat[start:start + columns])
                              for start in range(0, len(flat), columns)]
                    before = [row[:] for row in source]
                    instance = NumMatrix(source)
                    for row1 in range(rows):
                        for row2 in range(row1, rows):
                            for col1 in range(columns):
                                for col2 in range(col1, columns):
                                    expected = sum(before[row][column]
                                                   for row in range(row1, row2 + 1)
                                                   for column in range(col1, col2 + 1))
                                    result = instance.sumRegion(row1, col1, row2, col2)
                                    self.assertIs(type(result), int)
                                    self.assertEqual(result, expected)
                    self.assertEqual(source, before)
                    matrices += 1
        self.assertEqual(matrices, 21297)

    def test_maximum_matrix_and_query_count_negative_and_positive_sums(self):
        size = 200
        source = [[-10000 if (row + column) % 2 == 0 else 10000
                   for column in range(size)] for row in range(size)]
        before = [row[:] for row in source]
        instance = NumMatrix(source)
        for query in range(10000):
            if query == 0:
                row1 = col1 = 0
                row2 = col2 = size - 1
            elif query == 1:
                row1 = row2 = col1 = col2 = size - 1
            else:
                row1 = query * 13 % size
                row2 = row1 + query * 17 % (size - row1)
                col1 = query * 19 % size
                col2 = col1 + query * 23 % (size - col1)
            expected = (before[row1][col1] if (row2 - row1 + 1) % 2
                        and (col2 - col1 + 1) % 2 else 0)
            result = instance.sumRegion(row1, col1, row2, col2)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
        self.assertEqual(source, before)
        for value in (-10000, 10000):
            constant = NumMatrix([[value] * size for _ in range(size)])
            self.assertEqual(constant.sumRegion(0, 0, size - 1, size - 1), value * size * size)
            self.assertEqual(constant.sumRegion(0, 0, 0, 0), value)


if __name__ == '__main__':
    unittest.main()
