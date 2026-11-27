from itertools import product
import unittest

from python.p0860_lemonade_change import Solution


def every_cash_state(bills):
    states = {(0, 0, 0)}
    for bill in bills:
        change = bill - 5
        following = set()
        for fives, tens, twenties in states:
            for give5 in range(min(fives, change // 5) + 1):
                for give10 in range(min(tens, change // 10) + 1):
                    for give20 in range(min(twenties, change // 20) + 1):
                        if 5 * give5 + 10 * give10 + 20 * give20 == change:
                            following.add((fives - give5 + (bill == 5),
                                           tens - give10 + (bill == 10),
                                           twenties - give20 + (bill == 20)))
        states = following
        if not states:
            return False
    return True


class LemonadeCashStateTests(unittest.TestCase):
    def check(self, bills, expected=None):
        before = bills[:]
        if expected is None:
            expected = every_cash_state(bills)
        result = Solution().lemonadeChange(bills)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(bills, before)

    def test_every_small_bill_sequence_against_all_exact_change_states(self):
        checks = 0
        for size in range(1, 9):
            for bills in product((5, 10, 20), repeat=size):
                self.check(list(bills))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_success_patterns_and_unrecoverable_prefix(self):
        self.check([5] * 100000, True)
        self.check([5, 10] * 50000, True)
        self.check([5, 5, 5, 20] * 25000, True)
        self.check([5, 5, 20] + [5] * 99997, False)
        self.check([20] * 100000, False)


if __name__ == '__main__':
    unittest.main()
