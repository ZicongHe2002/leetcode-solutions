import unittest
from itertools import combinations

from python.p1802_maximum_value_at_given_index_bounded_array import Solution


def all_legal_positive_arrays(length, budget):
    maxima = [1] * length
    for total in range(length, budget + 1):
        for cuts in combinations(range(1, total), length - 1):
            edges = (0, *cuts, total)
            values = [edges[i + 1] - edges[i] for i in range(length)]
            if all(abs(values[i + 1] - values[i]) <= 1 for i in range(length - 1)):
                maxima = [max(previous, value) for previous, value in zip(maxima, values)]
    return maxima


class BoundedPeakTests(unittest.TestCase):
    def check(self, length, index, budget, expected):
        result = Solution().maxValue(length, index, budget)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_lengths_budgets_indices_against_positive_compositions(self):
        checks = 0
        for length in range(1, 7):
            for budget in range(length, 13):
                expected = all_legal_positive_arrays(length, budget)
                for index, value in enumerate(expected):
                    self.check(length, index, budget, value)
                    checks += 1
        self.assertEqual(checks, 182)

    def test_maximum_scalar_bounds_and_decreasing_sides(self):
        self.check(10**9, 10**9 - 1, 10**9, 1)
        self.check(1, 0, 10**9, 10**9)
        self.check(2, 0, 10**9, 500000000)
        self.check(5, 2, 14, 4)
        self.check(4, 2, 6, 2)
        self.check(6, 1, 10, 3)


if __name__ == '__main__':
    unittest.main()
