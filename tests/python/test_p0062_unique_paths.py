import math
import unittest

from python.p0062_unique_paths import Solution


class UniquePathTests(unittest.TestCase):
    def check(self, rows, columns):
        expected = math.comb(rows + columns - 2, rows - 1)
        self.assertEqual(Solution().uniquePaths(rows, columns), expected)
        return expected

    def test_all_small_dimensions_against_binomial_formula(self):
        checks = 0
        for rows in range(1, 13):
            for columns in range(1, 13):
                self.assertLessEqual(self.check(rows, columns), 2 * 10**9)
                checks += 1
        self.assertEqual(checks, 144)

    def test_maximum_dimension_contract_and_separate_wide_integer_extension(self):
        self.assertEqual(self.check(3, 7), 28)
        self.assertEqual(self.check(100, 1), 1)
        self.assertEqual(self.check(1, 100), 1)
        self.assertLessEqual(self.check(100, 7), 2 * 10**9)
        self.assertLessEqual(self.check(7, 100), 2 * 10**9)
        self.assertGreater(self.check(100, 100), 2 * 10**9)


if __name__ == '__main__':
    unittest.main()
