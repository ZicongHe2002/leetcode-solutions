import unittest
from itertools import product

from python.p0174_dungeon_game import Solution


def minimum_health_by_forward_paths(dungeon):
    def walk(row, column, total, lowest):
        total += dungeon[row][column]
        lowest = min(lowest, total)
        if row == len(dungeon) - 1 and column == len(dungeon[0]) - 1:
            return max(1, 1 - lowest)
        choices = []
        if row + 1 < len(dungeon):
            choices.append(walk(row + 1, column, total, lowest))
        if column + 1 < len(dungeon[0]):
            choices.append(walk(row, column + 1, total, lowest))
        return min(choices)
    return walk(0, 0, 0, 0)


class DungeonHealthTests(unittest.TestCase):
    def check(self, dungeon, expected=None):
        before = [row[:] for row in dungeon]
        if expected is None:
            expected = minimum_health_by_forward_paths(dungeon)
        result = Solution().calculateMinimumHP(dungeon)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(dungeon, before)

    def test_all_small_ternary_rectangles_against_forward_paths(self):
        checks = 0
        for rows in range(1, 4):
            for columns in range(1, 4):
                for values in product((-2, 0, 3), repeat=rows * columns):
                    self.check([list(values[row * columns:(row + 1) * columns]) for row in range(rows)])
                    checks += 1
        self.assertEqual(checks, 21297)

    def test_maximum_dimensions_damage_healing_zero_and_prefix_survival(self):
        self.check([[-1000] * 200 for _ in range(200)], 399001)
        self.check([[1000] * 200 for _ in range(200)], 1)
        self.check([[0] * 200 for _ in range(200)], 1)
        self.check([[100, -200, 100]], 101)
        self.check([[-1000]], 1001)
        self.check([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7)


if __name__ == '__main__':
    unittest.main()
