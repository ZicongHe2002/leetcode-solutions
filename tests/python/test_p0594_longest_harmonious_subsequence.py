from itertools import combinations, product
import unittest

from python.p0594_longest_harmonious_subsequence import Solution


def all_subsequences(values):
    best = 0
    for size in range(2, len(values) + 1):
        for indices in combinations(range(len(values)), size):
            chosen = [values[index] for index in indices]
            if max(chosen) - min(chosen) == 1:
                best = max(best, size)
    return best


class HarmoniousSubsequenceTests(unittest.TestCase):
    def check(self, values, expected):
        before = values[:]
        result = Solution().findLHS(values)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_every_index_subset(self):
        cases = 0
        for size in range(9):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values), all_subsequences(values))
                cases += 1
        self.assertEqual(cases, 9841)

    def test_twenty_thousand_elements_exact_difference_and_extreme_values(self):
        self.check([0] * 20000, 0)
        self.check([0] * 19999 + [1], 20000)
        self.check([-10**9] * 10000 + [-10**9 + 1] * 10000, 20000)
        self.check([-10**9, 10**9] * 10000, 0)
        self.check(list(range(-10000, 10000)), 2)
        self.check([10**9, 10**9 - 1], 2)
        self.check([1, 3, 2, 2, 5, 2, 3, 7], 5)
        self.check([1, 1, 1, 1], 0)


if __name__ == '__main__':
    unittest.main()
