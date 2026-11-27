from itertools import permutations
from random import Random
import unittest

from python.p0778_swim_in_rising_water import Solution


def water_threshold_binary_search(grid):
    size = len(grid)

    def connected(level):
        if grid[0][0] > level:
            return False
        reachable = {(0, 0)}
        pending = [(0, 0)]
        for row, column in pending:
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = row + dr, column + dc
                if (0 <= nr < size and 0 <= nc < size and (nr, nc) not in reachable
                        and grid[nr][nc] <= level):
                    reachable.add((nr, nc))
                    pending.append((nr, nc))
        return (size - 1, size - 1) in reachable

    low, high = max(grid[0][0], grid[-1][-1]), size * size - 1
    while low < high:
        middle = (low + high) // 2
        if connected(middle):
            high = middle
        else:
            low = middle + 1
    return low


class RisingWaterBottleneckTests(unittest.TestCase):
    def check(self, grid, expected=None):
        before = [row[:] for row in grid]
        size = len(grid)
        self.assertEqual(sorted(value for row in grid for value in row), list(range(size * size)))
        if expected is None:
            expected = water_threshold_binary_search(grid)
        result = Solution().swimInWater(grid)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertGreaterEqual(result, max(grid[0][0], grid[-1][-1]))
        self.assertEqual(grid, before)

    def test_every_tiny_permutation_and_seeded_three_by_three_permutations(self):
        checks = 0
        for size in (1, 2):
            for flat in permutations(range(size * size)):
                self.check([list(flat[start:start + size]) for start in range(0, len(flat), size)])
                checks += 1
        self.assertEqual(checks, 25)
        random = Random(778)
        flat = list(range(9))
        for _ in range(300):
            random.shuffle(flat)
            self.check([flat[start:start + 3] for start in range(0, 9, 3)])

    def test_maximum_size_endpoint_levels_serpentine_and_seeded_permutations(self):
        size = 50
        ordered = [[row * size + column for column in range(size)] for row in range(size)]
        self.check(ordered, 2499)
        self.check([[2499 - value for value in row] for row in ordered], 2499)
        serpentine = [row[:] if index % 2 == 0 else row[::-1] for index, row in enumerate(ordered)]
        self.check(serpentine, 2450)
        random = Random(77850)
        flat = list(range(size * size))
        for _ in range(2):
            random.shuffle(flat)
            self.check([flat[start:start + size] for start in range(0, len(flat), size)])


if __name__ == '__main__':
    unittest.main()
