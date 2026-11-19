from collections import deque
from itertools import combinations_with_replacement
import unittest

from python.p0322_coin_change import Solution


def shortest_coin_path(coins, amount):
    pending = deque([(0, 0)])
    seen = {0}
    while pending:
        subtotal, count = pending.popleft()
        if subtotal == amount:
            return count
        for coin in coins:
            next_sum = subtotal + coin
            if next_sum <= amount and next_sum not in seen:
                seen.add(next_sum)
                pending.append((next_sum, count + 1))
    return -1


class CoinChangeTests(unittest.TestCase):
    def test_small_inputs_match_breadth_first_shortest_path(self):
        cases = 0
        for length in range(1, 4):
            for values in combinations_with_replacement(range(1, 7), length):
                for amount in range(21):
                    coins = list(values)
                    with self.subTest(coins=coins, amount=amount):
                        self.assertEqual(Solution().coinChange(coins, amount), shortest_coin_path(values, amount))
                        self.assertEqual(coins, list(values))
                    cases += 1
        self.assertEqual(cases, 1743)

    def test_boundaries_and_greedy_counterexample(self):
        fixtures = (([1, 3, 4], 6, 2), ([2], 3, -1), ([], 0, 0), ([], 3, -1), ([2147483647], 2, -1), ([1], 10000, 10000))
        for coins, amount, expected in fixtures:
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(Solution().coinChange(coins, amount), expected)


if __name__ == "__main__":
    unittest.main()
