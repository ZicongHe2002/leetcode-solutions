import unittest
from itertools import product

from python.p0128_longest_consecutive_sequence import Solution


class SolutionTests(unittest.TestCase):
    def check(self, values, expected, *args):
        before = values[:]
        actual = Solution().longestConsecutive(values, *args)
        self.assertEqual(actual, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_sorted_runs(self):
        checked = 0
        for size in range(7):
            for values in product(range(-2, 3), repeat=size):
                previous, current, best = None, 0, 0
                for value in sorted(values):
                    if previous is not None and value == previous:
                        continue
                    current = current + 1 if previous is not None and value == previous + 1 else 1
                    best = max(best, current)
                    previous = value
                self.check(list(values), best)
                checked += 1
        self.assertEqual(checked, 19531)

    def test_length_value_boundaries_and_duplicates(self):
        self.check(list(range(-50000, 50000)), 100000)
        self.check([7] * 100000, 1)
        self.check([-10**9, 10**9], 1)
        self.check([100, 4, 200, 1, 3, 2, 2], 4)

if __name__ == '__main__':
    unittest.main()
