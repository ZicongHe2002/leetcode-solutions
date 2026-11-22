from functools import lru_cache
from itertools import product
import unittest

from python.p1048_longest_string_chain import Solution


def is_direct_predecessor(shorter, longer):
    if len(longer) != len(shorter) + 1:
        return False
    matched = 0
    for character in longer:
        if matched < len(shorter) and shorter[matched] == character:
            matched += 1
    return matched == len(shorter)


def direct_word_relation_longest_path(words):
    @lru_cache(None)
    def from_index(index):
        return 1 + max((from_index(other) for other in range(len(words))
                        if is_direct_predecessor(words[index], words[other])), default=0)

    return max(from_index(index) for index in range(len(words)))


class StringChainDirectRelationTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        if expected is None:
            expected = direct_word_relation_longest_path(words)
        result = Solution().longestStrChain(words)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(words, before)

    def test_all_nonempty_small_word_sets_against_direct_pair_relation(self):
        universe = [''.join(letters) for length in range(1, 4)
                    for letters in product('ab', repeat=length)]
        checked = 0
        for mask in range(1, 1 << len(universe)):
            words = [word for index, word in enumerate(universe) if mask & (1 << index)]
            self.check(list(reversed(words)))
            checked += 1
        self.assertEqual((len(universe), checked), (14, 16383))

    def test_maximum_word_count_length_and_duplicate_words(self):
        words = ['a' * length for length in range(1, 17)]
        for index in range(984):
            prefix = ''.join(chr(97 + value) for value in
                             (index // 676, (index // 26) % 26, index % 26))
            words.append(prefix + 'z' * 13)
        self.assertEqual((len(words), len(set(words)), max(map(len, words))), (1000, 1000, 16))
        self.check(list(reversed(words)), 16)
        self.check(['a', 'a', 'ab', 'ab', 'abc'], 3)
        self.check(['abc', 'def'], 1)
        self.check(['z'], 1)
        self.check(['a', 'b', 'ba', 'bca', 'bda', 'bdca'], 4)


if __name__ == '__main__':
    unittest.main()
