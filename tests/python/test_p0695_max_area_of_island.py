import unittest
from itertools import product

from python.p0695_max_area_of_island import Solution


def union_find_area(grid):
    parent = {(r, c): (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == 1}

    def find(point):
        while parent[point] != point:
            point = parent[point]
        return point

    for r, c in parent:
        for neighbor in [(r + 1, c), (r, c + 1)]:
            if neighbor in parent:
                parent[find((r, c))] = find(neighbor)
    sizes = {}
    for point in parent:
        root = find(point)
        sizes[root] = sizes.get(root, 0) + 1
    return max(sizes.values(), default=0)


class IslandAreaTests(unittest.TestCase):
    def check(self, grid, expected):
        before, rows = [row[:] for row in grid], grid[:]
        self.assertEqual(Solution().maxAreaOfIsland(grid), expected)
        self.assertEqual(grid, before)
        for actual, original in zip(grid, rows):
            self.assertIs(actual, original)

    def test_all_small_binary_grids_against_union_find(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]:
            for values in product(range(2), repeat=height * width):
                grid = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(grid, union_find_area(grid))
                checks += 1
        self.assertEqual(checks, 66202)

    def test_empty_diagonals_and_maximum_grids(self):
        self.check([], 0)
        self.check([[]], 0)
        self.check([[1]], 1)
        self.check([[1, 0], [0, 1]], 1)
        self.check([[0] * 50 for _ in range(50)], 0)
        self.check([[1] * 50 for _ in range(50)], 2500)
        self.check([[(r + c) % 2 for c in range(50)] for r in range(50)], 1)


if __name__ == '__main__':
    unittest.main()
