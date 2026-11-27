import unittest

from python.p0441_arranging_coins import Solution


def consume_complete_rows(coins):
    row = 1
    while coins >= row:
        coins -= row
        row += 1
    return row - 1


class TriangularBudgetSearchTests(unittest.TestCase):
    def check(self, coins, expected):
        result = Solution().arrangeCoins(coins)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_budget_against_literal_row_construction(self):
        for coins in range(1, 10001):
            self.check(coins, consume_complete_rows(coins))

    def test_every_triangular_boundary_and_maximum_budget(self):
        checks = 0
        for rows in range(1, 65536):
            exact = rows * (rows + 1) // 2
            if exact > 1:
                self.check(exact - 1, rows - 1)
                checks += 1
            self.check(exact, rows)
            self.check(exact + 1, rows)
            checks += 2
        self.assertEqual(checks, 196604)
        self.check(2**31 - 1, 65535)
        self.check(2**31 - 2, 65535)


if __name__ == '__main__':
    unittest.main()
