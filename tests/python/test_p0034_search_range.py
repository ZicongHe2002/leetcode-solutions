import unittest
from itertools import combinations_with_replacement

from python.p0034_search_range import Solution


class RangeTests(unittest.TestCase):
    def check(self, values, target, expected):
        before = values[:]
        self.assertEqual(Solution().searchRange(values, target), expected)
        self.assertEqual(values, before)

    def test_all_small_sorted_arrays_against_position_scan(self):
        arrays = queries = 0
        for size in range(9):
            for values in combinations_with_replacement(range(-2, 3), size):
                arrays += 1
                for target in range(-3, 4):
                    matches = [index for index, value in enumerate(values) if value == target]
                    expected = [matches[0], matches[-1]] if matches else [-1, -1]
                    self.check(list(values), target, expected)
                    queries += 1
        self.assertEqual((arrays, queries), (1287, 9009))

    def test_duplicates_endpoints_and_maximum_length(self):
        self.check([5, 7, 7, 8, 8, 10], 8, [3, 4])
        self.check([5, 7, 7, 8, 8, 10], 6, [-1, -1])
        for target, expected in [(-10**9, [0, 1]), (10**9, [3, 4])]:
            self.check([-10**9, -10**9, 0, 10**9, 10**9], target, expected)
        self.check([10**9] * 100000, 10**9, [0, 99999])
        self.check([-10**9] * 100000, 0, [-1, -1])
        values = [index // 10 - 5000 for index in range(100000)]
        for target, expected in [(-5000, [0, 9]), (0, [50000, 50009]), (4999, [99990, 99999])]:
            self.check(values, target, expected)


if __name__ == '__main__':
    unittest.main()
