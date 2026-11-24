import unittest
from itertools import product

from python.p0994_rotting_oranges import Solution


def synchronous_simulation(grid):
    state = [row[:] for row in grid]
    minutes = 0
    while any(value == 1 for row in state for value in row):
        next_state = [row[:] for row in state]
        for r, row in enumerate(state):
            for c, value in enumerate(row):
                if value == 1 and any(0 <= nr < len(state) and 0 <= nc < len(row)
                                      and state[nr][nc] == 2
                                      for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]):
                    next_state[r][c] = 2
        if next_state == state:
            return -1, state
        minutes += 1
        state = next_state
    return minutes, state


class RottingTests(unittest.TestCase):
    def check(self, grid, expected=None):
        rows = grid[:]
        minutes, final = synchronous_simulation(grid)
        if expected is not None:
            self.assertEqual(minutes, expected)
        self.assertEqual(Solution().orangesRotting(grid), minutes)
        self.assertEqual(grid, final)
        for actual, original in zip(grid, rows):
            self.assertIs(actual, original)

    def test_all_small_three_state_grids_against_synchronous_simulation(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2)]:
            for values in product(range(3), repeat=height * width):
                self.check([list(values[r * width:(r + 1) * width]) for r in range(height)])
                checks += 1
        self.assertEqual(checks, 1569)

    def test_examples_unreachable_and_maximum_dimensions(self):
        self.check([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
        self.check([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1)
        self.check([[0, 2]], 0)
        self.check([[1]], -1)
        self.check([], 0)
        self.check([[]], 0)
        grid = [[1] * 10 for _ in range(10)]
        grid[0][0] = 2
        self.check(grid, 18)


if __name__ == '__main__':
    unittest.main()
