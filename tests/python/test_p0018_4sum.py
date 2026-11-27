from itertools import combinations, product
import unittest

from python.p0018_4sum import Solution


def direct_index_combinations(values, target):
    return {tuple(sorted(items)) for items in combinations(values, 4) if sum(items) == target}


class FourSumCombinationOracleTests(unittest.TestCase):
    def check(self, values, target, expected=None):
        before = values[:]
        if expected is None:
            expected = direct_index_combinations(values, target)
        result = Solution().fourSum(values, target)
        self.assertIs(type(result), list)
        for row in result:
            self.assertIs(type(row), list)
            self.assertEqual(len(row), 4)
            self.assertEqual(row, sorted(row))
            self.assertTrue(all(type(value) is int for value in row))
        actual = [tuple(row) for row in result]
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(set(actual), expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_and_targets_against_index_combinations(self):
        arrays = checks = 0
        for size in range(1, 8):
            for values in product((-1, 0, 1), repeat=size):
                arrays += 1
                for target in (-4, -1, 0, 1, 4):
                    self.check(list(values), target)
                    checks += 1
        self.assertEqual((arrays, checks), (3279, 16395))

    def test_maximum_length_duplicate_values_and_wide_intermediate_sums(self):
        self.check([0] * 200, 0, {(0, 0, 0, 0)})
        self.check([0] * 200, 1, set())
        self.check([-10**9] * 100 + [10**9] * 100, 0, {(-10**9, -10**9, 10**9, 10**9)})
        self.check([10**9] * 200, -294967296, set())
        self.check([-10**9] * 200, 10**9, set())
        self.check([1, 0, -1, 0, -2, 2], 0)
        self.check([2, 2, 2, 2, 2], 8, {(2, 2, 2, 2)})


if __name__ == '__main__':
    unittest.main()
