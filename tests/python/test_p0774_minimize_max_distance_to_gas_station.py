import unittest
from fractions import Fraction
from itertools import accumulate, product

from python.p0774_minimize_max_distance_to_gas_station import Solution


def all_allocations(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in all_allocations(total - first, parts - 1):
            yield (first,) + rest


def exact_allocation_optimum(stations, k):
    gaps = [right - left for left, right in zip(stations, stations[1:])]
    return min(max(Fraction(gap, count + 1) for gap, count in zip(gaps, allocation))
               for allocation in all_allocations(k, len(gaps)))


class GasStationDistanceTests(unittest.TestCase):
    def check(self, stations, k, expected):
        before = stations[:]
        result = Solution().minmaxGasDist(stations, k)
        self.assertIs(type(result), float)
        error = Fraction.from_float(result) - expected
        self.assertGreaterEqual(error, -Fraction(1, 50000000))
        self.assertLessEqual(error, Fraction(3, 25000000))
        self.assertLess(abs(error), Fraction(1, 10**6))
        self.assertEqual(stations, before)

    def test_all_legal_ten_station_gap_pairs_and_small_budgets_against_rational_allocations(self):
        checked = 0
        for first, second in product(range(1, 6), repeat=2):
            stations = [0] + list(accumulate([first, second] + [1] * 7))
            self.assertEqual(len(stations), 10)
            for k in range(1, 5):
                optimum = exact_allocation_optimum(stations, k)
                self.check(stations, k, optimum)
                offset = 10**8 - stations[-1]
                self.check([value + offset for value in stations], k, optimum)
                checked += 2
        self.assertEqual(checked, 200)

    def test_official_examples_maximum_station_budget_coordinate_and_length_bounds(self):
        self.check(list(range(1, 11)), 9, Fraction(1,2))
        self.check([23,24,36,39,46,56,57,65,84,98], 1, Fraction(14))
        self.check(list(range(2000)), 10**6, Fraction(1,501))
        self.check([50025 * index for index in range(2000)], 1, Fraction(50025))
        stations = list(range(9)) + [10**8]
        self.check(stations, 1, Fraction(10**8 - 8, 2))
        self.check(stations, 10**6, Fraction(10**8 - 8, 10**6 + 1))


if __name__ == '__main__':
    unittest.main()
