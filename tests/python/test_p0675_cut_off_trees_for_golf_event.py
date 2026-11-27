import random
import unittest
from itertools import product

from python.p0675_cut_off_trees_for_golf_event import Solution


def all_pairs_paths(forest):
    rows, columns = len(forest), len(forest[0])
    if forest[0][0] == 0:
        return -1
    cells = [(r, c) for r in range(rows) for c in range(columns) if forest[r][c]]
    index = {cell: i for i, cell in enumerate(cells)}
    distances = [[float('inf')] * len(cells) for _ in cells]
    for i, (r, c) in enumerate(cells):
        distances[i][i] = 0
        for j, (nr, nc) in enumerate(cells):
            if abs(r - nr) + abs(c - nc) == 1:
                distances[i][j] = 1
    for middle in range(len(cells)):
        for first in range(len(cells)):
            for last in range(len(cells)):
                distances[first][last] = min(distances[first][last],
                                              distances[first][middle] + distances[middle][last])
    targets = sorted((forest[r][c], (r, c)) for r, c in cells if forest[r][c] > 1)
    route = [(0, 0)] + [cell for _, cell in targets]
    total = sum(distances[index[first]][index[last]] for first, last in zip(route, route[1:]))
    return -1 if total == float('inf') else int(total)


def labelled_grid(kinds, rows, columns, reverse=False):
    positions = [i for i, kind in enumerate(kinds) if kind == 2]
    heights = {position: height + 2 for height, position in enumerate(
        reversed(positions) if reverse else positions)}
    flat = [heights[i] if kind == 2 else kind for i, kind in enumerate(kinds)]
    return [flat[r * columns:(r + 1) * columns] for r in range(rows)]


class CutForestTreesTests(unittest.TestCase):
    def check(self, forest, expected=None):
        before = [row[:] for row in forest]
        row_ids = [id(row) for row in forest]
        if expected is None:
            expected = all_pairs_paths(forest)
        result = Solution().cutOffTree(forest)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, forest)
        self.assertEqual(forest, before)
        self.assertEqual([id(row) for row in forest], row_ids)

    def test_all_small_terrain_and_two_height_orders_against_floyd_warshall(self):
        checked = 0
        for rows, columns in ((1, 1), (1, 2), (2, 2), (2, 3)):
            for kinds in product((0, 1, 2), repeat=rows * columns):
                if 2 not in kinds:
                    continue
                for reverse in (False, True):
                    self.check(labelled_grid(kinds, rows, columns, reverse))
                    checked += 1
        self.assertEqual(checked, 1472)
        rng = random.Random(675)
        for _ in range(200):
            rows, columns = rng.randrange(1, 5), rng.randrange(1, 5)
            kinds = [rng.randrange(3) for _ in range(rows * columns)]
            kinds[rng.randrange(len(kinds))] = 2
            self.check(labelled_grid(kinds, rows, columns, bool(rng.randrange(2))))

    def test_maximum_grid_all_trees_obstacles_start_and_future_tree_transit(self):
        self.check([[2 + r * 50 + c for c in range(50)] for r in range(50)], 4900)
        self.check([[2501 - r * 50 - c for c in range(50)] for r in range(50)], 4998)
        grid = [[1] * 50 for _ in range(50)]
        grid[-1][-1] = 10**9
        self.check(grid, 98)
        grid[24] = [0] * 50
        self.check(grid, -1)
        self.check([[0, 2]], -1)
        self.check([[2]], 0)
        self.check([[1, 100, 2]], 3)
        self.check([[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6)


if __name__ == '__main__':
    unittest.main()
