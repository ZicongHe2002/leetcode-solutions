import unittest
from itertools import product

from python.p0733_flood_fill import Solution


def fixed_point_fill(image, sr, sc, color):
    reached = {(sr, sc)}
    while True:
        expanded = reached | {(r, c) for r in range(len(image)) for c in range(len(image[0]))
                              if image[r][c] == image[sr][sc]
                              and any(abs(r - rr) + abs(c - cc) == 1 for rr, cc in reached)}
        if expanded == reached:
            return [[color if (r, c) in reached else value for c, value in enumerate(row)]
                    for r, row in enumerate(image)]
        reached = expanded


class FloodFillTests(unittest.TestCase):
    def check(self, image, sr, sc, color, expected):
        rows = image[:]
        self.assertIs(Solution().floodFill(image, sr, sc, color), image)
        self.assertEqual(image, expected)
        for actual, original in zip(image, rows):
            self.assertIs(actual, original)

    def test_all_small_images_starts_and_colors_against_fixed_point(self):
        grids = checks = 0
        for height, width in [(1, 1), (1, 3), (2, 2), (2, 3), (3, 2), (3, 3)]:
            for values in product(range(2), repeat=height * width):
                grid = [list(values[r * width:(r + 1) * width]) for r in range(height)]
                grids += 1
                for sr in range(height):
                    for sc in range(width):
                        for color in range(3):
                            self.check([row[:] for row in grid], sr, sc, color,
                                       fixed_point_fill(grid, sr, sc, color))
                            checks += 1
        self.assertEqual((grids, checks), (666, 16398))

    def test_examples_color_bounds_and_maximum_image(self):
        self.check([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2,
                   [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
        self.check([[65535, 0], [0, 65535]], 0, 0, 0, [[0, 0], [0, 65535]])
        self.check([[0, 0]], 0, 1, 0, [[0, 0]])
        self.check([[0] * 50 for _ in range(50)], 49, 49, 65535,
                   [[65535] * 50 for _ in range(50)])


if __name__ == '__main__':
    unittest.main()
