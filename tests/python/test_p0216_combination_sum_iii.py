import unittest
from itertools import combinations

from python.p0216_combination_sum_iii import Solution


class FixedDigitCombinationTests(unittest.TestCase):
    def check(self, count, total, expected=None):
        if expected is None:
            expected = {choice for choice in combinations(range(1, 10), count) if sum(choice) == total}
        result = Solution().combinationSum3(count, total)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(row) is list for row in result))
        observed = [tuple(row) for row in result]
        self.assertEqual(len(observed), len(set(observed)))
        self.assertEqual(set(observed), set(expected))

    def test_all_original_k_n_against_standard_combination_sums(self):
        checks = 0
        for count in range(2, 10):
            for total in range(1, 61):
                self.check(count, total)
                checks += 1
        self.assertEqual(checks, 480)

    def test_extreme_digit_counts_sum_bounds_and_multiple_answers(self):
        self.check(9, 45, [tuple(range(1, 10))])
        self.check(9, 44, [])
        self.check(9, 60, [])
        self.check(2, 3, [(1, 2)])
        self.check(2, 17, [(8, 9)])
        self.check(2, 1, [])
        self.check(3, 9, [(1, 2, 6), (1, 3, 5), (2, 3, 4)])


if __name__ == '__main__':
    unittest.main()
