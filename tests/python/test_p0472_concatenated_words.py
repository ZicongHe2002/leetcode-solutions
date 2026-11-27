from itertools import product
import unittest

from python.p0472_concatenated_words import Solution


def cut_mask_oracle(words):
    dictionary = set(words)
    result = []
    for word in words:
        for mask in range(1, 1 << (len(word) - 1)):
            cuts = [0] + [index for index in range(1, len(word)) if mask & (1 << (index - 1))] + [len(word)]
            if all(word[left:right] in dictionary for left, right in zip(cuts, cuts[1:])):
                result.append(word)
                break
    return result


def fixed_width_word(number):
    chars = ['a'] * 10
    for index in range(9, -1, -1):
        number, digit = divmod(number, 26)
        chars[index] = chr(ord('a') + digit)
    return ''.join(chars)


class ConcatenatedWordCountTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        self.assertEqual(Solution().findAllConcatenatedWordsInADict(words),
                         cut_mask_oracle(words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_every_dictionary_from_short_binary_words_against_all_cuts(self):
        vocabulary = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        dictionaries = 0
        for mask in range(1 << len(vocabulary)):
            self.check([word for index, word in enumerate(vocabulary) if mask & (1 << index)])
            dictionaries += 1
        self.assertEqual(dictionaries, 16384)

    def test_word_count_total_length_maximum_word_length_and_order(self):
        words = [fixed_width_word(number) for number in range(10000)]
        self.assertEqual(len(set(words)), 10000)
        self.assertEqual(sum(map(len, words)), 100000)
        self.check(words, [])
        words = ['a' * size for size in range(1, 31)]
        self.check(words, words[1:])
        self.check(words[::-1], words[:0:-1])
        self.check(['cat', 'cats', 'dog', 'catsdog', 'catsdogcats', 'rat'], ['catsdog', 'catsdogcats'])
        self.check(['aa', 'aaaa', 'aaaaaa'], ['aaaa', 'aaaaaa'])
        self.check(['only'], [])


if __name__ == '__main__':
    unittest.main()
