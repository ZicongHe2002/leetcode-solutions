import string
import unittest
from itertools import combinations, product

from python.p0676_implement_magic_dictionary import MagicDictionary


def substitutions(word, dictionary):
    words = set(dictionary)
    return any(word[:i] + letter + word[i + 1:] in words
               for i, old in enumerate(word)
               for letter in string.ascii_lowercase if letter != old)


class MagicDictionaryTests(unittest.TestCase):
    def test_small_distinct_dictionaries_against_actual_character_substitution(self):
        words = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        queries = [''.join(chars) for size in range(1, 4) for chars in product('abc', repeat=size)]
        dictionaries = checked = 0
        for size in range(1, 4):
            for selected in combinations(words, size):
                dictionary = list(selected)
                before = dictionary[:]
                obj = MagicDictionary()
                self.assertIsNone(obj.buildDict(dictionary))
                for query in queries:
                    result = obj.search(query)
                    self.assertIs(type(result), bool)
                    self.assertEqual(result, substitutions(query, dictionary), (dictionary, query))
                    checked += 1
                self.assertEqual(dictionary, before)
                dictionaries += 1
        self.assertEqual((dictionaries, checked), (469, 18291))

    def test_maximum_dictionary_word_length_calls_and_exactly_one_change(self):
        dictionary = [chr(97 + i // 26) + chr(97 + i % 26) + 'a' * 98 for i in range(100)]
        before = dictionary[:]
        obj = MagicDictionary()
        obj.buildDict(dictionary)
        queries = dictionary[:50] + ['z' * 100, 'a', 'a' * 99, 'a' * 100, 'b' * 100] * 10
        self.assertEqual(len(queries), 100)
        for query in queries:
            self.assertEqual(obj.search(query), substitutions(query, dictionary))
        self.assertEqual(dictionary, before)
        single = MagicDictionary()
        single.buildDict(['hello'])
        self.assertFalse(single.search('hello'))
        self.assertTrue(single.search('hhllo'))
        self.assertFalse(single.search('hell'))
        other = MagicDictionary()
        other.buildDict(['hello', 'hallo'])
        self.assertTrue(other.search('hello'))


if __name__ == '__main__':
    unittest.main()
