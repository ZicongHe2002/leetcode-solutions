from itertools import combinations_with_replacement
import unittest

from python.p0475_heaters import Solution


def all_heater_distances(houses, heaters):
    return max((min(abs(house - heater) for heater in heaters) for house in houses), default=0)


class NearestHeaterRadiusTests(unittest.TestCase):
    def check(self, houses, heaters, expected=None):
        before = (houses[:], heaters[:])
        actual = Solution().findRadius(houses, heaters)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_heater_distances(houses, heaters) if expected is None else expected)
        self.assertEqual((houses, heaters), before)

    def test_every_small_position_multiset_against_all_distances(self):
        house_sets = [values for size in range(5) for values in combinations_with_replacement(range(1, 5), size)]
        heater_sets = [values for size in range(1, 4) for values in combinations_with_replacement(range(1, 5), size)]
        pairs = 0
        for houses in house_sets:
            for heaters in heater_sets:
                self.check(list(houses)[::(-1 if pairs % 2 else 1)], list(heaters)[::(-1 if pairs % 3 else 1)])
                pairs += 1
        self.assertEqual((len(house_sets), len(heater_sets), pairs), (70, 34, 2380))

    def test_maximum_counts_extreme_positions_duplicates_and_gap_midpoints(self):
        self.check(list(range(1, 30001)), [1], 29999)
        self.check(list(range(30000, 0, -1)), list(range(1, 30001)), 0)
        self.check([10**9] * 30000, [1] * 30000, 10**9 - 1)
        self.check([500000000, 500000001], [1, 10**9], 499999999)
        self.check([1, 2, 3], [2], 1)
        self.check([1, 5], [2], 3)
        self.check([1, 1], [1, 1], 0)
        self.check([1, 10**9], [1, 10**9], 0)


if __name__ == '__main__':
    unittest.main()
