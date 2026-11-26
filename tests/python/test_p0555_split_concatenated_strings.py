from itertools import product
import unittest

from python.p0555_split_concatenated_strings import Solution


def all_loop_orientations_oracle(words):
    answer = ''
    for reversed_flags in product((False, True), repeat=len(words)):
        loop = ''.join(word[::-1] if reverse else word for word, reverse in zip(words, reversed_flags))
        for cut in range(len(loop)):
            answer = max(answer, loop[cut:] + loop[:cut])
    return answer


class CutBlockOrientationTests(unittest.TestCase):
    def check(self, words, expected=None):
        before = words[:]
        actual = Solution().splitLoopedString(words)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, all_loop_orientations_oracle(words) if expected is None else expected)
        self.assertEqual(len(actual), sum(map(len, words)))
        self.assertEqual(words, before)

    def test_all_short_word_lists_against_all_orientations_and_global_cuts(self):
        vocabulary = [''.join(chars) for size in range(1, 4) for chars in product('ab', repeat=size)]
        lists = 0
        for size in range(1, 4):
            for words in product(vocabulary, repeat=size):
                self.check(list(words))
                lists += 1
        self.assertEqual((len(vocabulary), lists), (14, 2954))

    def test_maximum_total_length_block_count_and_cut_inside_a_block(self):
        self.check(['a'] * 999 + ['z'], 'z' + 'a' * 999)
        self.check(['a' * 499 + 'z' + 'b' * 500])
        self.check(['abc', 'xyz'], 'zyxcba')
        self.check(['abc'], 'cba')
        self.check(['abca', 'za'])
        self.check(['aba', 'bbb', 'aba'])
        self.check(['a'], 'a')


if __name__ == '__main__':
    unittest.main()
