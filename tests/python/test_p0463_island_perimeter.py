from collections import deque
from itertools import product
import unittest

from python.p0463_island_perimeter import Solution


def original_single_island_without_lakes(grid):
    rows, columns = len(grid), len(grid[0])
    land = {(row, column) for row in range(rows) for column in range(columns) if grid[row][column]}
    if not land:
        return False
    root = next(iter(land))
    seen, queue = {root}, deque([root])
    while queue:
        row, column = queue.popleft()
        for point in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
            if point in land and point not in seen:
                seen.add(point)
                queue.append(point)
    if seen != land:
        return False
    outside, queue = {(-1, -1)}, deque([(-1, -1)])
    while queue:
        row, column = queue.popleft()
        for point in ((row - 1, column), (row + 1, column), (row, column - 1), (row, column + 1)):
            x, y = point
            if -1 <= x <= rows and -1 <= y <= columns and point not in land and point not in outside:
                outside.add(point)
                queue.append(point)
    return all((row, column) in outside for row in range(rows) for column in range(columns)
               if grid[row][column] == 0)


def geometric_edge_set_oracle(grid):
    edges = set()
    for row, values in enumerate(grid):
        for column, value in enumerate(values):
            if value:
                corners = [(row, column), (row + 1, column), (row + 1, column + 1), (row, column + 1)]
                for first, second in zip(corners, corners[1:] + corners[:1]):
                    edge = tuple(sorted((first, second)))
                    if edge in edges:
                        edges.remove(edge)
                    else:
                        edges.add(edge)
    return len(edges)


class IslandSharedEdgeTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        actual = Solution().islandPerimeter(grid)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, geometric_edge_set_oracle(grid) if expected is None else expected)
        self.assertEqual(grid, before)

    def test_every_legal_three_by_three_single_island_without_lakes(self):
        grids = 0
        for cells in product((0, 1), repeat=9):
            grid = [list(cells[row * 3:(row + 1) * 3]) for row in range(3)]
            if original_single_island_without_lakes(grid):
                self.check(grid)
                grids += 1
        self.assertEqual(grids, 213)

    def test_maximum_dimensions_solid_strips_and_comb_boundary(self):
        self.check([[1] * 100 for _ in range(100)], 400)
        self.check([[1] * 100], 202)
        self.check([[1] for _ in range(100)], 202)
        self.check([[int(row == 0 or column % 2 == 0) for column in range(100)] for row in range(100)], 10102)
        self.check([[1]], 4)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
