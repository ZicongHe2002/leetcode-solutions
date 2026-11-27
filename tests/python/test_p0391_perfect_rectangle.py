from collections import Counter
from itertools import combinations_with_replacement
import unittest

from python.p0391_perfect_rectangle import Solution


def integer_cell_oracle(rectangles):
    if not rectangles:
        return False
    cells = Counter()
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1, x2):
            for y in range(y1, y2):
                cells[x, y] += 1
    left = min(item[0] for item in rectangles)
    bottom = min(item[1] for item in rectangles)
    right = max(item[2] for item in rectangles)
    top = max(item[3] for item in rectangles)
    return all(cells[x, y] == 1 for x in range(left, right) for y in range(bottom, top))


class PerfectRectangleParityTests(unittest.TestCase):
    def check(self, rectangles, expected=None):
        before = [list(item) for item in rectangles]
        actual = Solution().isRectangleCover(rectangles)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, integer_cell_oracle(rectangles) if expected is None else expected)
        self.assertEqual([list(item) for item in rectangles], before)

    def test_all_small_rectangle_multisets_against_unit_cell_coverage(self):
        catalog = [(x1, y1, x2, y2) for x1 in range(3) for x2 in range(x1 + 1, 4)
                   for y1 in range(3) for y2 in range(y1 + 1, 4)]
        self.assertEqual(len(catalog), 36)
        checks = 1
        self.check([])
        for size in range(1, 4):
            for rectangles in combinations_with_replacement(catalog, size):
                self.check(list(rectangles))
                checks += 1
        self.assertEqual(checks, 9139)

    def test_equal_area_hole_overlap_negative_coordinates_and_maximum_count(self):
        self.check([[0, 0, 1, 1], [0, 0, 1, 1], [2, 0, 3, 1]], False)
        self.check([[-2, -2, 0, 1], [0, -2, 2, 1]], True)
        self.check([[0, 0, 0, 1]], False)
        self.check([[1, 0, 0, 1]], False)
        strips = [[-100000 + index * 10, -100000, -100000 + (index + 1) * 10, 100000]
                  for index in range(20000)]
        self.check(strips, True)


if __name__ == '__main__':
    unittest.main()
