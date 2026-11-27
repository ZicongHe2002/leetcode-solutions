from itertools import combinations, product
import unittest

from python.p0149_max_points_on_a_line import Solution


def cross_product_oracle(points):
    if len(points) < 2:
        return len(points)
    return max(sum((x - ax) * (by - ay) == (y - ay) * (bx - ax) for x, y in points)
               for (ax, ay), (bx, by) in combinations(points, 2))


class ExactLineDirectionTests(unittest.TestCase):
    def check(self, points, expected=None):
        before = [point[:] for point in points]
        expected = cross_product_oracle(points) if expected is None else expected
        result = Solution().maxPoints(points)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(points, before)

    def test_all_small_grid_subsets_against_integer_cross_products(self):
        grid = list(product((-1, 0, 1), repeat=2))
        for mask in range(1 << len(grid)):
            self.check([list(point) for index, point in enumerate(grid) if mask & (1 << index)])

    def test_opposite_directions_nearby_slopes_and_maximum_size(self):
        self.check([[0, 0], [-2, -2], [2, 2], [1, 0]], 3)
        self.check([[0, 0], [9999, 10000], [9998, 9999]], 2)
        self.check([[0, -10000], [0, 0], [0, 10000]], 3)
        self.check([[x, 2 * x + 3] for x in range(300)], 300)
        self.check([[x, 2 * x + 3] for x in range(150)] + [[x, -2 * x - 3] for x in range(150, 300)], 150)


if __name__ == '__main__':
    unittest.main()
