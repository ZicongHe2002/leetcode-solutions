from itertools import combinations, product
import unittest

from python.p0447_number_of_boomerangs import Solution


def every_ordered_triple_oracle(points):
    answer = 0
    for center in range(len(points)):
        for first in range(len(points)):
            if first == center:
                continue
            for second in range(len(points)):
                if second in (center, first):
                    continue
                left = sum((a - b) ** 2 for a, b in zip(points[center], points[first]))
                right = sum((a - b) ** 2 for a, b in zip(points[center], points[second]))
                answer += left == right
    return answer


class OrderedEqualDistanceTests(unittest.TestCase):
    def check(self, points, expected=None):
        before = [point[:] for point in points]
        actual = Solution().numberOfBoomerangs(points)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, every_ordered_triple_oracle(points) if expected is None else expected)
        self.assertEqual(points, before)

    def test_every_subset_of_small_coordinate_grid(self):
        catalog = tuple(product((-1, 0, 1), repeat=2))
        sets = 0
        for size in range(10):
            for points in combinations(catalog, size):
                self.check([list(point) for point in points])
                sets += 1
        self.assertEqual(sets, 512)

    def test_maximum_point_count_coordinate_bounds_and_ordered_pairs(self):
        self.check([[index, 0] for index in range(500)], 124500)
        self.check([[-10000, -10000], [-10000, 10000], [10000, -10000], [10000, 10000]], 8)
        self.check([[0, 0]], 0)
        self.check([[0, 0], [1, 0]], 0)
        self.check([[0, 0], [1, 0], [2, 0]], 2)
        self.check([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]], 20)


if __name__ == '__main__':
    unittest.main()
