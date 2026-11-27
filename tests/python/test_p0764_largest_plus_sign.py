import random
import unittest
from itertools import product

from python.p0764_largest_plus_sign import Solution


def all_literal_centered_pluses(n, mines):
    blocked = {tuple(cell) for cell in mines}
    best = 0
    for row, column in product(range(n), repeat=2):
        for order in range(1, n + 1):
            cells = {(row + dr * length, column + dc * length)
                     for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)) for length in range(order)}
            if all(0 <= r < n and 0 <= c < n and (r,c) not in blocked for r,c in cells):
                best = max(best, order)
    return best


class LargestPlusTests(unittest.TestCase):
    def check(self, n, mines, expected=None):
        before = [cell[:] for cell in mines]
        result = Solution().orderOfLargestPlusSign(n, mines)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_literal_centered_pluses(n, mines) if expected is None else expected, (n, mines[:20]))
        self.assertEqual(mines, before)

    def test_every_small_mine_set_and_seeded_boards_against_literal_plus_cells(self):
        checked = 0
        for n in range(1, 4):
            cells = list(product(range(n), repeat=2))
            for mask in range(1 << len(cells)):
                self.check(n, [list(cell) for index, cell in enumerate(cells) if mask >> index & 1])
                checked += 1
        self.assertEqual(checked, 530)
        rng = random.Random(764)
        for _ in range(100):
            n = rng.randrange(1, 9)
            cells = list(product(range(n), repeat=2))
            self.check(n, [list(cell) for cell in rng.sample(cells, rng.randrange(len(cells) + 1))])

    def test_official_examples_maximum_grid_and_legal_mine_count_boundaries(self):
        self.check(5, [[4,2]], 2)
        self.check(1, [[0,0]], 0)
        self.check(1, [], 1)
        self.check(500, [], 250)
        self.check(500, [[r,c] for r in range(10) for c in range(500)], 245)
        self.check(70, [[r,c] for r in range(70) for c in range(70)], 0)


if __name__ == '__main__':
    unittest.main()
