import unittest
from itertools import combinations, permutations, product

from python.p0518_coin_change_ii import Solution


def explicit_count_vectors(coins, amount):
    return sum(sum(count * coin for count, coin in zip(counts, coins)) == amount
               for counts in product(*(range(amount // coin + 1) for coin in coins)))


class CoinCombinationTests(unittest.TestCase):
    def check(self, coins, amount, expected=None):
        before = coins[:]
        if expected is None:
            expected = explicit_count_vectors(coins, amount)
        result = Solution().change(amount, coins)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(coins, before)

    def test_all_small_candidate_subsets_orders_and_amounts_against_count_vectors(self):
        checks = 0
        for size in range(1, 6):
            for values in combinations(range(1, 6), size):
                for order in permutations(values):
                    for amount in range(11):
                        self.check(list(order), amount)
                        checks += 1
        self.assertEqual(checks, 3575)

    def test_maximum_amount_candidate_count_and_empty_extensions(self):
        self.check([1], 5000, 1)
        self.check([5000], 5000, 1)
        self.check([2], 4999, 0)
        self.check([1, 2], 5000, 2501)
        self.check(list(range(4701, 5001)), 5000, 1)
        self.check([], 0, 1)
        self.check([], 7, 0)


if __name__ == '__main__':
    unittest.main()
