import unittest
from itertools import permutations, product

from python.p0782_transform_to_chessboard import Solution


def transposition_cost(permutation):
    seen, cycles = set(), 0
    for start in range(len(permutation)):
        if start in seen:
            continue
        cycles += 1
        index = start
        while index not in seen:
            seen.add(index)
            index = permutation[index]
    return len(permutation) - cycles


def all_target_row_column_permutations(size):
    moves = [(permutation,transposition_cost(permutation)) for permutation in permutations(range(size))]
    costs = {}
    for rows, row_cost in moves:
        for columns, column_cost in moves:
            for phase in (0,1):
                state = tuple((rows[row] + columns[column] + phase) % 2
                              for row in range(size) for column in range(size))
                costs[state] = min(costs.get(state,10000),row_cost + column_cost)
    return costs


class TransformChessboardTests(unittest.TestCase):
    def check(self, board, expected):
        before = [row[:] for row in board]
        result = Solution().movesToChessboard(board)
        self.assertIs(type(result),int)
        self.assertEqual(result,expected,board)
        self.assertEqual(board,before)

    def test_every_small_binary_board_against_all_target_permutations_and_cycle_costs(self):
        checked = 0
        for size in range(2,5):
            costs = all_target_row_column_permutations(size)
            for flat in product((0,1),repeat=size * size):
                board = [list(flat[index:index + size]) for index in range(0,len(flat),size)]
                self.check(board,costs.get(flat,-1))
                checked += 1
        self.assertEqual(checked,66064)

    def test_official_examples_maximum_phases_odd_even_blocks_and_impossible_defects(self):
        self.check([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]],2)
        self.check([[0,1],[1,0]],0)
        self.check([[1,0],[1,0]],-1)
        for phase in (0,1):
            board = [[(row + column + phase) % 2 for column in range(30)] for row in range(30)]
            self.check(board,0)
            board[15][15] ^= 1
            self.check(board,-1)
        self.check([[int(row >= 15) ^ int(column >= 15) for column in range(30)] for row in range(30)],14)
        self.check([[int(row >= 14) ^ int(column >= 14) for column in range(29)] for row in range(29)],14)
        board = [[(row + column) % 2 for column in range(30)] for row in range(30)]
        board[0] = board[1][:]
        self.check(board,-1)


if __name__ == '__main__':
    unittest.main()
