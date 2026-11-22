import unittest
from itertools import combinations, product

from python.p1011_capacity_to_ship_packages_within_d_days import Solution


def all_contiguous_partitions(values, days):
    best = sum(values)
    for cuts in combinations(range(1, len(values)), days - 1):
        edges = (0, *cuts, len(values))
        capacity = max(sum(values[edges[i]:edges[i + 1]]) for i in range(days))
        best = min(best, capacity)
    return best


class ShippingCapacityTests(unittest.TestCase):
    def check(self, values, days, expected=None):
        before = values[:]
        if expected is None:
            expected = all_contiguous_partitions(values, days)
        result = Solution().shipWithinDays(values, days)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_small_positive_arrays_against_all_contiguous_partitions(self):
        arrays = checks = 0
        for size in range(1, 7):
            for values in product((1, 2, 3), repeat=size):
                arrays += 1
                for days in range(1, size + 1):
                    self.check(list(values), days)
                    checks += 1
        self.assertEqual((arrays, checks), (1092, 6015))

    def test_maximum_lengths_and_capacity_thresholds(self):
        self.check([500] * 50000, 1, 25000000)
        self.check([500] * 50000, 50000, 500)
        self.check([500] * 50000, 10000, 2500)
        self.check([500] * 50000, 49999, 1000)
        self.check([1, 2, 3, 1, 1], 4, 3)


if __name__ == '__main__':
    unittest.main()
