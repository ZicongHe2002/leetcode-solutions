from collections import Counter
from functools import lru_cache
from itertools import product
import unittest

from python.p0522_longest_uncommon_subsequence_ii import Solution


@lru_cache(None)
def actual_subsequences(text):
    return {''.join(char for index, char in enumerate(text) if mask & (1 << index))
            for mask in range(1 << len(text))}


def per_entry_membership_oracle(words):
    memberships = Counter()
    for word in words:
        memberships.update(actual_subsequences(word))
    return max((len(text) for text, count in memberships.items() if count == 1), default=-1)


class UncommonWholeCandidateTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        actual = Solution().findLUSlength(words)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, per_entry_membership_oracle(words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_every_short_binary_word_list_against_subsequence_memberships(self):
        vocabulary = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        arrays = 0
        for size in range(2, 5):
            for words in product(vocabulary, repeat=size):
                self.check(list(words))
                arrays += 1
        self.assertEqual((len(vocabulary), arrays), (14, 41356))

    def test_maximum_count_length_duplicates_and_unique_shorter_candidate(self):
        words = ['a' * 8 + chr(ord('a') + index // 26) + chr(ord('a') + index % 26) for index in range(50)]
        self.assertEqual((len(set(words)), set(map(len, words))), (50, {10}))
        self.check(words, 10)
        self.check(['a' * 10] * 50, -1)
        self.check(['a' * 10] * 49 + ['b' * 9], 9)
        self.check(['aaa', 'aaa', 'aa'], -1)
        self.check(['aabbcc', 'aabbcc', 'cb'], 2)
        self.check(['aba', 'cdc', 'eae'], 3)


if __name__ == '__main__':
    unittest.main()
