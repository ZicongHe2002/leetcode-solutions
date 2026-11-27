import unittest
from fractions import Fraction
from functools import lru_cache
from itertools import combinations_with_replacement, permutations

from python.p0679_24_game import Solution


@lru_cache(None)
def parenthesized_values(order):
    if len(order) == 1:
        return frozenset((Fraction(order[0]),))
    results = set()
    for split in range(1, len(order)):
        for left in parenthesized_values(order[:split]):
            for right in parenthesized_values(order[split:]):
                results.update((left + right, left - right, left * right))
                if right:
                    results.add(left / right)
    return frozenset(results)


def all_orders_and_parentheses(cards):
    return any(Fraction(24) in parenthesized_values(order) for order in set(permutations(cards)))


class TwentyFourGameTests(unittest.TestCase):
    def check(self, cards, expected=None):
        before = cards[:]
        if expected is None:
            expected = all_orders_and_parentheses(cards)
        result = Solution().judgePoint24(cards)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, cards)
        self.assertEqual(cards, before)

    def test_all_legal_card_multisets_against_ordered_parenthesis_enumeration(self):
        checked = 0
        for cards in combinations_with_replacement(range(1, 10), 4):
            self.check(list(cards))
            checked += 1
        self.assertEqual(checked, 495)

    def test_fractional_solution_repeated_cards_and_input_order(self):
        self.assertEqual(Fraction(8) / (3 - Fraction(8, 3)), 24)
        for cards in set(permutations((3, 3, 8, 8))):
            self.check(list(cards), True)
        self.check([4, 1, 8, 7], True)
        self.check([1, 2, 1, 2], False)
        self.check([1, 1, 1, 1], False)
        parenthesized_values.cache_clear()


if __name__ == '__main__':
    unittest.main()
