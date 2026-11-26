from itertools import product
import unittest

from python.p0598_range_addition_ii import Solution


def apply_every_cell(rows, columns, operations):
    matrix = [[0] * columns for _ in range(rows)]
    for height, width in operations:
        for row in range(height):
            for column in range(width):
                matrix[row][column] += 1
    maximum = max(map(max, matrix))
    return sum(value == maximum for row in matrix for value in row)


class RangeAdditionTests(unittest.TestCase):
    def check(self, rows, columns, operations, expected):
        before = [operation[:] for operation in operations]
        result = Solution().maxCount(rows, columns, operations)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(operations, before)

    def test_all_small_grids_and_operation_sequences_against_cell_updates(self):
        cases = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                legal = [(height, width) for height in range(1, rows + 1) for width in range(1, columns + 1)]
                for count in range(4):
                    for sequence in product(legal, repeat=count):
                        operations = list(map(list, sequence))
                        self.check(rows, columns, operations, apply_every_cell(rows, columns, operations))
                        cases += 1
        self.assertEqual(cases, 1537)

    def test_maximum_dimensions_empty_and_ten_thousand_operations(self):
        self.check(40000, 40000, [], 1600000000)
        self.check(40000, 40000, [[40000, 40000] for _ in range(10000)], 1600000000)
        self.check(40000, 40000, [[40000, 1]] + [[1, 40000] for _ in range(9999)], 1)
        self.check(3, 3, [[2, 2], [3, 3]], 4)
        self.check(1, 1, [], 1)


if __name__ == '__main__':
    unittest.main()
