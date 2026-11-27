import random
import unittest
from itertools import product

from python.p0694_number_of_distinct_islands import Solution


def can_translate(first, second):
    if len(first) != len(second):
        return False
    r, c = next(iter(first))
    return any({(x + nr - r, y + nc - c) for x, y in first} == second for nr, nc in second)


def union_and_compare(grid):
    rows, columns = len(grid), len(grid[0])
    parent = {(r, c): (r, c) for r in range(rows) for c in range(columns) if grid[r][c]}

    def find(cell):
        while parent[cell] != cell:
            cell = parent[cell]
        return cell

    for r, c in parent:
        for neighbour in ((r + 1, c), (r, c + 1)):
            if neighbour in parent:
                parent[find((r, c))] = find(neighbour)
    components = {}
    for cell in parent:
        components.setdefault(find(cell), set()).add(cell)
    representatives = []
    for component in components.values():
        if not any(can_translate(component, old) for old in representatives):
            representatives.append(component)
    return len(representatives)


class DistinctIslandsTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before, row_ids = [row[:] for row in grid], [id(row) for row in grid]
        result = Solution().numDistinctIslands(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, union_and_compare(grid) if expected is None else expected)
        self.assertEqual(grid, before)
        self.assertEqual([id(row) for row in grid], row_ids)

    def test_all_small_binary_matrices_and_seeded_shapes_against_actual_translation(self):
        checked = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for cells in product((0, 1), repeat=rows * columns):
                    self.check([list(cells[r * columns:(r + 1) * columns]) for r in range(rows)])
                    checked += 1
        self.assertEqual(checked, 682)
        rng = random.Random(694)
        for _ in range(200):
            rows, columns = rng.randrange(1, 9), rng.randrange(1, 9)
            self.check([[rng.randrange(2) for _ in range(columns)] for _ in range(rows)])

    def test_fifty_by_fifty_grids_orientation_and_holes(self):
        self.check([[0] * 50 for _ in range(50)], 0)
        self.check([[1] * 50 for _ in range(50)], 1)
        self.check([[(r + c) % 2 for c in range(50)] for r in range(50)], 1)
        grid = [[0] * 50 for _ in range(50)]
        square = {(0, 0), (0, 1), (1, 0), (1, 1)}
        for i, missing in enumerate(sorted(square)):
            for offset in (0, 20):
                for r, c in square - {missing}:
                    grid[r + offset][c + 4 * i] = 1
        self.check(grid, 4)
        holes = [[0] * 8 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                holes[r][c] = int((r, c) != (1, 1))
                holes[r][c + 5] = 1
        self.check(holes, 2)


if __name__ == '__main__':
    unittest.main()
