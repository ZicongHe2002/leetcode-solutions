import unittest
from itertools import combinations

from python.p0757_set_intersection_size_at_least_two import Solution


def all_integer_subsets(intervals):
    return min(mask.bit_count() for mask in range(32)
               if all(sum(bool(mask & (1 << point)) for point in range(start, end + 1)) >= 2
                      for start, end in intervals))


class IntersectionTwoTests(unittest.TestCase):
    def check(self, intervals, expected):
        before = [row[:] for row in intervals]
        result = Solution().intersectionSizeTwo(intervals)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected, intervals[:20])
        self.assertEqual(intervals, before)

    def test_every_small_interval_family_against_all_literal_integer_subsets(self):
        candidates = list(combinations(range(5), 2))
        checked = 0
        for family in range(1, 1 << len(candidates)):
            intervals = [list(interval) for index, interval in enumerate(candidates) if family >> index & 1]
            expected = all_integer_subsets(intervals)
            self.check(intervals, expected)
            self.check(intervals[::-1] + [intervals[0][:]], expected)
            checked += 1
        self.assertEqual(checked, 1023)

    def test_official_examples_equal_right_endpoints_and_maximum_disjoint_count(self):
        self.check([[1,3],[3,7],[8,9]], 5)
        self.check([[1,3],[1,4],[2,5],[3,5]], 3)
        self.check([[1,2],[2,3],[2,4],[4,5]], 5)
        self.check([[0,10**8]] * 3000, 2)
        self.check([[2 * index, 2 * index + 1] for index in range(3000)], 6000)
        self.check([[0,10],[9,10],[2,10],[1,10]], 2)
        self.check([[0,1],[10**8 - 1,10**8]], 4)
        self.check([[1,2],[1,2],[0,2]], 2)


if __name__ == '__main__':
    unittest.main()
