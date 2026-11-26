import unittest
from functools import lru_cache
from itertools import combinations, combinations_with_replacement

from python.p0846_hand_of_straights import Solution


@lru_cache(None)
def can_partition_all_subsets(cards, group_size):
    if not cards:
        return True
    if len(cards) % group_size:
        return False
    for indices in combinations(range(len(cards)), group_size):
        group = [cards[i] for i in indices]
        if any(group[i] != group[0] + i for i in range(group_size)):
            continue
        selected = set(indices)
        rest = tuple(card for index, card in enumerate(cards) if index not in selected)
        if can_partition_all_subsets(rest, group_size):
            return True
    return False


class StraightHandTests(unittest.TestCase):
    def check(self, hand, group_size, expected=None):
        before = hand[:]
        if expected is None:
            expected = can_partition_all_subsets(tuple(sorted(hand)), group_size)
        result = Solution().isNStraightHand(hand, group_size)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)
        self.assertEqual(hand, before)

    def test_all_small_multisets_and_group_sizes_against_arbitrary_partitions(self):
        hands = checks = 0
        for size in range(1, 9):
            for cards in combinations_with_replacement(range(4), size):
                hands += 1
                for group_size in range(1, size + 1):
                    self.check(list(reversed(cards)), group_size)
                    checks += 1
        self.assertEqual((hands, checks), (494, 3168))

    def test_maximum_lengths_counts_missing_values_and_maximum_card(self):
        self.check(list(range(10000)), 10000, True)
        self.check(list(range(100)) * 100, 100, True)
        self.check([10**9] * 10000, 1, True)
        self.check([0] * 5001 + [1] * 4999, 2, False)
        self.check([0, 2] * 5000, 2, False)
        self.check(list(range(10**9 - 999, 10**9 + 1)) * 10, 1000, True)
        self.check([1, 2, 3, 4, 5], 4, False)


if __name__ == '__main__':
    unittest.main()
