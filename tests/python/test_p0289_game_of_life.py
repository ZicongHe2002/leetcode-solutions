from collections import Counter
from itertools import product
import unittest

from python.p0289_game_of_life import Solution


def sparse_live_neighbor_reference(board):
    living = {(row, column) for row in range(len(board))
              for column in range(len(board[0])) if board[row][column]}
    counts = Counter((row + dr, column + dc) for row, column in living
                     for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc)
    return [[int(counts[row, column] == 3 or
                 ((row, column) in living and counts[row, column] == 2))
             for column in range(len(board[0]))] for row in range(len(board))]


class InPlaceSynchronousLifeTests(unittest.TestCase):
    def check(self, board):
        expected = sparse_live_neighbor_reference(board)
        outer_identity = id(board)
        row_identities = [id(row) for row in board]
        result = Solution().gameOfLife(board)
        self.assertIsNone(result)
        self.assertEqual(id(board), outer_identity)
        self.assertEqual([id(row) for row in board], row_identities)
        self.assertEqual(board, expected)
        self.assertTrue(all(type(value) is int and value in (0, 1) for row in board for value in row))

    def test_all_small_binary_boards_against_sparse_live_neighbor_counts(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for flat in product((0, 1), repeat=rows * columns):
                    self.check([list(flat[start:start + columns])
                                for start in range(0, len(flat), columns)])
                    checks += 1
        self.assertEqual(checks, 682)

    def test_current_maximum_dimensions_edges_and_multiple_generations(self):
        self.check([[0] * 25 for _ in range(25)])
        self.check([[1] * 25 for _ in range(25)])
        self.check([[int((7 * row + 11 * column) % 5 == 0)
                     for column in range(25)] for row in range(25)])
        self.check([[1] * 25])
        self.check([[1] for _ in range(25)])
        glider = [[0] * 25 for _ in range(25)]
        for row, column in ((5, 6), (6, 7), (7, 5), (7, 6), (7, 7)):
            glider[row][column] = 1
        for _ in range(4):
            self.check(glider)
        self.check([[1, 1], [1, 0]])


if __name__ == '__main__':
    unittest.main()
