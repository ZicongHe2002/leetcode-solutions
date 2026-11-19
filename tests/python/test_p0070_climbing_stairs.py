from math import comb
import unittest

from python.p0070_climbing_stairs import Solution


class ClimbingStairsTests(unittest.TestCase):
    def test_full_domain_matches_independent_combinatorial_count(self):
        for n in range(46):
            expected = sum(comb(n - twos, twos) for twos in range(n // 2 + 1))
            with self.subTest(n=n):
                self.assertEqual(Solution().climbStairs(n), expected)

    def test_examples_and_upper_boundary(self):
        for n, expected in ((1, 1), (2, 2), (3, 3), (5, 8), (45, 1836311903)):
            with self.subTest(n=n):
                self.assertEqual(Solution().climbStairs(n), expected)


if __name__ == "__main__":
    unittest.main()
