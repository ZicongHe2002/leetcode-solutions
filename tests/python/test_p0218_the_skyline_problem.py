from itertools import combinations_with_replacement
import unittest

from python.p0218_the_skyline_problem import Solution


def unit_interval_oracle(buildings):
    if not buildings:
        return []
    answer = []
    previous = 0
    for position in range(min(b[0] for b in buildings), max(b[1] for b in buildings) + 1):
        height = max((height for left, right, height in buildings if left <= position < right), default=0)
        if height != previous:
            answer.append([position, height])
            previous = height
    return answer


class SkylineGroupedEventsTests(unittest.TestCase):
    def check(self, buildings, expected=None):
        before = [building[:] for building in buildings]
        expected = unit_interval_oracle(buildings) if expected is None else expected
        result = Solution().getSkyline(buildings)
        self.assertEqual(result, expected)
        self.assertEqual(buildings, before)
        self.assertTrue(all(result[i - 1][0] < result[i][0] and result[i - 1][1] != result[i][1] for i in range(1, len(result))))
        if result:
            self.assertEqual(result[-1][1], 0)

    def test_all_small_building_multisets_against_unit_interval_heights(self):
        pool = [(left, right, height) for left in range(4) for right in range(left + 1, 4) for height in (1, 2, 3)]
        self.assertEqual(len(pool), 18)
        cases = 0
        for size in range(4):
            for buildings in combinations_with_replacement(pool, size):
                self.check([list(building) for building in buildings])
                cases += 1
        self.assertEqual(cases, 1330)

    def test_shared_boundaries_lazy_expiry_and_maximum_building_count(self):
        self.check([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]])
        self.check([[1, 8, 3], [2, 4, 9], [3, 6, 5], [6, 7, 2]])
        self.check([[2, 5, 3], [0, 2, 3]], [[0, 3], [5, 0]])
        maximum = 2**31 - 1
        self.check([[0, maximum, maximum]] * 10000, [[0, maximum], [maximum, 0]])
        buildings = [[2 * index, 2 * index + 1, 1] for index in range(10000)]
        expected = [[position, height] for index in range(10000) for position, height in ((2 * index, 1), (2 * index + 1, 0))]
        self.check(buildings, expected)


if __name__ == '__main__':
    unittest.main()
