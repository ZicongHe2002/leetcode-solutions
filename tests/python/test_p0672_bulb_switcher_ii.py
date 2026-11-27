import unittest

from python.p0672_bulb_switcher_ii import Solution


def exact_step_counts(n, maximum):
    predicates = (lambda i: True, lambda i: i % 2 == 0,
                  lambda i: i % 2 == 1, lambda i: (i - 1) % 3 == 0)
    buttons = [sum(1 << (i - 1) for i in range(1, n + 1) if predicate(i))
               for predicate in predicates]
    states = {(1 << n) - 1}
    counts = [1]
    for _ in range(maximum):
        states = {state ^ button for state in states for button in buttons}
        counts.append(len(states))
    return counts


class BulbSwitcherIITests(unittest.TestCase):
    def check_counts(self, n, maximum):
        counts = exact_step_counts(n, maximum)
        for presses, expected in enumerate(counts):
            result = Solution().flipLights(n, presses)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected, (n, presses))

    def test_small_full_bulb_states_after_each_exact_step(self):
        for n in range(1, 21):
            self.check_counts(n, 20)

    def test_one_thousand_presses_and_full_one_thousand_bulbs(self):
        for n in (1, 2, 3, 6, 7, 1000):
            self.check_counts(n, 1000)
        self.assertEqual([Solution().flipLights(n, 1) for n in (1, 2, 3)], [2, 3, 4])
        self.assertEqual(Solution().flipLights(1000, 0), 1)


if __name__ == '__main__':
    unittest.main()
