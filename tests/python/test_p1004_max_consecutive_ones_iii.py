import unittest
from itertools import product

from python.p1004_max_consecutive_ones_iii import Solution


def all_intervals(values, budget):
    return max((end - start for start in range(len(values))
                for end in range(start + 1, len(values) + 1)
                if values[start:end].count(0) <= budget), default=0)


class FlipWindowTests(unittest.TestCase):
    def check(self, values, budget, expected=None):
        before = values[:]
        if expected is None:
            expected = all_intervals(values, budget)
        result = Solution().longestOnes(values, budget)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_binary_arrays_and_budgets_against_all_intervals(self):
        arrays = checks = 0
        for size in range(10):
            for values in product((0, 1), repeat=size):
                arrays += 1
                for budget in range(size + 1):
                    self.check(list(values), budget)
                    checks += 1
        self.assertEqual((arrays, checks), (1023, 9217))

    def test_maximum_lengths_and_flip_budgets(self):
        self.check([1] * 100000, 0, 100000)
        self.check([0] * 100000, 17, 17)
        self.check([0, 1] * 50000, 0, 1)
        self.check([0, 1] * 50000, 25000, 50001)
        self.check([0, 1] * 50000, 50000, 100000)


if __name__ == '__main__':
    unittest.main()
