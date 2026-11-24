import unittest

from python.p0037_sudoku_solver import Solution


STANDARD = ('53..7....', '6..195...', '.98....6.', '8...6...3', '4..8.3..1',
            '7...2...6', '.6....28.', '...419..5', '....8..79')
STANDARD_SOLUTION = ('534678912', '672195348', '198342567', '859761423', '426853791',
                     '713924856', '961537284', '287419635', '345286179')
HARD = ('1....7.9.', '.3..2...8', '..96..5..', '..53..9..', '.1..8...2',
        '6....4...', '3......1.', '.4......7', '..7...3..')
HARD_SOLUTION = ('162857493', '534129678', '789643521', '475312986', '913586742',
                 '628794135', '356478219', '241935867', '897261354')


def transform(lines, shift, transpose):
    result = [[str((int(value) - 1 + shift) % 9 + 1) if value != '.' else '.'
               for value in line] for line in lines]
    return [list(column) for column in zip(*result)] if transpose else result


class SudokuSolverTests(unittest.TestCase):
    def check(self, puzzle, expected):
        board = [list(line) for line in puzzle]
        before = [row[:] for row in board]
        row_ids = [id(row) for row in board]
        self.assertIsNone(Solution().solveSudoku(board))
        self.assertEqual(row_ids, [id(row) for row in board])
        self.assertEqual(board, [list(line) for line in expected])
        digits = set('123456789')
        for row in board:
            self.assertEqual(set(row), digits)
        for column in zip(*board):
            self.assertEqual(set(column), digits)
        for top in (0, 3, 6):
            for left in (0, 3, 6):
                self.assertEqual({board[row][column]
                                  for row in range(top, top + 3)
                                  for column in range(left, left + 3)}, digits)
        for row in range(9):
            for column in range(9):
                if before[row][column] != '.':
                    self.assertEqual(board[row][column], before[row][column])

    def test_unique_puzzles_under_digit_and_transpose_bijections(self):
        count = 0
        for puzzle, solution in ((STANDARD, STANDARD_SOLUTION), (HARD, HARD_SOLUTION)):
            for shift in range(9):
                for transpose in (False, True):
                    self.check(transform(puzzle, shift, transpose),
                               transform(solution, shift, transpose))
                    count += 1
        self.assertEqual(count, 36)

    def test_solved_single_holes_and_forced_diagonal_subsets(self):
        self.check(STANDARD_SOLUTION, STANDARD_SOLUTION)
        for position in range(81):
            puzzle = [list(row) for row in STANDARD_SOLUTION]
            puzzle[position // 9][position % 9] = '.'
            self.check(puzzle, STANDARD_SOLUTION)
        for mask in range(1 << 9):
            puzzle = [list(row) for row in STANDARD_SOLUTION]
            for index in range(9):
                if mask & (1 << index):
                    puzzle[index][index] = '.'
            self.check(puzzle, STANDARD_SOLUTION)


if __name__ == '__main__':
    unittest.main()
