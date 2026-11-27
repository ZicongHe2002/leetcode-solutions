import random
import unittest
from itertools import combinations, product

from python.p0750_number_of_corner_rectangles import Solution


def all_four_corner_choices(grid):
    return sum(grid[top][left] == grid[top][right] == grid[bottom][left] == grid[bottom][right] == 1
               for top, bottom in combinations(range(len(grid)), 2)
               for left, right in combinations(range(len(grid[0])), 2))


class CornerRectanglesTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        self.assertTrue(1 <= sum(map(sum, grid)) <= 6000)
        result = Solution().countCornerRectangles(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_four_corner_choices(grid) if expected is None else expected)
        self.assertEqual(grid, before)

    def test_every_small_nonzero_binary_grid_and_seeded_grids_against_literal_four_corners(self):
        checked = 0
        for rows in range(1, 4):
            for columns in range(1, 5):
                for values in product((0, 1), repeat=rows * columns):
                    if not any(values):
                        continue
                    self.check([list(values[start:start + columns]) for start in range(0, len(values), columns)])
                    checked += 1
        self.assertEqual(checked, 5038)
        rng = random.Random(750)
        for _ in range(100):
            rows, columns = rng.randrange(1, 8), rng.randrange(1, 8)
            grid = [[rng.randrange(2) for _ in range(columns)] for _ in range(rows)]
            if not any(map(any, grid)):
                grid[0][0] = 1
            self.check(grid)

    def test_examples_hollow_corners_and_maximum_dimensions_with_six_thousand_ones(self):
        self.check([[1,0,0,1,0],[0,0,1,0,1],[0,0,0,1,0],[1,0,1,0,1]], 1)
        self.check([[1,1,1],[1,1,1],[1,1,1]], 9)
        self.check([[1,0,1],[0,0,0],[1,0,1]], 1)
        self.check([[1] * 200], 0)
        self.check([[1] for _ in range(200)], 0)
        grid = [[1] * 200 for _ in range(30)] + [[0] * 200 for _ in range(170)]
        self.assertEqual((len(grid), len(grid[0]), sum(map(sum, grid))), (200, 200, 6000))
        self.check(grid, 8656500)


if __name__ == '__main__':
    unittest.main()
