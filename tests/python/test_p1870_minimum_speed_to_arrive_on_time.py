import unittest
from fractions import Fraction
from itertools import product

from python.p1870_minimum_speed_to_arrive_on_time import Solution


def enumerate_exact_speeds(distances, hundredths):
    if hundredths <= 100 * (len(distances) - 1):
        return -1
    allowed = Fraction(hundredths, 100)
    for speed in range(1, 401):
        elapsed = sum(Fraction(-(-value // speed), 1) for value in distances[:-1])
        elapsed += Fraction(distances[-1], speed)
        if elapsed <= allowed:
            return speed
    raise AssertionError('Small-input oracle range was insufficient')


class OnTimeSpeedTests(unittest.TestCase):
    def check(self, distances, hundredths, expected=None):
        before = distances[:]
        if expected is None:
            expected = enumerate_exact_speeds(distances, hundredths)
        result = Solution().minSpeedOnTime(distances, hundredths / 100)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(distances, before)

    def test_small_distance_arrays_and_decimal_budgets_against_exact_fractions(self):
        arrays = checks = 0
        for size in range(1, 5):
            for distances in product(range(1, 5), repeat=size):
                arrays += 1
                for hundredths in (100, 125, 150, 175, 200, 250, 300, 400, 500, 1000):
                    self.check(list(distances), hundredths)
                    checks += 1
        self.assertEqual((arrays, checks), (340, 3400))

    def test_maximum_lengths_exact_arrival_speed_limit_and_impossibility(self):
        self.check([100000] * 100000, 10000000, 100000)
        self.check([100000] * 100000, 9999999, 101011)
        self.check([1] * 100000, 9999901, 100)
        self.check([1, 100000], 101, 10**7)
        self.check([1, 100000], 100, -1)
        self.check([1, 3, 2], 270, 3)


if __name__ == '__main__':
    unittest.main()
