from functools import lru_cache
from itertools import product
import unittest

from python.p1140_stone_game_ii import Solution


def explicit_alice_turn_score(piles):
    @lru_cache(None)
    def play(index, limit, alice_turn):
        if index == len(piles):
            return 0
        outcomes, collected = [], 0
        for taken in range(1, min(2 * limit, len(piles) - index) + 1):
            collected += piles[index + taken - 1]
            future = play(index + taken, max(limit, taken), not alice_turn)
            outcomes.append(collected + future if alice_turn else future)
        return max(outcomes) if alice_turn else min(outcomes)

    return play(0, 1, True)


class StoneGameExplicitTurnOracleTests(unittest.TestCase):
    def check(self, piles, expected=None):
        before = piles[:]
        if expected is None:
            expected = explicit_alice_turn_score(tuple(piles))
        result = Solution().stoneGameII(piles)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(piles, before)

    def test_every_small_array_against_absolute_alice_score_search(self):
        checked = 0
        for size in range(1, 8):
            for piles in product((1, 2, 3), repeat=size):
                self.check(list(piles))
                checked += 1
        self.assertEqual(checked, 3279)

    def test_maximum_piles_value_limits_and_changing_m(self):
        self.check([10000] * 100)
        self.check(list(range(1, 101)))
        self.check([10000], 10000)
        self.check([2, 7, 9, 4, 4], 10)
        self.check([1, 2, 3, 4, 5, 100], 104)


if __name__ == '__main__':
    unittest.main()
