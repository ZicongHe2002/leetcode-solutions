import unittest
from itertools import permutations, product

from python.p0047_permutations_ii import Solution


class UniquePermutationTests(unittest.TestCase):
    def check(self, values):
        before = values[:]
        expected = set(permutations(values))
        result = Solution().permuteUnique(values)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        observed = [tuple(row) for row in result]
        self.assertEqual(len(observed), len(set(observed)))
        self.assertEqual(set(observed), expected)
        self.assertEqual(values, before)

    def test_all_small_signed_arrays_against_position_permutations(self):
        checks = 0
        for size in range(7):
            for values in product((-1, 0, 1), repeat=size):
                self.check(list(values))
                checks += 1
        self.assertEqual(checks, 1093)

    def test_maximum_length_unique_values_identical_values_and_signed_bounds(self):
        self.check(list(range(-4, 4)))
        self.check([-10] * 8)
        self.check([-10, 10] * 4)
        self.check([1, 1, 2])


if __name__ == '__main__':
    unittest.main()
