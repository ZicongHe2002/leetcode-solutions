from itertools import combinations, product
import unittest

from python.p0529_minesweeper import Solution


def static_zero_region_reveal(board, click):
    output = [row[:] for row in board]
    start = tuple(click)
    if board[start[0]][start[1]] == 'M':
        output[start[0]][start[1]] = 'X'
        return output
    mines = [(row, column) for row in range(len(board)) for column in range(len(board[0]))
             if board[row][column] == 'M']
    counts = {(row, column): sum(max(abs(row - mr), abs(column - mc)) == 1 for mr, mc in mines)
              for row in range(len(board)) for column in range(len(board[0])) if board[row][column] == 'E'}
    if counts[start]:
        output[start[0]][start[1]] = str(counts[start])
        return output
    parents = {cell: cell for cell, count in counts.items() if count == 0}

    def root(cell):
        while parents[cell] != cell:
            cell = parents[cell]
        return cell

    for first, second in combinations(parents, 2):
        if max(abs(first[0] - second[0]), abs(first[1] - second[1])) == 1:
            parents[root(first)] = root(second)
    region = {cell for cell in parents if root(cell) == root(start)}
    for cell, count in counts.items():
        if cell in region or any(max(abs(cell[0] - zr), abs(cell[1] - zc)) == 1 for zr, zc in region):
            output[cell[0]][cell[1]] = str(count) if count else 'B'
    return output


class MinesweeperStaticRegionTests(unittest.TestCase):
    def check(self, board, click, expected=None):
        if expected is None:
            expected = static_zero_region_reveal(board, click)
        before_click = click[:]
        result = Solution().updateBoard(board, click)
        self.assertIs(result, board)
        self.assertEqual(board, expected)
        self.assertEqual(click, before_click)

    def test_every_small_fresh_board_and_every_unrevealed_click(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)):
            for values in product('ME', repeat=rows * columns):
                original = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                for row in range(rows):
                    for column in range(columns):
                        self.check([line[:] for line in original], [row, column])
                        checked += 1
        self.assertEqual(checked, 5458)

    def test_maximum_boards_eight_mines_and_partly_revealed_input(self):
        self.check([['E'] * 50 for _ in range(50)], [25, 25], [['B'] * 50 for _ in range(50)])
        board = [['M'] * 50 for _ in range(50)]
        expected = [row[:] for row in board]
        expected[0][0] = 'X'
        self.check(board, [0, 0], expected)
        self.check([['M', 'M', 'M'], ['M', 'E', 'M'], ['M', 'M', 'M']], [1, 1],
                   [['M', 'M', 'M'], ['M', '8', 'M'], ['M', 'M', 'M']])
        board = [['E'] * 5 for _ in range(4)]
        board[1][2] = 'M'
        self.check(board, [3, 0])
        self.assertEqual(board[0][2], 'E')
        self.check(board, [0, 2])
        self.check(board, [1, 2])


if __name__ == '__main__':
    unittest.main()
