from functools import lru_cache
from itertools import product
import unittest

from python.p0521_longest_uncommon_subsequence_i import Solution


@lru_cache(None)
def actual_subsequences(text):
    return {''.join(char for index, char in enumerate(text) if mask & (1 << index))
            for mask in range(1 << len(text))}


def symmetric_difference_oracle(left, right):
    uncommon = actual_subsequences(left) ^ actual_subsequences(right)
    return max(map(len, uncommon), default=-1)


class WholeStringUncommonTests(unittest.TestCase):
    def check(self, left, right, expected=None):
        actual = Solution().findLUSlength(left, right)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, symmetric_difference_oracle(left, right) if expected is None else expected)

    def test_every_short_binary_string_pair_against_subsequence_set_difference(self):
        words = [''.join(chars) for size in range(1, 6) for chars in product('ab', repeat=size)]
        queries = 0
        for left in words:
            for right in words:
                self.check(left, right)
                queries += 1
        self.assertEqual((len(words), queries), (62, 3844))

    def test_maximum_lengths_equal_unequal_prefix_and_repeated_letters(self):
        self.check('a' * 100, 'a' * 100, -1)
        self.check('a' * 99 + 'b', 'a' * 100, 100)
        self.check('a' * 100, 'a' * 99, 100)
        self.check('a' * 99, 'a' * 100, 100)
        self.check('b' * 100, 'a' * 100, 100)
        self.check('aba', 'cdc', 3)
        self.check('aaa', 'aa', 3)
        self.check('aaa', 'aaa', -1)


if __name__ == '__main__':
    unittest.main()
