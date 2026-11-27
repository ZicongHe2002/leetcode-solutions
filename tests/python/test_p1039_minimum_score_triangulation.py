from functools import lru_cache
from itertools import product
import unittest

from python.p1039_minimum_score_triangulation import Solution


@lru_cache(None)
def remove_ear_oracle(values):
    if len(values) == 3:
        return values[0] * values[1] * values[2]
    return min(values[index - 1] * values[index] * values[(index + 1) % len(values)]
               + remove_ear_oracle(values[:index] + values[index + 1:])
               for index in range(len(values)))


class PolygonEarClippingOracleTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = remove_ear_oracle(tuple(values))
        result = Solution().minScoreTriangulation(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_polygons_against_ear_removal_search(self):
        checked = 0
        for size in range(3, 7):
            for values in product((1, 2, 3), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 1080)

    def test_maximum_vertices_value_limits_and_single_triangle(self):
        self.check([1] * 50, 48)
        self.check([100] * 50, 48 * 100**3)
        self.check([1, 100, 1], 100)
        self.check([1, 3, 1, 4, 1, 5], 13)
        self.check([3, 7, 4, 5], 144)


if __name__ == '__main__':
    unittest.main()
