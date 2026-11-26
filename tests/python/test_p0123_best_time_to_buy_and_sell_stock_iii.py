import unittest
from functools import lru_cache
from itertools import product

from python.p0123_best_time_to_buy_and_sell_stock_iii import Solution


def all_two_transaction_paths(prices):
    @lru_cache(None)
    def visit(day, holding, remaining):
        if day == len(prices):
            return float('-inf') if holding else 0
        result = visit(day + 1, holding, remaining)
        if remaining:
            if holding:
                result = max(result, prices[day] + visit(day + 1, False, remaining - 1))
            else:
                result = max(result, -prices[day] + visit(day + 1, True, remaining))
        return result
    return visit(0, False, 2)


class TwoStockTradesTests(unittest.TestCase):
    def check(self, prices, expected=None):
        before = prices[:]
        if expected is None:
            expected = all_two_transaction_paths(tuple(prices))
        result = Solution().maxProfit(prices)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(prices, before)

    def test_all_small_price_arrays_against_two_transaction_actions(self):
        checks = 0
        for size in range(1, 8):
            for prices in product((0, 1, 3), repeat=size):
                self.check(list(prices))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_two_extreme_profits_monotone_and_single_day(self):
        self.check([0, 100000] * 50000, 200000)
        self.check(list(range(100000)), 99999)
        self.check(list(range(100000, 0, -1)), 0)
        self.check([3, 3, 5, 0, 0, 3, 1, 4], 6)
        self.check([100000], 0)


if __name__ == '__main__':
    unittest.main()
