import unittest
from itertools import product

from python.p0741_cherry_pickup import Solution


def actual_path_pair_union(grid):
    size, paths = len(grid), []

    def walk(row, column, visited):
        if row >= size or column >= size or grid[row][column] == -1:
            return
        visited = visited + ((row, column),)
        if row == column == size - 1:
            paths.append(frozenset(visited))
            return
        walk(row + 1, column, visited)
        walk(row, column + 1, visited)

    walk(0, 0, ())
    return max((sum(grid[row][column] for row, column in left | right)
                for left in paths for right in paths), default=0)


class CherryPickupTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        result = Solution().cherryPickup(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_path_pair_union(grid) if expected is None else expected, grid)
        self.assertEqual(grid, before)

    def test_every_small_legal_endpoint_grid_against_actual_path_pair_unions(self):
        checked = 0
        for size in (1, 2, 3):
            interior = [(row, column) for row in range(size) for column in range(size)
                        if (row, column) not in ((0, 0), (size - 1, size - 1))]
            for values in product((-1, 0, 1), repeat=len(interior)):
                for endpoints in product((0, 1), repeat=1 if size == 1 else 2):
                    grid = [[0] * size for _ in range(size)]
                    grid[0][0], grid[-1][-1] = endpoints[0], endpoints[-1]
                    for (row, column), value in zip(interior, values):
                        grid[row][column] = value
                    self.check(grid)
                    checked += 1
        self.assertEqual(checked, 8786)

    def test_official_examples_fifty_square_closed_forms_and_blocked_paths(self):
        self.check([[0,1,-1],[1,0,-1],[1,1,1]], 5)
        self.check([[1,1,-1],[1,-1,1],[-1,1,1]], 0)
        self.check([[1] * 50 for _ in range(50)], 196)
        self.check([[0] * 50 for _ in range(50)], 0)
        blocked = [[1] * 50 for _ in range(50)]
        blocked[25] = [-1] * 50
        self.check(blocked, 0)
        corridor = [[-1] * 50 for _ in range(50)]
        corridor[0] = [1] * 50
        for row in range(50):
            corridor[row][-1] = 1
        self.check(corridor, 99)


if __name__ == '__main__':
    unittest.main()
