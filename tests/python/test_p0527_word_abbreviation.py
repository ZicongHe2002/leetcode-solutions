from collections import Counter
from itertools import combinations, product
import unittest

from python.p0527_word_abbreviation import Solution


def conflict_iteration_oracle(words):
    prefixes = [1] * len(words)
    while True:
        forms = []
        for word, prefix in zip(words, prefixes):
            omitted = len(word) - prefix - 1
            candidate = word[:prefix] + str(omitted) + word[-1]
            forms.append(candidate if len(candidate) < len(word) else word)
        counts = Counter(forms)
        conflicting = [index for index, form in enumerate(forms) if counts[form] > 1]
        if not conflicting:
            return forms
        for index in conflicting:
            prefixes[index] += 1


class DistinguishingPrefixAbbreviationTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        actual = Solution().wordsAbbreviation(words)
        self.assertIs(type(actual), list)
        self.assertEqual(actual, conflict_iteration_oracle(words) if expected is None else expected)
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(words, before)

    def test_every_small_distinct_word_subset_against_iterative_conflict_refinement(self):
        vocabulary = [''.join(chars) for size in range(2, 6) for chars in product('ab', repeat=size)]
        count = 0
        for size in range(1, 4):
            for words in combinations(vocabulary, size):
                self.check(list(words))
                count += 1
        self.assertEqual((len(vocabulary), count), (60, 36050))

    def test_maximum_count_length_order_and_multidigit_abbreviations(self):
        words = ['a' * 396 + chr(ord('a') + index // 26) + chr(ord('a') + index % 26) + 'az'
                 for index in range(400)]
        self.assertEqual((len(set(words)), set(map(len, words))), (400, {400}))
        self.check(words, words)
        self.check(words[::-1], words[::-1])
        self.check(['like', 'god', 'internal', 'me', 'internet', 'interval', 'intension', 'face', 'intrusion'],
                   ['l2e', 'god', 'internal', 'me', 'i6t', 'interval', 'inte4n', 'f2e', 'intr4n'])
        self.check(['aa', 'aaa'], ['aa', 'aaa'])
        self.check(['ab' + 'c' * 397 + 'd'], ['a398d'])
        self.check(['abcdef', 'abndef'], ['abc2f', 'abn2f'])
        self.check(['abndef', 'abcdef'], ['abn2f', 'abc2f'])


if __name__ == '__main__':
    unittest.main()
