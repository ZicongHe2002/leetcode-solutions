import unittest
from itertools import combinations, product

from python.p0064_minimum_path_sum import Solution


def all_paths_oracle(grid):
    rows, columns = len(grid), len(grid[0])
    sums = []
    for down_positions in combinations(range(rows + columns - 2), rows - 1):
        down = set(down_positions)
        row = column = 0
        total = grid[0][0]
        for step in range(rows + columns - 2):
            if step in down:
                row += 1
            else:
                column += 1
            total += grid[row][column]
        sums.append(total)
    return min(sums)


class MinimumPathTests(unittest.TestCase):
    def check(self, grid, expected):
        before, rows = [row[:] for row in grid], grid[:]
        self.assertEqual(Solution().minPathSum(grid), expected)
        self.assertEqual(grid, before)
        for actual, original in zip(grid, rows):
            self.assertIs(actual, original)

    def test_all_small_weighted_grids_against_complete_path_enumeration(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
            alphabet = range(2) if (height, width) == (3, 3) else range(3)
            for values in product(alphabet, repeat=height * width):
                grid = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(grid, all_paths_oracle(grid))
                checks += 1
        self.assertEqual(checks, 2081)

    def test_examples_maximum_grid_and_empty_extensions(self):
        self.check([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)
        self.check([[200] * 200 for _ in range(200)], 79800)
        self.check([[200] for _ in range(200)], 40000)
        self.check([[200] * 200], 40000)
        self.check([[0] * 200 for _ in range(200)], 0)
        self.check([], 0)
        self.check([[]], 0)


if __name__ == '__main__':
    unittest.main()
