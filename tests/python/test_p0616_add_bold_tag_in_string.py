from itertools import product
import unittest

from python.p0616_add_bold_tag_in_string import Solution


def all_substring_intervals(text, words):
    intervals = [(start, end) for start in range(len(text))
                 for end in range(start + 1, len(text) + 1) if text[start:end] in words]
    merged = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    pieces, previous = [], 0
    for start, end in merged:
        pieces.extend((text[previous:start], '<b>' + text[start:end] + '</b>'))
        previous = end
    pieces.append(text[previous:])
    return ''.join(pieces)


class BoldIntervalTests(unittest.TestCase):
    def check(self, text, words, expected):
        before = words[:]
        result = Solution().addBoldTag(text, words)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)
        self.assertEqual(words, before)

    def test_all_small_strings_and_word_subsets_against_substring_interval_union(self):
        vocabulary = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
        cases = 0
        for size in range(1, 8):
            for letters in product('ab', repeat=size):
                text = ''.join(letters)
                for mask in range(64):
                    words = [word for index, word in enumerate(vocabulary) if mask & (1 << index)]
                    self.check(text, words, all_substring_intervals(text, words))
                    cases += 1
        self.assertEqual(cases, 16256)

    def test_maximum_lengths_overlaps_adjacency_empty_words_and_case(self):
        self.check('a' * 1000, ['a' * size for size in range(1, 101)], '<b>' + 'a' * 1000 + '</b>')
        text = 'A' * 999 + '1'
        self.check(text, ['A' * 1000, text], '<b>' + text + '</b>')
        self.check('aaabbb', ['aa', 'b'], '<b>aaabbb</b>')
        self.check('aabcc', ['aa', 'bc'], '<b>aabc</b>c')
        self.check('abc', ['b'], 'a<b>b</b>c')
        self.check('ABCabc1', ['abc', '1'], 'ABC<b>abc1</b>')
        self.check('abcxyz123', ['abc', '123'], '<b>abc</b>xyz<b>123</b>')
        self.check('abc', [], 'abc')
        self.check('a', ['abc'], 'a')


if __name__ == '__main__':
    unittest.main()
