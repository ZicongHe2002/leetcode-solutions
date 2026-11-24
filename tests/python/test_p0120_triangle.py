import unittest
from itertools import product

from python.p0120_triangle import Solution


def all_path_sums(triangle):
    best = None
    for steps in product((0, 1), repeat=len(triangle) - 1):
        column = 0
        total = triangle[0][0]
        for row, step in enumerate(steps, 1):
            column += step
            total += triangle[row][column]
        best = total if best is None else min(best, total)
    return best


class TrianglePathTests(unittest.TestCase):
    def check(self, triangle, expected=None):
        before = [row[:] for row in triangle]
        if expected is None:
            expected = all_path_sums(triangle)
        result = Solution().minimumTotal(triangle)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(triangle, before)

    def test_all_small_signed_triangles_against_all_paths(self):
        checks = 0
        for rows in range(1, 5):
            for values in product((-1, 0, 1), repeat=rows * (rows + 1) // 2):
                triangle, offset = [], 0
                for width in range(1, rows + 1):
                    triangle.append(list(values[offset:offset + width]))
                    offset += width
                self.check(triangle)
                checks += 1
        self.assertEqual(checks, 59808)

    def test_maximum_rows_value_limits_and_edge_paths(self):
        self.check([[10000] * width for width in range(1, 201)], 2000000)
        self.check([[-10000] * width for width in range(1, 201)], -2000000)
        self.check([[-10000] + [10000] * (width - 1) for width in range(1, 201)], -2000000)
        self.check([[-10]], -10)
        self.check([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11)


if __name__ == '__main__':
    unittest.main()
