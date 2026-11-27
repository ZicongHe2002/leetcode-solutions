import string
import unittest
from itertools import combinations, product

from python.p0720_longest_word_in_dictionary import Solution


def every_prefix_in_original(words):
    valid = [word for word in words if all(word[:end] in words for end in range(1, len(word) + 1))]
    return min(valid, key=lambda word: (-len(word), word), default='')


class LongestDictionaryWordTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        result = Solution().longestWord(words)
        self.assertIs(type(result), str)
        self.assertEqual(result, every_prefix_in_original(words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_every_small_nonempty_dictionary_against_all_literal_prefixes(self):
        pool = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        checked = 0
        for size in range(1, len(pool) + 1):
            for words in combinations(pool, size):
                self.check(list(reversed(words)))
                checked += 1
        self.assertEqual(checked, 16383)

    def test_thousand_words_length_thirty_missing_prefixes_ties_and_duplicates(self):
        words = [letter * size for letter in string.ascii_lowercase for size in range(1, 31)]
        words += ['zz' + chr(97 + i // 26) + chr(97 + i % 26) + 'q' * 26 for i in range(220)]
        self.assertEqual(len(words), 1000)
        self.assertTrue(all(1 <= len(word) <= 30 for word in words))
        self.check(list(reversed(words)), 'a' * 30)
        self.check(['a', 'banana', 'app', 'appl', 'ap', 'apply', 'apple'], 'apple')
        self.check(['a', 'app', 'appl', 'apple'], 'a')
        self.check(['ab', 'abc'], '')
        self.check(['w', 'wo', 'wor', 'worl', 'world'], 'world')
        self.check(['a', 'a', 'ab', 'ab', 'abc'], 'abc')


if __name__ == '__main__':
    unittest.main()
