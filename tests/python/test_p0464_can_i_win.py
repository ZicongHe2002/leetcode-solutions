import unittest

from python.p0464_can_i_win import Solution


def original_game_tree_oracle(maximum, target):
    choices = tuple(range(1, maximum + 1))
    if target <= 0:
        return True
    if sum(choices) < target:
        return False
    def play(available, total):
        for index, choice in enumerate(available):
            if total + choice >= target:
                return True
            following = available[:index] + available[index + 1:]
            if not play(following, total + choice):
                return True
        return False
    return play(choices, 0)


class UsedChoiceMinimaxTests(unittest.TestCase):
    def test_all_small_choice_ranges_and_targets_against_full_game_tree(self):
        games = 0
        for maximum in range(1, 8):
            for target in range(maximum * (maximum + 1) // 2 + 2):
                actual = Solution().canIWin(maximum, target)
                self.assertIs(type(actual), bool)
                self.assertEqual(actual, original_game_tree_oracle(maximum, target))
                games += 1
        self.assertEqual(games, 98)

    def test_maximum_choices_target_bounds_pair_strategy_and_call_isolation(self):
        solver = Solution()
        for maximum, target, expected in [(20, 0, True), (20, 20, True), (20, 21, False),
                                           (20, 300, False), (20, 210, False),
                                           (10, 11, False), (1, 1, True), (1, 2, False)]:
            self.assertEqual(solver.canIWin(maximum, target), expected)


if __name__ == '__main__':
    unittest.main()
