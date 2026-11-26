from itertools import islice, permutations, product
from string import ascii_lowercase
import unittest

from python.p0336_palindrome_pairs import Solution


def concatenation_oracle(words):
    answers = set()
    for first in range(len(words)):
        for second in range(len(words)):
            if first == second:
                continue
            text = words[first] + words[second]
            if all(text[index] == text[-index - 1] for index in range(len(text) // 2)):
                answers.add((first, second))
    return answers


class PalindromeSplitPairsTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        actual = Solution().palindromePairs(words)
        self.assertIs(type(actual), list)
        self.assertTrue(all(type(pair) is list and len(pair) == 2 for pair in actual))
        result = set(map(tuple, actual))
        self.assertEqual(len(actual), len(result))
        self.assertTrue(all(first != second for first, second in result))
        self.assertEqual(result, concatenation_oracle(words) if expected is None else expected)
        self.assertEqual(words, before)

    def test_all_small_ordered_unique_dictionaries_against_full_concatenation(self):
        vocabulary = ('', 'a', 'b', 'aa', 'ab', 'ba', 'bb')
        dictionaries = 0
        for size in range(5):
            for words in permutations(vocabulary, size):
                self.check(list(words))
                dictionaries += 1
        self.assertEqual(dictionaries, 1100)

    def test_empty_word_mixed_lengths_and_both_input_limits(self):
        self.check(['', 'aba', 'ab', 'ba'])
        self.check(['abcd', 'dcba', 'lls', 's', 'sssll'])
        self.check(['a' * 300, 'b' + 'a' * 299, ''])
        words = [''.join(chars) for chars in islice(product(ascii_lowercase, repeat=3), 5000)]
        expected = set()
        for index in range(5000):
            reversed_index = (index % 26) * 26**2 + ((index // 26) % 26) * 26 + index // 26**2
            if reversed_index < 5000 and reversed_index != index:
                expected.add((index, reversed_index))
        self.check(words, expected)


if __name__ == '__main__':
    unittest.main()
