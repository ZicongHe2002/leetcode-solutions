from itertools import product
import unittest

from python.p1391_check_valid_path_in_grid import Solution


def port_masks_dsu(grid):
    rows, columns = len(grid), len(grid[0])
    parent = list(range(rows * columns))
    masks = (0, 3, 12, 9, 10, 5, 6)

    def root(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def unite(first, second):
        parent[root(first)] = root(second)

    for row in range(rows):
        for column in range(columns):
            node = row * columns + column
            mask = masks[grid[row][column]]
            if column + 1 < columns and mask & 2 and masks[grid[row][column + 1]] & 1:
                unite(node, node + 1)
            if row + 1 < rows and mask & 8 and masks[grid[row + 1][column]] & 4:
                unite(node, node + columns)
    return root(0) == root(rows * columns - 1)


class StreetGridPortMaskOracleTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        if expected is None:
            expected = port_masks_dsu(grid)
        result = Solution().hasValidPath(grid)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(grid, before)

    def test_all_small_street_type_grids_against_port_mask_dsu(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2)):
            for values in product(range(1, 7), repeat=rows * columns):
                grid = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                self.check(grid)
                checked += 1
        self.assertEqual(checked, 1806)

    def test_maximum_grid_long_snake_and_broken_reciprocal_endpoint(self):
        grid = [[1] * 300 for _ in range(300)]
        for row in range(299):
            if row % 2 == 0:
                grid[row][299], grid[row + 1][299] = 3, 5
            else:
                grid[row][0], grid[row + 1][0] = 4, 6
        self.check(grid, True)
        grid[-1][-1] = 1
        self.check(grid, False)
        self.check([[1] * 300], True)
        self.check([[2] for _ in range(300)], True)
        self.check([[1, 2]], False)
        self.check([[2, 4, 3], [6, 5, 2]], True)


if __name__ == '__main__':
    unittest.main()
