import unittest
from itertools import product

from python.p0656_coin_path import Solution


def all_legal_paths(coins, jump):
    candidates = []

    def visit(index, path, cost):
        if coins[index] == -1:
            return
        path = path + [index + 1]
        cost += coins[index]
        if index == len(coins) - 1:
            candidates.append((cost, path))
        else:
            for target in range(index + 1, min(len(coins), index + jump + 1)):
                visit(target, path, cost)

    visit(0, [], 0)
    return min(candidates)[1] if candidates else []


class CoinPathTests(unittest.TestCase):
    def check(self, coins, jump, expected=None):
        before = coins[:]
        if expected is None:
            expected = all_legal_paths(coins, jump)
        actual = Solution().cheapestJump(coins, jump)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(index) is int for index in actual))
        self.assertEqual(actual, expected)
        self.assertEqual(coins, before)

    def test_all_small_legal_arrays_and_jump_limits_against_all_paths(self):
        arrays = queries = 0
        for length in range(1, 8):
            for first in (0, 2):
                for tail in product((-1, 0, 2), repeat=length - 1):
                    coins = [first, *tail]
                    arrays += 1
                    for jump in range(1, length + 1):
                        self.check(coins, jump)
                        queries += 1
        self.assertEqual((arrays, queries), (2186, 14216))

    def test_maximum_length_zero_cost_ties_and_blocked_boundaries(self):
        self.check([0] * 1000, 100, list(range(1, 1001)))
        self.check([1] * 1000, 100, [1] + list(range(100, 1001, 100)))
        self.check([100] * 1000, 1, list(range(1, 1001)))
        self.check([0] + [-1] * 998 + [0], 100, [])
        self.check([0] + [-1] * 99 + [0], 100, [1, 101])
        self.check([0] + [-1] * 99 + [0], 99, [])
        self.check([0, -1], 100, [])
        self.check([1, 2, 4, -1, 2], 2, [1, 3, 5])


if __name__ == '__main__':
    unittest.main()
