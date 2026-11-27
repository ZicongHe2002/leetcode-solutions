import unittest
from itertools import permutations

from python.p0773_sliding_puzzle import Solution


def complete_state_graph_relaxation():
    states = list(permutations(range(6)))
    edges = {}
    for state in states:
        zero = state.index(0)
        row, column = divmod(zero, 3)
        following = []
        for target_row in range(2):
            for target_column in range(3):
                if abs(target_row - row) + abs(target_column - column) == 1:
                    index = 3 * target_row + target_column
                    moved = list(state)
                    moved[zero], moved[index] = moved[index], moved[zero]
                    following.append(tuple(moved))
        edges[state] = following
    unreachable = 10000
    distance = {state: unreachable for state in states}
    distance[(1,2,3,4,5,0)] = 0
    while True:
        updated = {state: min(distance[state], 1 + min(distance[other] for other in edges[state]))
                   for state in states}
        if updated == distance:
            break
        distance = updated
    return {state: value if value < unreachable else -1 for state, value in distance.items()}


class SlidingPuzzleTests(unittest.TestCase):
    def check(self, board, expected):
        before = [row[:] for row in board]
        result = Solution().slidingPuzzle(board)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, board)
        self.assertEqual(board, before)

    def test_every_legal_board_against_complete_coordinate_swap_graph_relaxation(self):
        distances = complete_state_graph_relaxation()
        self.assertEqual(len(distances), 720)
        self.assertEqual(sum(value >= 0 for value in distances.values()), 360)
        self.assertEqual(sum(value == -1 for value in distances.values()), 360)
        self.assertEqual(max(distances.values()), 21)
        for state, expected in distances.items():
            self.check([list(state[:3]), list(state[3:])], expected)

    def test_official_examples_and_already_solved_board(self):
        self.check([[1,2,3],[4,0,5]], 1)
        self.check([[1,2,3],[5,4,0]], -1)
        self.check([[4,1,2],[5,0,3]], 5)
        self.check([[1,2,3],[4,5,0]], 0)


if __name__ == '__main__':
    unittest.main()
