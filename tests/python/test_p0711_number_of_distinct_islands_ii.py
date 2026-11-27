import random
import unittest
from itertools import product

from python.p0711_number_of_distinct_islands_ii import Solution


def actual_motion_matches(first, second):
    if len(first) != len(second):
        return False
    for reflected in (False, True):
        moved = {(r, -c if reflected else c) for r, c in first}
        for _ in range(4):
            ar, ac = next(iter(moved))
            if any({(r + br - ar, c + bc - ac) for r, c in moved} == second for br, bc in second):
                return True
            moved = {(c, -r) for r, c in moved}
    return False


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
        if not any(actual_motion_matches(component, other) for other in representatives):
            representatives.append(component)
    return len(representatives)


class DistinctIslandsIITests(unittest.TestCase):
    def check(self, grid, expected=None):
        before, row_ids = [row[:] for row in grid], [id(row) for row in grid]
        result = Solution().numDistinctIslands2(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, union_and_compare(grid) if expected is None else expected)
        self.assertEqual(grid, before)
        self.assertEqual([id(row) for row in grid], row_ids)

    def test_all_small_binary_grids_and_seeded_shapes_against_actual_motions(self):
        checked = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for cells in product((0, 1), repeat=rows * columns):
                    self.check([list(cells[r * columns:(r + 1) * columns]) for r in range(rows)])
                    checked += 1
        self.assertEqual(checked, 682)
        rng = random.Random(711)
        for _ in range(200):
            rows, columns = rng.randrange(1, 9), rng.randrange(1, 9)
            self.check([[rng.randrange(2) for _ in range(columns)] for _ in range(rows)])

    def test_fifty_by_fifty_all_eight_chiral_orientations_and_holes(self):
        self.check([[0] * 50 for _ in range(50)], 0)
        self.check([[1] * 50 for _ in range(50)], 1)
        self.check([[(r + c) % 2 for c in range(50)] for r in range(50)], 1)
        shape = {(0, 1), (0, 2), (1, 0), (1, 1), (2, 1)}
        variants = []
        for reflected in (False, True):
            moved = {(r, -c if reflected else c) for r, c in shape}
            for _ in range(4):
                variants.append(moved)
                moved = {(c, -r) for r, c in moved}
        grid = [[0] * 50 for _ in range(50)]
        for i, moved in enumerate(variants):
            minimum_r, minimum_c = min(r for r, _ in moved), min(c for _, c in moved)
            for r, c in moved:
                grid[r - minimum_r + 1 + 8 * (i // 4)][c - minimum_c + 1 + 8 * (i % 4)] = 1
        self.check(grid, 1)
        holes = [[0] * 8 for _ in range(3)]
        for r in range(3):
            for c in range(3):
                holes[r][c] = int((r, c) != (1, 1))
                holes[r][c + 5] = 1
        self.check(holes, 2)


if __name__ == '__main__':
    unittest.main()
