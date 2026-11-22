import unittest
from itertools import product

from python.p0049_group_anagrams import Solution


def normalized(groups):
    return sorted(tuple(sorted(group)) for group in groups)


def oracle(words):
    groups = {}
    for word in words:
        groups.setdefault(''.join(sorted(word)), []).append(word)
    return list(groups.values())


class GroupAnagramsTests(unittest.TestCase):
    def check_words(self, words, expected):
        before = words[:]
        self.assertEqual(normalized(Solution().groupAnagrams(words)), normalized(expected))
        self.assertEqual(words, before)

    def test_all_small_word_lists_against_sorting_keys(self):
        checked = 0
        for size in range(5):
            for words in product(('', 'a', 'b', 'aa', 'ab', 'ba', 'bb'), repeat=size):
                self.check_words(list(words), oracle(words))
                checked += 1
        self.assertEqual(checked, 2801)

    def test_repeated_empty_words_and_maximum_size(self):
        self.check_words([''] * 10000, [[''] * 10000])
        first, second = 'a' * 100, 'a' * 99 + 'b'
        self.check_words([first] * 5000 + [second] * 5000, [[first] * 5000, [second] * 5000])
        self.check_words(['eat', 'tea', 'eat', 'tan', 'ate', 'nat', 'bat'],
                         [['eat', 'tea', 'eat', 'ate'], ['tan', 'nat'], ['bat']])


if __name__ == '__main__':
    unittest.main()
