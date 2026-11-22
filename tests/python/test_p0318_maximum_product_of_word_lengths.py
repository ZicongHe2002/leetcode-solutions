from itertools import product
import unittest

from python.p0318_maximum_product_of_word_lengths import Solution


def character_set_pair_reference(words):
    return max((len(words[left]) * len(words[right])
                for left in range(len(words))
                for right in range(left + 1, len(words))
                if set(words[left]).isdisjoint(words[right])), default=0)


class AlphabetMaskWordProductTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        if expected is None:
            expected = character_set_pair_reference(words)
        result = Solution().maxProduct(words)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)
        self.assertEqual(words, before)

    def test_all_small_word_lists_against_direct_character_set_pairs(self):
        vocabulary = ('a', 'b', 'ab', 'aa', 'bb', 'abc')
        checks = 0
        for size in range(2, 6):
            for words in product(vocabulary, repeat=size):
                self.check(list(words))
                checks += 1
        self.assertEqual(checks, 9324)

    def test_maximum_dimensions_repeated_letters_and_high_alphabet_bits(self):
        self.check(['a' * 1000] * 500 + ['b' * 1000] * 500, 1000000)
        self.check(['a' * 1000] * 1000, 0)
        self.check(['a' * 1000, 'b' * 999, 'ab' * 500], 999000)
        self.check(['az', 'by'], 4)
        self.check(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'], 16)


if __name__ == '__main__':
    unittest.main()
