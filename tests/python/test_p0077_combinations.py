import unittest
from itertools import combinations

from python.p0077_combinations import Solution


class CombinationEnumerationTests(unittest.TestCase):
    def check(self, length, count):
        expected = set(combinations(range(1, length + 1), count))
        result = Solution().combine(length, count)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        observed = [tuple(row) for row in result]
        self.assertEqual(len(observed), len(set(observed)))
        self.assertEqual(set(observed), expected)

    def test_all_small_legal_n_k_against_standard_combinations(self):
        checks = 0
        for length in range(1, 11):
            for count in range(1, length + 1):
                self.check(length, count)
                checks += 1
        self.assertEqual(checks, 55)

    def test_maximum_n_endpoints_and_largest_output(self):
        for count in (1, 2, 10, 20):
            self.check(20, count)


if __name__ == '__main__':
    unittest.main()
