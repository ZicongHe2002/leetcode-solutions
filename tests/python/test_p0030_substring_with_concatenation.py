import unittest
from collections import Counter
from itertools import product

from python.p0030_substring_with_concatenation import Solution


def brute_starts(text, words):
    if not words:
        return []
    width = len(words[0])
    total = width * len(words)
    expected = Counter(words)
    return [start for start in range(len(text) - total + 1)
            if Counter(text[index:index + width]
                       for index in range(start, start + total, width)) == expected]


class ConcatenatedSubstringTests(unittest.TestCase):
    def check(self, text, words, expected=None):
        before = words[:]
        actual = Solution().findSubstring(text, words)
        self.assertEqual(words, before)
        self.assertEqual(len(set(actual)), len(actual))
        self.assertEqual(sorted(actual), brute_starts(text, words)
                         if expected is None else expected)

    def test_all_small_binary_texts_and_word_multisets(self):
        queries = 0
        for width in (1, 2):
            vocabulary = [''.join(chars) for chars in product('ab', repeat=width)]
            for count in range(1, 4):
                for words in product(vocabulary, repeat=count):
                    for size in range(8):
                        for chars in product('ab', repeat=size):
                            self.check(''.join(chars), list(words))
                            queries += 1
        self.assertEqual(queries, 24990)

    def test_examples_overlaps_resets_and_contract_boundaries(self):
        self.check('barfoothefoobarman', ['foo', 'bar'], [0, 9])
        self.check('wordgoodgoodgoodbestword', ['word', 'good', 'best', 'good'], [8])
        self.check('barfoofoobarthefoobarman', ['bar', 'foo', 'the'], [6, 9, 12])
        self.check('aaaaaa', ['aaa'], [0, 1, 2, 3])
        self.check('abxcab', ['ab', 'ca'])
        self.check('a' * 10000, ['a'] * 5000, list(range(5001)))
        self.check('a' * 10000, ['a' * 30] * 333, list(range(11)))
        self.check('a' * 10000, ['a' * 30] * 5000, [])
        self.check('example', [], [])


if __name__ == '__main__':
    unittest.main()
