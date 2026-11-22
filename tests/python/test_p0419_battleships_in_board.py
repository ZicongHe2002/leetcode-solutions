from itertools import product
import unittest

from python.p0419_battleships_in_board import Solution


def valid_straight_components(board):
    remaining = {(row, column) for row in range(len(board)) for column in range(len(board[0]))
                 if board[row][column] == 'X'}
    count = 0
    while remaining:
        first = remaining.pop()
        component, pending = {first}, [first]
        while pending:
            row, column = pending.pop()
            for cell in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
                if cell in remaining:
                    remaining.remove(cell)
                    component.add(cell)
                    pending.append(cell)
        if len({row for row, column in component}) != 1 and len({column for row, column in component}) != 1:
            return None
        count += 1
    return count


class BattleshipComponentOracleTests(unittest.TestCase):
    def check(self, board, expected):
        before = [row[:] for row in board]
        result = Solution().countBattleships(board)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(board, before)

    def test_every_small_board_that_satisfies_straight_ship_contract(self):
        checked = skipped = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)):
            for values in product('.X', repeat=rows * columns):
                board = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                expected = valid_straight_components(board)
                if expected is None:
                    skipped += 1
                else:
                    self.check(board, expected)
                    checked += 1
        self.assertEqual((checked, skipped), (286, 380))

    def test_maximum_board_separated_single_cells_and_long_ships(self):
        self.check([['X' if (row + column) % 2 == 0 else '.' for column in range(200)]
                    for row in range(200)], 20000)
        self.check([['X' if row % 2 == 0 else '.'] * 200 for row in range(200)], 100)
        self.check([['.'] * 200 for _ in range(200)], 0)
        self.check([['X'] for _ in range(200)], 1)


if __name__ == '__main__':
    unittest.main()
