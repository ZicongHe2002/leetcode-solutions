import unittest
from itertools import product

from python.p0036_valid_sudoku import Solution


def pairwise_oracle(board):
    filled = [(r, c, value) for r, row in enumerate(board) for c, value in enumerate(row) if value != '.']
    for index, (r, c, value) in enumerate(filled):
        for rr, cc, other in filled[:index]:
            if value == other and (r == rr or c == cc or (r // 3 == rr // 3 and c // 3 == cc // 3)):
                return False
    return True


class SudokuTests(unittest.TestCase):
    def check(self, board, expected):
        before, rows = [row[:] for row in board], board[:]
        self.assertIs(Solution().isValidSudoku(board), expected)
        self.assertEqual(board, before)
        for actual, original in zip(board, rows):
            self.assertIs(actual, original)

    def test_all_selected_cell_assignments_against_pairwise_relations(self):
        coordinates = [(0, 0), (0, 4), (1, 1), (1, 4), (4, 0), (4, 4)]
        checks = 0
        for values in product('.12', repeat=len(coordinates)):
            board = [['.'] * 9 for _ in range(9)]
            for (row, column), value in zip(coordinates, values):
                board[row][column] = value
            self.check(board, pairwise_oracle(board))
            checks += 1
        self.assertEqual(checks, 729)

    def test_complete_board_all_single_changes_and_partial_validation_scope(self):
        board = [[str((3 * r + r // 3 + c) % 9 + 1) for c in range(9)] for r in range(9)]
        self.assertTrue(pairwise_oracle(board))
        self.check(board, True)
        changes = 0
        for row in range(9):
            for column in range(9):
                for value in '123456789':
                    if value == board[row][column]:
                        continue
                    changed = [line[:] for line in board]
                    changed[row][column] = value
                    self.check(changed, False)
                    changes += 1
        self.assertEqual(changes, 648)
        partial = [['.'] * 9 for _ in range(9)]
        partial[0] = list('12345678.')
        partial[1][8] = '9'
        self.assertTrue(pairwise_oracle(partial))
        self.check(partial, True)
        self.check([['.'] * 9 for _ in range(9)], True)


if __name__ == '__main__':
    unittest.main()
