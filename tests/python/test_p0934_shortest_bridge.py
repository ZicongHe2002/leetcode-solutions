import unittest
from itertools import product

from python.p0934_shortest_bridge import Solution


def union_islands(grid):
    size = len(grid)
    parent = list(range(size * size))

    def root(index):
        while parent[index] != index:
            index = parent[index]
        return index

    for row in range(size):
        for column in range(size):
            if not grid[row][column]:
                continue
            for nr, nc in ((row + 1, column), (row, column + 1)):
                if nr < size and nc < size and grid[nr][nc]:
                    parent[root(row * size + column)] = root(nr * size + nc)
    groups = {}
    for row in range(size):
        for column in range(size):
            if grid[row][column]:
                groups.setdefault(root(row * size + column), []).append((row, column))
    return list(groups.values())


class ShortestBridgeTests(unittest.TestCase):
    def check(self, grid, expected):
        before = [row[:] for row in grid]
        result = Solution().shortestBridge(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_square_patterns_with_two_union_islands(self):
        patterns = valid = 0
        for size in (2, 3):
            for values in product((0, 1), repeat=size * size):
                patterns += 1
                grid = [list(values[row * size:(row + 1) * size]) for row in range(size)]
                groups = union_islands(grid)
                if len(groups) != 2:
                    continue
                expected = min(abs(r1 - r2) + abs(c1 - c2) - 1 for r1, c1 in groups[0] for r2, c2 in groups[1])
                self.check(grid, expected)
                valid += 1
        self.assertEqual(patterns, 528)
        self.assertGreater(valid, 0)

    def test_maximum_grid_corners_side_islands_and_surrounding_ring(self):
        grid = [[0] * 100 for _ in range(100)]
        grid[0][0] = grid[99][99] = 1
        self.check(grid, 197)
        self.check([[int(column in (0, 99)) for column in range(100)] for _ in range(100)], 98)
        grid = [[int(row in (0, 99) or column in (0, 99)) for column in range(100)] for row in range(100)]
        grid[50][50] = 1
        self.check(grid, 48)
        self.check([[0, 1], [1, 0]], 1)


if __name__ == '__main__':
    unittest.main()
