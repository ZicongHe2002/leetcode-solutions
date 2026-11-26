import unittest
from itertools import product

from python.p0130_surrounded_regions import Solution


def outside_union_result(board):
    rows, columns = len(board), len(board[0])
    outside = rows * columns
    parent = list(range(outside + 1))

    def root(index):
        while parent[index] != index:
            index = parent[index]
        return index

    def union(first, second):
        parent[root(first)] = root(second)

    for row in range(rows):
        for column in range(columns):
            if board[row][column] != 'O':
                continue
            index = row * columns + column
            if row in (0, rows - 1) or column in (0, columns - 1):
                union(index, outside)
            for nr, nc in ((row + 1, column), (row, column + 1)):
                if nr < rows and nc < columns and board[nr][nc] == 'O':
                    union(index, nr * columns + nc)
    return [['O' if board[row][column] == 'O' and root(row * columns + column) == root(outside) else 'X'
             for column in range(columns)] for row in range(rows)]


class SurroundedRegionTests(unittest.TestCase):
    def check(self, board, expected=None):
        if expected is None:
            expected = outside_union_result(board)
        result = Solution().solve(board)
        self.assertIsNone(result)
        self.assertEqual(board, expected)

    def test_all_small_boards_against_outside_union(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product('XO', repeat=rows * columns):
                    self.check([list(values[i * columns:(i + 1) * columns]) for i in range(rows)])
                    checks += 1
        self.assertEqual(checks, 682)

    def test_maximum_dimensions_regions_corridors_diagonal_and_empty_extensions(self):
        self.check([['O'] * 200 for _ in range(200)], [['O'] * 200 for _ in range(200)])
        self.check([['X'] * 200 for _ in range(200)], [['X'] * 200 for _ in range(200)])
        board = [['O' if 0 < row < 199 and 0 < column < 199 else 'X' for column in range(200)] for row in range(200)]
        self.check(board, [['X'] * 200 for _ in range(200)])
        board = [['O' if column == 100 or (row == 100 and 30 <= column <= 100) else 'X'
                  for column in range(200)] for row in range(200)]
        self.check(board, [row[:] for row in board])
        board = [['O' if row == column else 'X' for column in range(200)] for row in range(200)]
        expected = [['X'] * 200 for _ in range(200)]
        expected[0][0] = expected[199][199] = 'O'
        self.check(board, expected)
        self.check([], [])
        self.check([[]], [[]])


if __name__ == '__main__':
    unittest.main()
