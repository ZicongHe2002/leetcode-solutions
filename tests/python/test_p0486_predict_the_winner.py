from functools import lru_cache
from itertools import product
import unittest

from python.p0486_predict_the_winner import Solution


def first_player_absolute_score(values):
    @lru_cache(None)
    def play(left, right, first_turn):
        if left > right:
            return 0
        if first_turn:
            return max(values[left] + play(left + 1, right, False),
                       values[right] + play(left, right - 1, False))
        return min(play(left + 1, right, True), play(left, right - 1, True))

    return play(0, len(values) - 1, True)


class WinnerAbsoluteScoreOracleTests(unittest.TestCase):
    def check(self, values, expected=None):
        before = values[:]
        if expected is None:
            expected = 2 * first_player_absolute_score(tuple(values)) >= sum(values)
        result = Solution().predictTheWinner(values)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(values, before)

    def test_all_small_arrays_against_explicit_turn_absolute_score(self):
        checked = 0
        for size in range(1, 9):
            for values in product((0, 1, 2), repeat=size):
                self.check(list(values))
                checked += 1
        self.assertEqual(checked, 9840)

    def test_maximum_length_value_limits_ties_and_losing_positions(self):
        self.check([0] * 20, True)
        self.check([10**7] * 20, True)
        self.check([0, 10**7, 0], False)
        self.check([10**7], True)
        self.check([1, 5, 2], False)
        self.check([1, 5, 233, 7], True)


if __name__ == '__main__':
    unittest.main()
