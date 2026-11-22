from itertools import product
import unittest

from python.p1631_path_with_minimum_effort import Solution


def ascending_threshold_connectivity(heights):
    rows, columns = len(heights), len(heights[0])
    thresholds = {0}
    for row in range(rows):
        for column in range(columns):
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = row + dr, column + dc
                if nr < rows and nc < columns:
                    thresholds.add(abs(heights[nr][nc] - heights[row][column]))
    for limit in sorted(thresholds):
        reachable = {(0, 0)}
        pending = [(0, 0)]
        for row, column in pending:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = row + dr, column + dc
                if (0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in reachable
                        and abs(heights[nr][nc] - heights[row][column]) <= limit):
                    reachable.add((nr, nc))
                    pending.append((nr, nc))
        if (rows - 1, columns - 1) in reachable:
            return limit
    raise AssertionError('a finite rectangular grid must have a path')


class MinimumEffortBottleneckTests(unittest.TestCase):
    def check(self, heights, expected=None):
        before = [row[:] for row in heights]
        if expected is None:
            expected = ascending_threshold_connectivity(heights)
        result = Solution().minimumEffortPath(heights)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(heights, before)

    def test_every_small_three_height_grid_against_threshold_connectivity(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                if rows * columns > 6:
                    continue
                for flat in product((1, 2, 4), repeat=rows * columns):
                    self.check([list(flat[start:start + columns])
                                for start in range(0, len(flat), columns)])
                    checks += 1
        self.assertEqual(checks, 1614)

    def test_maximum_grid_height_extremes_degenerate_axes_and_zero_effort_detour(self):
        self.check([[7] * 100 for _ in range(100)], 0)
        self.check([[1 if (row + column) % 2 == 0 else 1000000
                     for column in range(100)] for row in range(100)], 999999)
        self.check([[row * 100 + column + 1 for column in range(100)] for row in range(100)], 100)
        self.check([[value * 10000 + 1 for value in range(100)]], 10000)
        self.check([[value * 10000 + 1] for value in range(100)], 10000)
        self.check([[1000000]], 0)
        self.check([[1, 2, 1, 1, 1], [1, 2, 1, 2, 1], [1, 2, 1, 2, 1],
                    [1, 2, 1, 2, 1], [1, 1, 1, 2, 1]], 0)


if __name__ == '__main__':
    unittest.main()
