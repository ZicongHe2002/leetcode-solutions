from itertools import permutations, product
import unittest

from python.p0593_valid_square import Solution


def all_cyclic_orders(points):
    if len(set(map(tuple, points))) != 4:
        return False
    for order in permutations(points):
        edges = [(order[(index + 1) % 4][0] - order[index][0],
                  order[(index + 1) % 4][1] - order[index][1]) for index in range(4)]
        lengths = [dx * dx + dy * dy for dx, dy in edges]
        if (lengths[0] > 0 and all(length == lengths[0] for length in lengths)
                and edges[0][0] * edges[1][0] + edges[0][1] * edges[1][1] == 0):
            return True
    return False


class ValidSquareTests(unittest.TestCase):
    def check(self, points, expected):
        before = [point[:] for point in points]
        result = Solution().validSquare(*points)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, points)
        self.assertEqual(points, before)

    def test_all_ordered_grid_quadruples_including_repeated_points(self):
        grid = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]
        cases = 0
        for values in product(grid, repeat=4):
            points = list(map(list, values))
            self.check(points, all_cyclic_orders(points))
            cases += 1
        self.assertEqual(cases, 6561)

    def test_all_input_orders_degenerate_rhombus_rectangle_and_coordinate_bounds(self):
        cases = (
            ([(0, 0), (1, 1), (1, 0), (0, 1)], True),
            ([(1, 0), (-1, 0), (0, 1), (0, -1)], True),
            ([(0, 0), (2, 1), (4, 0), (2, -1)], False),
            ([(0, 0), (2, 0), (2, 1), (0, 1)], False),
            ([(0, 0), (1, 0), (2, 0), (3, 0)], False),
            ([(0, 0), (1, 0), (1, 1), (1, 0)], False),
            ([(-10000, -10000), (10000, -10000), (10000, 10000), (-10000, 10000)], True),
            ([(10000, 0), (0, 10000), (-10000, 0), (0, -10000)], True),
        )
        for points, expected in cases:
            for order in permutations(points):
                self.check(list(map(list, order)), expected)


if __name__ == '__main__':
    unittest.main()
