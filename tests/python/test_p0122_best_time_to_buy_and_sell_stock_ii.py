import unittest
from functools import lru_cache
from itertools import product

from python.p0122_best_time_to_buy_and_sell_stock_ii import Solution


def all_daily_trades(prices):
    @lru_cache(None)
    def visit(day, holding):
        if day == len(prices):
            return float('-inf') if holding else 0
        result = visit(day + 1, holding)
        if holding:
            result = max(result, prices[day] + visit(day + 1, False))
        else:
            result = max(result, -prices[day] + visit(day + 1, True))
        return result
    return visit(0, False)


class UnlimitedStockTests(unittest.TestCase):
    def check(self, prices, expected=None):
        before = prices[:]
        if expected is None:
            expected = all_daily_trades(tuple(prices))
        result = Solution().maxProfit(prices)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(prices, before)

    def test_all_small_price_arrays_against_daily_actions(self):
        checks = 0
        for size in range(1, 8):
            for prices in product((0, 1, 3), repeat=size):
                self.check(list(prices))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_extreme_swings_flat_and_single_day(self):
        self.check([0, 10000] * 15000, 150000000)
        self.check([10000, 0] * 15000, 149990000)
        self.check([10000] * 30000, 0)
        self.check(list(range(10000, -1, -1)), 0)
        self.check([0], 0)


if __name__ == '__main__':
    unittest.main()
