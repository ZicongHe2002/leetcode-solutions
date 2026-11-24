import unittest
from itertools import product

from python.p0875_koko_eating_bananas import Solution


def simulated_hours(piles, speed):
    hours = 0
    for pile in piles:
        remaining = pile
        while remaining > 0:
            remaining -= speed
            hours += 1
    return hours


class BananaTests(unittest.TestCase):
    def check(self, piles, h, expected):
        before = piles[:]
        self.assertEqual(Solution().minEatingSpeed(piles, h), expected)
        self.assertEqual(piles, before)

    def test_small_piles_and_all_feasible_deadlines_against_hour_simulation(self):
        arrays = queries = 0
        for size in range(1, 6):
            for piles in product(range(1, 5), repeat=size):
                arrays += 1
                for h in range(size, sum(piles) + 1):
                    expected = next(speed for speed in range(1, max(piles) + 1)
                                    if simulated_hours(piles, speed) <= h)
                    self.check(list(piles), h, expected)
                    queries += 1
        self.assertEqual((arrays, queries), (1364, 10922))

    def test_examples_and_maximum_numeric_contract(self):
        for piles, h, expected in [([3, 6, 7, 11], 8, 4), ([30, 11, 23, 4, 20], 5, 30),
                                   ([30, 11, 23, 4, 20], 6, 23), ([10**9], 1, 10**9),
                                   ([10**9], 10**9, 1)]:
            self.check(piles, h, expected)
        self.check([10**9] * 10000, 10000, 10**9)
        self.check([10**9] * 10000, 10**9, 10000)


if __name__ == '__main__':
    unittest.main()
