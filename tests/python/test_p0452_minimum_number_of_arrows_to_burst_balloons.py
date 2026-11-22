import unittest
from itertools import combinations, product

from python.p0452_minimum_number_of_arrows_to_burst_balloons import Solution


def minimum_endpoint_cover(points):
    if not points:
        return 0
    endpoints = sorted({coordinate for interval in points for coordinate in interval})
    for count in range(1, len(endpoints) + 1):
        for shots in combinations(endpoints, count):
            if all(any(start <= shot <= end for shot in shots) for start, end in points):
                return count
    raise AssertionError('All interval endpoints must cover every nonempty interval')


class BalloonArrowTests(unittest.TestCase):
    def check(self, points, expected=None):
        before = [interval[:] for interval in points]
        if expected is None:
            expected = minimum_endpoint_cover(points)
        result = Solution().findMinArrowShots(points)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(points, before)

    def test_all_small_interval_sequences_against_endpoint_covers(self):
        possible = list(combinations((-1, 0, 1, 2), 2))
        checks = 0
        for size in range(1, 5):
            for points in product(possible, repeat=size):
                self.check([list(interval) for interval in points])
                checks += 1
        self.assertEqual(checks, 1554)

    def test_maximum_lengths_touching_nested_extreme_endpoints_and_empty_extension(self):
        self.check([[3 * value, 3 * value + 1] for value in range(100000)], 100000)
        self.check([[-2**31, 2**31 - 1] for _ in range(100000)], 1)
        self.check([[-2**31, -1], [-1, 2**31 - 1]], 1)
        self.check([[-5, 5], [-4, 4], [-3, 3]], 1)
        self.check([[1, 2], [2, 3], [3, 4]], 2)
        self.check([], 0)


if __name__ == '__main__':
    unittest.main()
