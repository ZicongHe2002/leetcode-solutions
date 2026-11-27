from itertools import product
import unittest

from python.p0959_regions_cut_by_slashes import Solution


def raster_regions(grid):
    size = len(grid) * 3
    blocked = set()
    for row, line in enumerate(grid):
        for column, symbol in enumerate(line):
            if symbol == ' ':
                continue
            for offset in range(3):
                horizontal = 2 - offset if symbol == '/' else offset
                blocked.add((3 * row + offset, 3 * column + horizontal))
    regions, seen = 0, set()
    for row in range(size):
        for column in range(size):
            start = (row, column)
            if start in blocked or start in seen:
                continue
            regions += 1
            seen.add(start)
            pending = [start]
            while pending:
                y, x = pending.pop()
                for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    following = (y + dy, x + dx)
                    if 0 <= following[0] < size and 0 <= following[1] < size:
                        if following not in blocked and following not in seen:
                            seen.add(following)
                            pending.append(following)
    return regions


class SlashRegionTests(unittest.TestCase):
    def check(self, grid):
        before = grid[:]
        result = Solution().regionsBySlashes(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, raster_regions(grid))
        self.assertEqual(grid, before)
        return result

    def test_every_small_slash_grid_against_raster_flood_fill(self):
        checks = 0
        for size in range(1, 4):
            for cells in product((' ', '/', chr(92)), repeat=size * size):
                grid = [''.join(cells[start:start + size]) for start in range(0, len(cells), size)]
                self.check(grid)
                checks += 1
        self.assertEqual(checks, 19767)

    def test_maximum_width_blank_parallel_and_alternating_slashes(self):
        self.assertEqual(self.check([' ' * 30 for _ in range(30)]), 1)
        self.assertEqual(self.check(['/' * 30 for _ in range(30)]), 60)
        self.assertEqual(self.check([chr(92) * 30 for _ in range(30)]), 60)
        self.check([''.join('/' if (row + column) % 2 else chr(92) for column in range(30))
                    for row in range(30)])


if __name__ == '__main__':
    unittest.main()
