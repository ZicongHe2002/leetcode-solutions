from itertools import product
import unittest

from python.p1905_count_sub_islands import Solution


def grid2_dsu_bad_roots(grid1, grid2):
    rows, columns = len(grid2), len(grid2[0])
    parents = {row * columns + column: row * columns + column
               for row in range(rows) for column in range(columns) if grid2[row][column]}

    def root(node):
        while parents[node] != node:
            node = parents[node]
        return node

    for row in range(rows):
        for column in range(columns):
            node = row * columns + column
            if node not in parents:
                continue
            for nr, nc in ((row + 1, column), (row, column + 1)):
                if nr < rows and nc < columns and grid2[nr][nc]:
                    parents[root(node)] = root(nr * columns + nc)
    all_roots = {root(node) for node in parents}
    bad_roots = {root(node) for node in parents if grid1[node // columns][node % columns] == 0}
    return len(all_roots - bad_roots)


class SubIslandDSURootTests(unittest.TestCase):
    def check(self, first, second, expected=None):
        before = ([row[:] for row in first], [row[:] for row in second])
        if expected is None:
            expected = grid2_dsu_bad_roots(first, second)
        result = Solution().countSubIslands(first, second)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual((first, second), before)

    def test_all_small_pairs_of_binary_grids_against_dsu_bad_components(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2)):
            cells = rows * columns
            for values in product((0, 1), repeat=2 * cells):
                first = [list(values[row * columns:(row + 1) * columns]) for row in range(rows)]
                second = [list(values[cells + row * columns:cells + (row + 1) * columns]) for row in range(rows)]
                self.check(first, second)
                checked += 1
        self.assertEqual(checked, 8484)

    def test_maximum_grids_single_bad_cell_and_many_separated_islands(self):
        first = [[1] * 500 for _ in range(500)]
        second = [[1] * 500 for _ in range(500)]
        self.check(first, second, 1)
        first[250][250] = 0
        self.check(first, second, 0)
        first[250][250] = 1
        second = [[int((row + column) % 2 == 0) for column in range(500)] for row in range(500)]
        self.check(first, second, 125000)


if __name__ == '__main__':
    unittest.main()
