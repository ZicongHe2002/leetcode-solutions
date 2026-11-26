import unittest
from functools import lru_cache
from itertools import product

from python.p0188_best_time_to_buy_and_sell_stock_iv import Solution


def enumerate_limited_trades(prices, limit):
    @lru_cache(None)
    def visit(day, holding, remaining):
        if day == len(prices):
            return float('-inf') if holding else 0
        result = visit(day + 1, holding, remaining)
        if remaining and holding:
            result = max(result, prices[day] + visit(day + 1, False, remaining - 1))
        if remaining and not holding:
            result = max(result, -prices[day] + visit(day + 1, True, remaining))
        return result
    return visit(0, False, limit)


class LimitedStockTests(unittest.TestCase):
    def check(self, k, prices, expected=None):
        before = prices[:]
        if expected is None:
            expected = enumerate_limited_trades(tuple(prices), k)
        result = Solution().maxProfit(k, prices)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(prices, before)

    def test_all_small_price_arrays_and_limits_against_actions(self):
        arrays = checks = 0
        for size in range(1, 7):
            for prices in product((0, 1, 3), repeat=size):
                arrays += 1
                for k in range(1, 5):
                    self.check(k, list(prices))
                    checks += 1
        self.assertEqual((arrays, checks), (1092, 4368))

    def test_maximum_days_limit_unlimited_shortcut_and_monotone_prices(self):
        self.check(100, [0, 1000] * 500, 100000)
        self.check(100, [0, 1000] * 100, 100000)
        self.check(1, [0, 1000] * 500, 1000)
        self.check(100, list(range(1000)), 999)
        self.check(100, list(range(1000, 0, -1)), 0)
        self.check(100, [1000], 0)


if __name__ == '__main__':
    unittest.main()
