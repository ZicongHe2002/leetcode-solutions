import unittest
from itertools import product

from python.p0692_top_k_frequent_words import Solution


def pairwise_ranking(words, k):
    frequencies = {word: words.count(word) for word in set(words)}
    ranked = [None] * len(frequencies)
    for word, count in frequencies.items():
        rank = sum(other_count > count or other_count == count and other < word
                   for other, other_count in frequencies.items())
        ranked[rank] = word
    return ranked[:k]


class TopKWordsTests(unittest.TestCase):
    def check(self, words, k, expected=None):
        before = words[:]
        result = Solution().topKFrequent(words, k)
        self.assertIs(type(result), list)
        self.assertTrue(all(type(word) is str for word in result))
        self.assertEqual(result, pairwise_ranking(words, k) if expected is None else expected)
        self.assertEqual(words, before)

    def test_every_small_word_array_and_k_against_pairwise_ranking(self):
        arrays = 0
        for size in range(1, 7):
            for words in product(('a', 'b', 'aa', 'ab'), repeat=size):
                for k in range(1, len(set(words)) + 1):
                    self.check(list(words), k)
                arrays += 1
        self.assertEqual(arrays, 5460)

    def test_five_hundred_words_length_ten_extreme_k_and_frequency_ties(self):
        words = [chr(97 + i // 26) + chr(97 + i % 26) + 'a' * 8 for i in range(500)]
        words.reverse()
        self.check(words, 1, sorted(words)[:1])
        self.check(words, 500, sorted(words))
        self.check(['z' * 10] * 200 + ['a' * 10] * 200 + ['b' * 10] * 100, 3,
                   ['a' * 10, 'z' * 10, 'b' * 10])
        self.check(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2, ['i', 'love'])
        self.check(['b', 'ab', 'aa', 'a'], 4, ['a', 'aa', 'ab', 'b'])


if __name__ == '__main__':
    unittest.main()
