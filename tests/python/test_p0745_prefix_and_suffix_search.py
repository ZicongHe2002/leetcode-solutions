import unittest
from itertools import product

from python.p0745_prefix_and_suffix_search import WordFilter


def reverse_original_scan(words, prefix, suffix):
    return next((index for index in range(len(words) - 1, -1, -1)
                 if words[index].startswith(prefix) and words[index].endswith(suffix)), -1)


class PrefixSuffixSearchTests(unittest.TestCase):
    def test_all_small_word_lists_and_query_pairs_against_reverse_original_scan(self):
        pool = [''.join(chars) for size in (1, 2) for chars in product('ab', repeat=size)]
        queries = [''.join(chars) for size in (1, 2, 3) for chars in product('ab', repeat=size)]
        lists = checked = 0
        for size in range(1, 5):
            for values in product(pool, repeat=size):
                words, before = list(values), list(values)
                obj = WordFilter(words)
                self.assertEqual(words, before)
                lists += 1
                for prefix, suffix in product(queries, repeat=2):
                    result = obj.f(prefix, suffix)
                    self.assertIs(type(result), int)
                    self.assertEqual(result, reverse_original_scan(words, prefix, suffix), (words, prefix, suffix))
                    checked += 1
                self.assertEqual(words, before)
        self.assertEqual((lists, checked), (1554, 304584))

    def test_examples_duplicate_maximum_overlap_and_ten_thousand_word_query_boundary(self):
        self.assertEqual(WordFilter(['apple']).f('a', 'e'), 0)
        obj = WordFilter(['apple', 'apply', 'apple'])
        for prefix, suffix, expected in (('app','le',2),('app','ly',1),('apple','apple',2),('z','e',-1)):
            self.assertEqual(obj.f(prefix, suffix), expected)
        words = ['aaaa' + ''.join(chr(97 + digit) for digit in (i // 676, i // 26 % 26, i % 26)) for i in range(10000)]
        before, obj = words[:], WordFilter(words)
        self.assertEqual({len(word) for word in words}, {7})
        calls = 0
        for index, word in enumerate(words):
            if index == 0:
                prefix, suffix, expected = 'aaaa', 'a', 9984
            elif index == 1:
                prefix, suffix, expected = 'aaaaaaa', 'aaaaaaa', 0
            elif index == 2:
                prefix, suffix, expected = 'z', 'z', -1
            else:
                prefix, suffix, expected = word, word[-1], index
            result = obj.f(prefix, suffix)
            self.assertIs(type(result), int)
            self.assertEqual(result, expected)
            calls += 1
        self.assertEqual(calls, 10000)
        self.assertEqual(words, before)


if __name__ == '__main__':
    unittest.main()
