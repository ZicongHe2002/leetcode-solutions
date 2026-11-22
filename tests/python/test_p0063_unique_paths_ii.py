import unittest
from itertools import product
from math import comb

from python.p0063_unique_paths_ii import Solution


def count_by_enumerating_routes(grid):
    def walk(row, column):
        if row == len(grid) or column == len(grid[0]) or grid[row][column]:
            return 0
        if row == len(grid) - 1 and column == len(grid[0]) - 1:
            return 1
        return walk(row + 1, column) + walk(row, column + 1)
    return walk(0, 0)


class ObstaclePathTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        if expected is None:
            expected = count_by_enumerating_routes(grid)
        self.assertLessEqual(expected, 2 * 10**9)
        result = Solution().uniquePathsWithObstacles(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_binary_rectangles_against_route_enumeration(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product((0, 1), repeat=rows * columns):
                    self.check([list(values[row * columns:(row + 1) * columns]) for row in range(rows)])
                    checks += 1
        self.assertEqual(checks, 682)

    def test_maximum_dimensions_blocked_ends_unique_corridor_and_bounded_many_paths(self):
        self.check([[1] * 100 for _ in range(100)], 0)
        blocked_end = [[0] * 100 for _ in range(100)]
        blocked_end[-1][-1] = 1
        self.check(blocked_end, 0)
        corridor = [[1] * 100 for _ in range(100)]
        corridor[0] = [0] * 100
        for row in corridor:
            row[-1] = 0
        self.check(corridor, 1)
        many = [[1] * 100 for _ in range(100)]
        for row in range(17):
            many[row][:17] = [0] * 17
        many[16] = [0] * 100
        for row in range(16, 100):
            many[row][-1] = 0
        self.check(many, comb(32, 16))


if __name__ == '__main__':
    unittest.main()
