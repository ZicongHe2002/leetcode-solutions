from itertools import product
import unittest

from python.p0151_reverse_words_in_string import Solution


def scan_nonspace_intervals(value):
    words, start = [], None
    for index, character in enumerate(value):
        if character == ' ':
            if start is not None:
                words.append(value[start:index])
                start = None
        elif start is None:
            start = index
    if start is not None:
        words.append(value[start:])
    return words


class ReverseWordsIntervalScannerTests(unittest.TestCase):
    def check(self, value, expected=None):
        words = scan_nonspace_intervals(value)
        result = Solution().reverseWords(value)
        self.assertIs(type(result), str)
        self.assertEqual(result.split(' '), list(reversed(words)))
        self.assertFalse(result.startswith(' ') or result.endswith(' '))
        self.assertNotIn('  ', result)
        if expected is not None:
            self.assertEqual(result, expected)
        return result

    def test_every_small_valid_string_against_independent_word_boundaries(self):
        checked = skipped = 0
        for size in range(1, 7):
            for characters in product('aB1 ', repeat=size):
                value = ''.join(characters)
                if value.strip(' '):
                    self.check(value)
                    checked += 1
                else:
                    skipped += 1
        self.assertEqual((checked, skipped), (5454, 6))

    def test_maximum_length_long_word_padding_and_many_words(self):
        self.check('A1' * 5000, 'A1' * 5000)
        padded = ' ' * 4999 + 'A1' + ' ' * 4999
        self.assertEqual(len(padded), 10000)
        self.check(padded, 'A1')
        many = 'a ' * 5000
        self.assertEqual(len(many), 10000)
        self.assertEqual(len(self.check(many)), 9999)
        self.check('the sky is blue', 'blue is sky the')
        self.check('a good   example', 'example good a')


if __name__ == '__main__':
    unittest.main()
