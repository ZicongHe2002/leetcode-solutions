from functools import lru_cache
from itertools import product
import unittest

from python.p1209_remove_all_adjacent_duplicates_in_string_ii import Solution


@lru_cache(None)
def all_group_deletion_outcomes(text, k):
    outcomes = set()
    for index in range(len(text) - k + 1):
        group = text[index:index + k]
        if len(set(group)) == 1:
            outcomes.update(all_group_deletion_outcomes(text[:index] + text[index + k:], k))
    return frozenset(outcomes or (text,))


class GroupDeletionTests(unittest.TestCase):
    def check(self, text, k, expected=None):
        result = Solution().removeDuplicates(text, k)
        self.assertIs(type(result), str)
        if expected is None:
            self.assertEqual(all_group_deletion_outcomes(text, k), frozenset((result,)))
        else:
            self.assertEqual(result, expected)

    def test_all_small_texts_and_group_sizes_against_all_rewrite_orders(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('ab', repeat=size):
                for k in (2, 3, 4, 9):
                    self.check(''.join(letters), k)
                    checks += 1
        self.assertEqual(checks, 2040)

    def test_maximum_lengths_group_size_remainders_and_cascades(self):
        self.check('a' * 100000, 10000, '')
        self.check('a' * 99999, 10000, 'a' * 9999)
        self.check('a' * 49999 + 'bb' + 'a' * 49999, 2, '')
        self.check('ab' * 50000, 10000, 'ab' * 50000)
        self.check('deeedbbcccbdaa', 3, 'aa')
        self.check('pbbcggttciiippooaais', 2, 'ps')


if __name__ == '__main__':
    unittest.main()
