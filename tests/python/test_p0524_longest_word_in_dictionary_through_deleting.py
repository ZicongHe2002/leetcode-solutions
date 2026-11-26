from functools import lru_cache
from itertools import product
import unittest

from python.p0524_longest_word_in_dictionary_through_deleting import Solution


@lru_cache(None)
def actual_subsequences(text):
    return {''.join(char for index, char in enumerate(text) if mask & (1 << index))
            for mask in range(1 << len(text))}


def subset_membership_oracle(source, words):
    feasible = [word for word in words if word in actual_subsequences(source)]
    return min(feasible, key=lambda word: (-len(word), word), default='')


class LongestDictionaryEmbeddingTests(unittest.TestCase):
    def check(self, source, words, expected=None):
        before = words[:]
        actual = Solution().findLongestWord(source, words)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, subset_membership_oracle(source, words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_all_short_sources_and_nonempty_subdictionaries_against_actual_subsequences(self):
        sources = [''.join(chars) for size in range(1, 7) for chars in product('ab', repeat=size)]
        vocabulary = ('a', 'b', 'aa', 'ab', 'ba', 'bb')
        queries = 0
        for source in sources:
            for mask in range(1, 1 << len(vocabulary)):
                words = [word for index, word in enumerate(vocabulary) if mask & (1 << index)]
                self.check(source, words)
                queries += 1
        self.assertEqual((len(sources), queries), (126, 7938))

    def test_maximum_lengths_count_failures_and_lexicographic_tie(self):
        self.check('a' * 1000, ['a' * 999 + 'b'] * 1000, '')
        source = 'ab' * 500
        self.check(source, ['a' * 500, 'b' * 500, source], source)
        self.check('abce', ['abe', 'abc'], 'abc')
        self.check('abce', ['abc', 'abe'], 'abc')
        self.check('abpcplea', ['ale', 'apple', 'monkey', 'plea'], 'apple')
        self.check('ab', ['b', 'a'], 'a')
        self.check('a', ['b'], '')


if __name__ == '__main__':
    unittest.main()
