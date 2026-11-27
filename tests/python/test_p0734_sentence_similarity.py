import unittest
from itertools import combinations, product

from python.p0734_sentence_similarity import Solution


def direct_pair_scan(left, right, pairs):
    if len(left) != len(right):
        return False
    return all(a == b or any((a == x and b == y) or (a == y and b == x) for x, y in pairs)
               for a, b in zip(left, right))


class SentenceSimilarityTests(unittest.TestCase):
    def check(self, left, right, pairs, expected=None):
        before = (left[:], right[:], [pair[:] for pair in pairs])
        result = Solution().areSentencesSimilar(left, right, pairs)
        self.assertIs(type(result), bool)
        self.assertEqual(result, direct_pair_scan(left, right, pairs) if expected is None else expected,
                         (left[:5], right[:5], pairs[:5]))
        self.assertEqual((left, right, pairs), before)

    def test_all_small_direct_relations_and_sentence_pairs_without_transitive_closure(self):
        edges = list(combinations('abc', 2))
        sentences = [list(chars) for size in range(1, 4) for chars in product('abc', repeat=size)]
        checked = 0
        for mask in range(8):
            pairs = [list(edge[::-1] if mask & 1 else edge) for index, edge in enumerate(edges) if mask >> index & 1]
            for left, right in product(sentences, repeat=2):
                self.check(left, right, pairs)
                checked += 1
        self.assertEqual(checked, 12168)

    def test_examples_case_sensitivity_reflexivity_and_maximum_word_pair_lengths(self):
        self.check(['great','acting','skills'], ['fine','drama','talent'],
                   [['great','fine'],['drama','acting'],['skills','talent']], True)
        self.check(['a'], ['c'], [['a','b'],['b','c']], False)
        self.check(['Word'], ['word'], [], False)
        self.check(['great'], ['great'], [], True)
        self.check(['great'], ['doubleplus','good'], [['great','doubleplus']], False)
        suffixes = [''.join(chr(97 + digit) for digit in (i // 676, i // 26 % 26, i % 26)) for i in range(1000)]
        left, right = ['a' * 17 + s for s in suffixes], ['b' * 17 + s for s in suffixes]
        pairs = [[b, a] for a, b in zip(left, right)]
        self.assertEqual((len(left), len(pairs), {len(word) for word in left + right}), (1000, 1000, {20}))
        self.check(left, right, pairs, True)
        self.check(left, left[:], [], True)
        self.check(left, right[:-1] + ['c' * 20], pairs, False)


if __name__ == '__main__':
    unittest.main()
