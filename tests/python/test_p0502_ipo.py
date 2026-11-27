from itertools import product
import unittest

from python.p0502_ipo import Solution


def feasible_order_oracle(k, initial, profits, capital):
    def choose(mask, wealth, remaining):
        best = wealth
        if remaining:
            for index in range(len(profits)):
                if not mask & (1 << index) and capital[index] <= wealth:
                    best = max(best, choose(mask | (1 << index), wealth + profits[index], remaining - 1))
        return best
    return choose(0, initial, k)


class AvailableProjectProfitTests(unittest.TestCase):
    def check(self, k, w, profits, capital, expected=None):
        before = (profits[:], capital[:])
        actual = Solution().findMaximizedCapital(k, w, profits, capital)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, feasible_order_oracle(k, w, profits, capital) if expected is None else expected)
        self.assertEqual((profits, capital), before)

    def test_every_short_project_list_starting_capital_and_limit_against_feasible_orders(self):
        kinds = tuple(product(range(3), repeat=2))
        arrays = queries = 0
        for size in range(4):
            for projects in product(kinds, repeat=size):
                profits = [profit for required, profit in projects]
                capital = [required for required, profit in projects]
                arrays += 1
                for initial, k in product(range(3), range(5)):
                    self.check(k, initial, profits, capital)
                    queries += 1
        self.assertEqual((arrays, queries), (820, 12300))

    def test_maximum_projects_limit_capital_profit_and_unlocking(self):
        self.check(100000, 1000000000, [10000] * 100000, [1000000000] * 100000, 2000000000)
        self.check(100000, 0, [1] * 100000, [0] * 100000, 100000)
        self.check(3, 0, [1, 2, 100], [0, 1, 3], 103)
        self.check(100000, 0, [10000, 10000], [1, 2], 0)
        self.check(2, 5, [0, 0, 100], [0, 5, 6], 5)
        self.check(1, 0, [1, 10], [0, 0], 10)
        self.check(0, 1000000000, [], [], 1000000000)


if __name__ == '__main__':
    unittest.main()
