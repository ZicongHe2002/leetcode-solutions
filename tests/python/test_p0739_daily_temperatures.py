import unittest
from itertools import product

from python.p0739_daily_temperatures import Solution


def scan(values):
    answer = []
    for day, temperature in enumerate(values):
        answer.append(next((future - day for future in range(day + 1, len(values))
                            if values[future] > temperature), 0))
    return answer


class TemperatureTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        self.assertEqual(Solution().dailyTemperatures(values), expected)
        self.assertEqual(values, before)

    def test_small_arrays_against_first_warmer_scan(self):
        checked = 0
        for size in range(8):
            for values in product((30, 31, 32, 100), repeat=size):
                self.check(list(values), scan(values))
                checked += 1
        self.assertEqual(checked, 21845)

    def test_equal_values_nearest_day_and_maximum_length(self):
        self.check([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
        self.check([73, 73, 74], [2, 1, 0])
        self.check([100, 30, 100], [0, 1, 0])
        size = 100000
        self.check([70] * size, [0] * size)
        self.check([70] * (size - 1) + [71], list(range(size - 1, -1, -1)))
        values = [100 - day % 71 for day in range(size)]
        expected = []
        for day in range(size):
            next_peak = (day // 71 + 1) * 71
            expected.append(next_peak - day if day % 71 and next_peak < size else 0)
        self.check(values, expected)


if __name__ == '__main__':
    unittest.main()
