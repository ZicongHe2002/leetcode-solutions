import unittest
from functools import lru_cache
from itertools import product

from python.p0649_dota2_senate import Solution


def every_optimal_ban(senate):
    size = len(senate)

    @lru_cache(None)
    def winner(active, next_position):
        parties = {senate[index] for index in range(size) if active & (1 << index)}
        if len(parties) == 1:
            return next(iter(parties))
        current = next((next_position + offset) % size for offset in range(size)
                       if active & (1 << ((next_position + offset) % size)))
        party = senate[current]
        for target in range(size):
            if active & (1 << target) and senate[target] != party:
                if winner(active ^ (1 << target), (current + 1) % size) == party:
                    return party
        return 'D' if party == 'R' else 'R'

    return 'Radiant' if winner((1 << size) - 1, 0) == 'R' else 'Dire'


class SenateTests(unittest.TestCase):
    def check(self, senate, expected=None):
        if expected is None:
            expected = every_optimal_ban(senate)
        actual = Solution().predictPartyVictory(senate)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, expected, senate if len(senate) < 12 else None)

    def test_every_small_party_sequence_against_all_optimal_ban_choices(self):
        checked = 0
        for size in range(1, 9):
            for parties in product('RD', repeat=size):
                self.check(''.join(parties))
                checked += 1
        self.assertEqual(checked, 510)

    def test_maximum_lengths_alternation_blocks_and_minority_examples(self):
        self.check('R' * 10000, 'Radiant')
        self.check('D' * 10000, 'Dire')
        self.check('RD' * 5000, 'Radiant')
        self.check('DR' * 5000, 'Dire')
        self.check('R' * 5000 + 'D' * 5000, 'Radiant')
        self.check('D' * 5000 + 'R' * 5000, 'Dire')
        self.check('RD', 'Radiant')
        self.check('RDD', 'Dire')


if __name__ == '__main__':
    unittest.main()
