import unittest
from functools import lru_cache
from itertools import product

from python.p0714_best_time_to_buy_and_sell_stock_with_transaction_fee import Solution


def all_daily_actions_charging_on_sale(prices, fee):
    @lru_cache(None)
    def visit(day, holding):
        if day == len(prices):
            return float('-inf') if holding else 0
        result = visit(day + 1, holding)
        if holding:
            result = max(result, prices[day] - fee + visit(day + 1, False))
        else:
            result = max(result, -prices[day] + visit(day + 1, True))
        return result
    return visit(0, False)


class FeeStockTests(unittest.TestCase):
    def check(self, prices, fee, expected=None):
        before = prices[:]
        if expected is None:
            expected = all_daily_actions_charging_on_sale(tuple(prices), fee)
        result = Solution().maxProfit(prices, fee)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(prices, before)

    def test_all_small_positive_prices_and_fees_against_daily_actions(self):
        arrays = checks = 0
        for size in range(1, 8):
            for prices in product((1, 2, 4), repeat=size):
                arrays += 1
                for fee in (0, 1, 2, 3, 10):
                    self.check(list(prices), fee)
                    checks += 1
        self.assertEqual((arrays, checks), (3279, 16395))

    def test_maximum_days_fee_endpoints_extreme_prices_and_combined_holding(self):
        prices = [1, 49999] * 25000
        self.check(prices, 0, 49998 * 25000)
        self.check(prices, 2, 49996 * 25000)
        self.check(prices, 49998, 0)
        self.check([49999] * 50000, 49999, 0)
        self.check([1, 3, 2, 8, 4, 9], 2, 8)
        self.check([1], 0, 0)


if __name__ == '__main__':
    unittest.main()
