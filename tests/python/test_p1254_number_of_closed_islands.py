import unittest
from itertools import product

from python.p1254_number_of_closed_islands import Solution


def count_union_roots_away_from_outside(grid):
    rows, columns = len(grid), len(grid[0])
    outside = rows * columns
    parent = list(range(outside + 1))

    def root(index):
        while parent[index] != index:
            index = parent[index]
        return index

    def union(first, second):
        parent[root(first)] = root(second)

    for row in range(rows):
        for column in range(columns):
            if grid[row][column]:
                continue
            index = row * columns + column
            if row in (0, rows - 1) or column in (0, columns - 1):
                union(index, outside)
            for nr, nc in ((row + 1, column), (row, column + 1)):
                if nr < rows and nc < columns and not grid[nr][nc]:
                    union(index, nr * columns + nc)
    roots = {root(row * columns + column) for row in range(rows) for column in range(columns)
             if not grid[row][column] and root(row * columns + column) != root(outside)}
    return len(roots)


class ClosedIslandTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        if expected is None:
            expected = count_union_roots_away_from_outside(grid)
        result = Solution().closedIsland(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_binary_rectangles_against_outside_union_roots(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product((0, 1), repeat=rows * columns):
                    self.check([list(values[row * columns:(row + 1) * columns]) for row in range(rows)])
                    checks += 1
        self.assertEqual(checks, 682)

    def test_maximum_dimensions_boundary_components_checkerboard_and_empty_extensions(self):
        self.check([[0] * 100 for _ in range(100)], 0)
        self.check([[1] * 100 for _ in range(100)], 0)
        self.check([[0 if 0 < row < 99 and 0 < column < 99 else 1 for column in range(100)] for row in range(100)], 1)
        self.check([[(row + column) % 2 for column in range(100)] for row in range(100)], 4802)
        self.check([[0] * 100], 0)
        self.check([], 0)
        self.check([[]], 0)


if __name__ == '__main__':
    unittest.main()
