from itertools import combinations
import unittest

from python.p0368_largest_divisible_subset import Solution


def pairwise_divisible(values):
    return all(a % b == 0 or b % a == 0 for a, b in combinations(values, 2))


def exhaustive_maximum_size(values):
    for size in range(len(values), -1, -1):
        if any(pairwise_divisible(candidate) for candidate in combinations(values, size)):
            return size
    raise AssertionError('empty subset is always feasible')


class DivisibleSubsetReconstructionTests(unittest.TestCase):
    def check(self, values, expected_size=None):
        before = values[:]
        result = Solution().largestDivisibleSubset(values)
        self.assertIs(type(result), list)
        self.assertEqual(len(result), len(set(result)))
        self.assertTrue(set(result) <= set(values))
        self.assertTrue(pairwise_divisible(result))
        self.assertEqual(result, sorted(result))
        self.assertEqual(len(result), exhaustive_maximum_size(values) if expected_size is None else expected_size)
        self.assertEqual(values, before)

    def test_all_subsets_of_small_positive_domain_against_all_feasible_subsets(self):
        inputs = 0
        for size in range(13):
            for values in combinations(range(1, 13), size):
                self.check(list(reversed(values)))
                inputs += 1
        self.assertEqual(inputs, 4096)

    def test_maximum_length_value_bound_and_nonunique_optima(self):
        self.check(list(range(1000, 0, -1)), 10)
        self.check([2 * 10**9], 1)
        self.check([2, 3, 5, 7, 11], 1)
        self.check([1, 2, 3], 2)
        self.check([1 << power for power in range(31)], 31)
        self.check([1, 2, 4, 8, 10**9, 2 * 10**9], 6)


if __name__ == '__main__':
    unittest.main()
