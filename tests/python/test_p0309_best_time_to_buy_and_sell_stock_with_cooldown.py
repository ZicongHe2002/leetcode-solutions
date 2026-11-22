import unittest
from functools import lru_cache
from itertools import product

from python.p0309_best_time_to_buy_and_sell_stock_with_cooldown import Solution


def all_trades_with_blocked_next_day(prices):
    @lru_cache(None)
    def visit(day, holding, blocked):
        if day == len(prices):
            return float('-inf') if holding else 0
        result = visit(day + 1, holding, False)
        if holding:
            result = max(result, prices[day] + visit(day + 1, False, True))
        elif not blocked:
            result = max(result, -prices[day] + visit(day + 1, True, False))
        return result
    return visit(0, False, False)


class CooldownStockTests(unittest.TestCase):
    def check(self, prices, expected=None):
        before = prices[:]
        if expected is None:
            expected = all_trades_with_blocked_next_day(tuple(prices))
        result = Solution().maxProfit(prices)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(prices, before)

    def test_all_small_price_arrays_against_explicit_cooldown_actions(self):
        checks = 0
        for size in range(1, 8):
            for prices in product((0, 1, 3), repeat=size):
                self.check(list(prices))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_days_alternation_three_day_cycles_and_no_profit(self):
        self.check([0, 1000] * 2500, 1250000)
        self.check([0, 1000, 0] * 1666 + [0, 1000], 1667000)
        self.check([0] * 5000, 0)
        self.check([1000 - index // 5 for index in range(5000)], 0)
        self.check([1, 2, 3, 0, 2], 3)
        self.check([1000], 0)


if __name__ == '__main__':
    unittest.main()
