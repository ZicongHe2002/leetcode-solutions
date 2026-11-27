import random
import unittest
from itertools import product

from python.p0723_candy_crush import Solution


def snapshot_maximal_runs(board):
    board = [row[:] for row in board]
    rows, columns = len(board), len(board[0])
    while True:
        removed = set()
        lines = [[(row, column) for column in range(columns)] for row in range(rows)]
        lines += [[(row, column) for row in range(rows)] for column in range(columns)]
        for line in lines:
            start = 0
            while start < len(line):
                row, column = line[start]
                value = board[row][column]
                end = start + 1
                while end < len(line) and board[line[end][0]][line[end][1]] == value:
                    end += 1
                if value and end - start >= 3:
                    removed.update(line[start:end])
                start = end
        if not removed:
            return board
        next_board = [[0] * columns for _ in range(rows)]
        for column in range(columns):
            remaining = [board[row][column] for row in range(rows)
                         if board[row][column] and (row, column) not in removed]
            for row, value in enumerate(remaining, rows - len(remaining)):
                next_board[row][column] = value
        board = next_board


class CandyCrushTests(unittest.TestCase):
    def check(self, board, expected=None):
        if expected is None:
            expected = snapshot_maximal_runs(board)
        result = Solution().candyCrush(board)
        self.assertIs(result, board)
        self.assertEqual(result, expected)
        self.assertTrue(all(type(value) is int and 0 <= value <= 2000 for row in result for value in row))
        self.assertEqual(Solution().candyCrush([row[:] for row in result]), result)

    def test_every_three_by_three_three_color_board_and_seeded_boards_against_snapshot_runs(self):
        checked = 0
        for values in product((1, 2, 3), repeat=9):
            self.check([list(values[start:start + 3]) for start in (0, 3, 6)])
            checked += 1
        self.assertEqual(checked, 19683)
        rng = random.Random(723)
        for _ in range(200):
            rows, columns = rng.randrange(3, 9), rng.randrange(3, 9)
            self.check([[rng.randrange(1, 5) for _ in range(columns)] for _ in range(rows)])

    def test_cascades_simultaneous_cross_and_fifty_square_boundaries(self):
        self.check([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],
                    [410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],
                    [710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]],
                   [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],
                    [210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],
                    [610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]])
        self.check([[2,1,2],[1,1,1],[2,1,2]], [[0,0,0],[2,0,2],[2,0,2]])
        self.check([[2000] * 50 for _ in range(50)], [[0] * 50 for _ in range(50)])
        stable = [[(row + 2 * column) % 7 + 1 for column in range(50)] for row in range(50)]
        self.check([row[:] for row in stable], stable)


if __name__ == '__main__':
    unittest.main()
