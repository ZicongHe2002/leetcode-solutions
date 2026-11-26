import unittest
from itertools import permutations

from python.p0051_n_queens import Solution


def valid_column_permutations(size):
    valid, checked = set(), 0
    for columns in permutations(range(size)):
        checked += 1
        if len({row - column for row, column in enumerate(columns)}) == size and len({row + column for row, column in enumerate(columns)}) == size:
            valid.add(columns)
    return valid, checked


class QueenBoardTests(unittest.TestCase):
    def normalized(self, boards, size):
        self.assertIs(type(boards), list)
        columns = []
        for board in boards:
            self.assertEqual(len(board), size)
            for row in board:
                self.assertIs(type(row), str)
                self.assertEqual(len(row), size)
                self.assertEqual(row.count('Q'), 1)
                self.assertLessEqual(set(row), {'.', 'Q'})
            columns.append(tuple(row.index('Q') for row in board))
        self.assertEqual(len(columns), len(set(columns)))
        return set(columns)

    def test_all_original_sizes_against_all_column_permutations(self):
        checked = 0
        for size in range(1, 10):
            expected, candidates = valid_column_permutations(size)
            checked += candidates
            self.assertEqual(self.normalized(Solution().solveNQueens(size), size), expected)
        self.assertEqual(checked, 409113)

    def test_unsatisfiable_sizes_and_repeated_call_result_isolation(self):
        solver = Solution()
        first = solver.solveNQueens(4)
        self.assertEqual(len(first), 2)
        first[0][0] = '....'
        self.assertEqual(solver.solveNQueens(1), [['Q']])
        expected, _ = valid_column_permutations(4)
        self.assertEqual(self.normalized(solver.solveNQueens(4), 4), expected)
        self.assertEqual(solver.solveNQueens(2), [])
        self.assertEqual(solver.solveNQueens(3), [])


if __name__ == '__main__':
    unittest.main()
