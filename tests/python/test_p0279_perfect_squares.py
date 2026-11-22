import unittest
from collections import deque
from math import isqrt

from python.p0279_perfect_squares import Solution


def breadth_first_minimum(n):
    if n == 0:
        return 0
    pending, visited = deque([(0, 0)]), {0}
    while pending:
        total, distance = pending.popleft()
        for root in range(1, isqrt(n - total) + 1):
            following = total + root * root
            if following == n:
                return distance + 1
            if following not in visited:
                visited.add(following)
                pending.append((following, distance + 1))


class PerfectSquareTests(unittest.TestCase):
    def check(self, n):
        result = Solution().numSquares(n)
        self.assertIs(type(result), int)
        self.assertEqual(result, breadth_first_minimum(n))

    def test_all_small_values_and_zero_extension_against_breadth_first_paths(self):
        for n in range(201):
            self.check(n)

    def test_maximum_and_greedy_counterexample_boundaries(self):
        for n in [1, 12, 10000, 9999, 9998]:
            self.check(n)


if __name__ == '__main__':
    unittest.main()
