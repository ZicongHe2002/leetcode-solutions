import unittest

from python.p0651_four_keys_keyboard import Solution


def four_literal_keys(limit):
    states = {(0, 0, 0)}
    answers = [0]
    for _ in range(limit):
        following = set()
        for screen, clipboard, selection in states:
            following.add((screen + 1, clipboard, 0))
            following.add((screen, clipboard, screen))
            following.add((screen, selection if selection else clipboard, selection))
            following.add((screen + clipboard, clipboard, 0))
        states = following
        answers.append(max(screen for screen, _, _ in states))
    return answers


def action_graph_frontiers(limit):
    layers = [set() for _ in range(limit + 1)]
    layers[0].add((0, 0))
    answers = []
    for used in range(limit + 1):
        frontier = []
        greatest_clipboard = -1
        for screen, clipboard in sorted(layers[used], reverse=True):
            if clipboard > greatest_clipboard:
                frontier.append((screen, clipboard))
                greatest_clipboard = clipboard
        answers.append(max(screen for screen, _ in frontier))
        for screen, clipboard in frontier:
            if used + 1 <= limit:
                layers[used + 1].add((screen + 1, clipboard))
                layers[used + 1].add((screen + clipboard, clipboard))
            if used + 2 <= limit:
                layers[used + 2].add((screen, screen))
    return answers


class FourKeyKeyboardTests(unittest.TestCase):
    def check(self, budget, expected):
        actual = Solution().maxA(budget)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, expected, budget)

    def test_small_budgets_against_literal_four_key_state_enumeration(self):
        expected = four_literal_keys(12)
        for budget in range(1, 13):
            self.check(budget, expected[budget])

    def test_entire_valid_domain_against_nondominated_action_graph(self):
        expected = action_graph_frontiers(50)
        for budget in range(1, 51):
            self.check(budget, expected[budget])
        self.assertEqual(expected[3], 3)
        self.assertEqual(expected[7], 9)


if __name__ == '__main__':
    unittest.main()
