from itertools import combinations_with_replacement, product
import unittest

from python.p0223_rectangle_area import Solution


def occupied_cells(rectangle):
    x1, y1, x2, y2 = rectangle
    return {(x, y) for x in range(x1, x2) for y in range(y1, y2)}


class RectangleUnionTests(unittest.TestCase):
    def check(self, first, second, expected):
        result = Solution().computeArea(*first, *second)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(Solution().computeArea(*second, *first), expected)

    def test_all_small_integer_rectangles_against_cell_union(self):
        intervals = list(combinations_with_replacement(range(-2, 3), 2))
        rectangles = [(x1, y1, x2, y2) for (x1, x2), (y1, y2) in product(intervals, repeat=2)]
        self.assertEqual(len(rectangles), 225)
        cells = {rectangle: occupied_cells(rectangle) for rectangle in rectangles}
        for first, second in product(rectangles, repeat=2):
            self.check(first, second, len(cells[first] | cells[second]))

    def test_disjoint_axes_boundary_contact_containment_and_large_coordinates(self):
        self.check((0, 0, 1, 1), (2, 2, 3, 3), 2)
        self.check((0, 0, 1, 1), (1, 0, 2, 1), 2)
        self.check((0, 0, 1, 1), (1, 1, 2, 2), 2)
        self.check((-3, -3, 3, 3), (-1, -1, 1, 1), 36)
        self.check((-10000, -10000, 10000, 10000), (-10000, -10000, 10000, 10000), 400000000)
        self.check((-3, 0, 3, 4), (0, -1, 9, 2), 45)

    def test_zero_width_zero_height_and_point_rectangles(self):
        cases = [
            ((0, 0, 0, 1), (2, 2, 3, 2), 0),
            ((0, 0, 0, 0), (2, 2, 2, 2), 0),
            ((0, 0, 0, 1), (-1, -1, 1, 2), 6),
            ((0, 0, 1, 0), (-1, -1, 2, 1), 6),
            ((4, 0, 4, 2), (-1, -1, 1, 2), 6),
            ((-1, 4, 1, 4), (-1, -1, 1, 2), 6),
            ((1, 1, 1, 1), (0, 0, 2, 2), 4),
            ((0, 0, 0, 2), (-1, 1, 1, 1), 0),
        ]
        for first, second, expected in cases:
            with self.subTest(first=first, second=second):
                self.check(first, second, expected)


if __name__ == '__main__':
    unittest.main()
