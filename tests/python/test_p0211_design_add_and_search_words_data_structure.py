import unittest
from itertools import product

from python.p0211_design_add_and_search_words_data_structure import WordDictionary


def match_in_word_set(words, pattern):
    return any(len(word) == len(pattern) and all(token == '.' or token == letter for token, letter in zip(pattern, word))
               for word in words)


class WildcardDictionaryTests(unittest.TestCase):
    def test_all_small_dictionaries_and_legal_patterns_against_string_set(self):
        words = [''.join(values) for size in (1, 2) for values in product('ab', repeat=size)]
        patterns = [''.join(values) for size in (1, 2, 3) for values in product('ab.', repeat=size)
                    if values.count('.') <= 2]
        checks = 0
        for mask in range(1 << len(words)):
            chosen = {word for index, word in enumerate(words) if mask >> index & 1}
            dictionary = WordDictionary()
            for word in chosen:
                self.assertIsNone(dictionary.addWord(word))
            for pattern in patterns:
                result = dictionary.search(pattern)
                self.assertIs(type(result), bool)
                self.assertEqual(result, match_in_word_set(chosen, pattern))
                checks += 1
        self.assertEqual((len(words), len(patterns), checks), (6, 38, 2432))

    def test_maximum_calls_length_two_dots_duplicate_insertion_and_prefix_rejection(self):
        dictionary = WordDictionary()
        longest = 'a' * 25
        self.assertIsNone(dictionary.addWord(longest))
        self.assertIsNone(dictionary.addWord(longest))
        self.assertTrue(dictionary.search(longest))
        self.assertTrue(dictionary.search('.' + 'a' * 23 + '.'))
        self.assertFalse(dictionary.search('a' * 24))
        for index in range(4997):
            suffix = ''.join(chr(ord('a') + index // 26**place % 26) for place in (3, 2, 1, 0))
            word = 'k' + suffix
            self.assertIsNone(dictionary.addWord(word))
            self.assertTrue(dictionary.search('k' + word[1:3] + '..'))
        self.assertFalse(dictionary.search('b' * 25))


if __name__ == '__main__':
    unittest.main()
