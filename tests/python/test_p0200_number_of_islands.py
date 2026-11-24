import unittest
from itertools import product

from python.p0200_number_of_islands import Solution


def union_find_count(grid):
    parent = {(r, c): (r, c) for r, row in enumerate(grid) for c, value in enumerate(row) if value == '1'}

    def find(point):
        while parent[point] != point:
            point = parent[point]
        return point

    for r, c in parent:
        for neighbor in [(r + 1, c), (r, c + 1)]:
            if neighbor in parent:
                parent[find((r, c))] = find(neighbor)
    return len({find(point) for point in parent})


class IslandCountTests(unittest.TestCase):
    def check(self, grid, expected):
        before, rows = [row[:] for row in grid], grid[:]
        self.assertEqual(Solution().numIslands(grid), expected)
        self.assertEqual(grid, before)
        for actual, original in zip(grid, rows):
            self.assertIs(actual, original)

    def test_all_small_character_grids_against_union_find(self):
        checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]:
            for values in product('01', repeat=height * width):
                grid = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                self.check(grid, union_find_count(grid))
                checks += 1
        self.assertEqual(checks, 66202)

    def test_empty_lines_diagonals_and_maximum_grids(self):
        self.check([], 0)
        self.check([[]], 0)
        self.check([list('10101')], 3)
        self.check([['1'], ['0'], ['1']], 2)
        self.check([list('10'), list('01')], 2)
        self.check([['0'] * 300 for _ in range(300)], 0)
        self.check([['1'] * 300 for _ in range(300)], 1)
        self.check([[str((r + c) % 2) for c in range(300)] for r in range(300)], 45000)


if __name__ == '__main__':
    unittest.main()
