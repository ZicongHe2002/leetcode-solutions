from itertools import combinations
import unittest

from python.p1584_min_cost_to_connect_all_points import Solution


def explicit_edges_kruskal_reference(points):
    edges = sorted((abs(points[left][0] - points[right][0]) + abs(points[left][1] - points[right][1]),
                    left, right) for left, right in combinations(range(len(points)), 2))
    parent = list(range(len(points)))

    def root(node):
        while parent[node] != node:
            node = parent[node]
        return node

    total = 0
    for weight, left, right in edges:
        left, right = root(left), root(right)
        if left != right:
            parent[left] = right
            total += weight
    return total


class DenseManhattanPrimTests(unittest.TestCase):
    def check(self, points, expected=None):
        before = [point[:] for point in points]
        if expected is None:
            expected = explicit_edges_kruskal_reference(points)
        result = Solution().minCostConnectPoints(points)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(points, before)

    def test_every_small_distinct_grid_point_subset_against_kruskal(self):
        universe = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
        checks = 0
        for size in range(1, 7):
            for points in combinations(universe, size):
                self.check([list(point) for point in points])
                checks += 1
        self.assertEqual(checks, 465)

    def test_maximum_point_counts_coordinate_extremes_and_known_geometry(self):
        self.check([[value, 0] for value in range(1000)], 999)
        self.check([[value, value] for value in range(1000)], 1998)
        self.check([[value, 0] for value in range(-1000000, 1000000, 2000)], 1998000)
        self.check([[-1000000, -1000000], [1000000, 1000000]], 4000000)
        self.check([[-1000000, -1000000], [-1000000, 1000000],
                    [1000000, -1000000], [1000000, 1000000]], 6000000)
        self.check([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20)


if __name__ == '__main__':
    unittest.main()
