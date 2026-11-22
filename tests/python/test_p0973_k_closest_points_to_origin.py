import unittest
from collections import Counter
from itertools import product

from python.p0973_k_closest_points_to_origin import Solution


class ClosestPointTests(unittest.TestCase):
    def check(self, points, k):
        before = [point[:] for point in points]
        result = Solution().kClosest(points, k)
        self.assertEqual(len(result), k)
        self.assertTrue(all(type(point) is list and len(point) == 2 for point in result))
        self.assertTrue(all(type(value) is int for point in result for value in point))
        self.assertFalse(Counter(map(tuple, result)) - Counter(map(tuple, points)))
        expected = sorted(x * x + y * y for x, y in points)[:k]
        self.assertEqual(sorted(x * x + y * y for x, y in result), expected)
        self.assertEqual(points, before)
        result[0][0] += 1
        self.assertEqual(points, before)

    def test_all_small_point_sequences_and_ranks_including_tied_boundary_extensions(self):
        possible = ((0, 0), (1, 0), (0, 1), (-1, 0), (1, 1))
        arrays = checks = 0
        for size in range(1, 6):
            for points in product(possible, repeat=size):
                arrays += 1
                for k in range(1, size + 1):
                    self.check([list(point) for point in points], k)
                    checks += 1
        self.assertEqual((arrays, checks), (3905, 18555))

    def test_maximum_lengths_coordinates_duplicate_points_and_rank_endpoints(self):
        self.check([[10000, -10000] for _ in range(10000)], 10000)
        axis = [[value, 0] for value in range(-5000, 5000)]
        self.check(axis, 1)
        self.check(axis, 9999)
        self.check([[0, 0], [-10000, -10000], [10000, 10000]], 1)
        self.check([[0, 0], [0, 0], [1, 1]], 2)


if __name__ == '__main__':
    unittest.main()
