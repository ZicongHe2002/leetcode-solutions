from itertools import combinations
import random
import unittest

from python.p0587_erect_the_fence import Solution


def supporting_line_oracle(points):
    if len(points) == 1:
        return {tuple(points[0])}
    boundary = set()
    for x, y in points:
        for a, b in points:
            if (x, y) == (a, b):
                continue
            sides = [(a - x) * (d - y) - (b - y) * (c - x) for c, d in points]
            if all(side >= 0 for side in sides) or all(side <= 0 for side in sides):
                boundary.add((x, y))
                break
    return boundary


class FenceHullTests(unittest.TestCase):
    def check(self, points, expected):
        before = [point[:] for point in points]
        result = Solution().outerTrees(points)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(p) is list and len(p) == 2 and all(type(v) is int for v in p) for p in result))
        self.assertEqual(len(result), len(set(map(tuple, result))))
        self.assertEqual(set(map(tuple, result)), expected)
        self.assertEqual(points, before)

    def test_all_small_grid_subsets_and_seeded_sets_against_supporting_lines(self):
        grid = [(x, y) for x in range(3) for y in range(3)]
        checks = 0
        for size in range(1, 10):
            for subset in combinations(grid, size):
                points = list(map(list, subset[::-1]))
                self.check(points, supporting_line_oracle(points))
                checks += 1
        self.assertEqual(checks, 511)
        rng = random.Random(587)
        population = [(x, y) for x in range(11) for y in range(11)]
        for _ in range(150):
            points = list(map(list, rng.sample(population, rng.randint(1, 25))))
            self.check(points, supporting_line_oracle(points))

    def test_three_thousand_points_collinear_and_coordinate_boundaries(self):
        points = [[x, y] for x in range(50) for y in range(60)]
        boundary = {(x, y) for x, y in points if x in (0, 49) or y in (0, 59)}
        self.assertEqual(len(boundary), 216)
        self.check(points[::-1], boundary)
        line = [[x, 40] for x in range(101)]
        self.check(line, set(map(tuple, line)))
        points = [[0, 0], [0, 100], [100, 0], [100, 100], [0, 50], [50, 0], [50, 100], [100, 50], [50, 50]]
        self.check(points, set(map(tuple, points[:-1])))
        self.check([[1, 1], [2, 2], [2, 0], [2, 4], [3, 3], [4, 2]],
                   {(1, 1), (2, 0), (2, 4), (3, 3), (4, 2)})


if __name__ == '__main__':
    unittest.main()
