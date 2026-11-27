import unittest
from itertools import product

from python.p0909_snakes_and_ladders import Solution


def board_from_labels(size, labels):
    board = [[-1] * size for _ in range(size)]
    square = 1
    for height, row in enumerate(range(size - 1, -1, -1)):
        columns = range(size) if height % 2 == 0 else range(size - 1, -1, -1)
        for column in columns:
            board[row][column] = labels.get(square, -1)
            square += 1
    return board


def explicit_turn_graph(board):
    size = len(board)
    labels = [-1]
    for height, row in enumerate(range(size - 1, -1, -1)):
        labels.extend(board[row] if height % 2 == 0 else reversed(board[row]))
    finish = size * size
    edges = [(source, landing if labels[landing] == -1 else labels[landing])
             for source in range(1, finish) for landing in range(source + 1, min(source + 6, finish) + 1)]
    distance = [10000] * (finish + 1)
    distance[1] = 0
    for _ in range(finish - 1):
        updated = distance[:]
        for source, target in edges:
            updated[target] = min(updated[target], distance[source] + 1)
        if updated == distance:
            break
        distance = updated
    return distance[finish] if distance[finish] < 10000 else -1


class SnakeLadderTests(unittest.TestCase):
    def check(self, board, expected=None):
        before = [row[:] for row in board]
        if expected is None:
            expected = explicit_turn_graph(board)
        result = Solution().snakesAndLadders(board)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(board, before)

    def test_all_small_selected_jump_boards_against_explicit_turn_graph(self):
        checks = 0
        for size, options in ((2, (-1, 1, 2, 3, 4)), (3, (-1, 1, 9))):
            for values in product(options, repeat=size * size - 2):
                self.check(board_from_labels(size, dict(zip(range(2, size * size), values))))
                checks += 1
        self.assertEqual(checks, 2212)

    def test_maximum_board_direct_ladder_trapped_start_and_single_jump_rule(self):
        self.check(board_from_labels(20, {}), 67)
        self.check(board_from_labels(20, {2: 400}), 1)
        self.check(board_from_labels(3, {square: 1 for square in range(2, 8)}), -1)
        single_jump = {square: 1 for square in range(3, 9)}
        single_jump[2] = 8
        self.check(board_from_labels(3, single_jump), 2)


if __name__ == '__main__':
    unittest.main()
