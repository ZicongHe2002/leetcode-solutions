from itertools import product
import unittest

from python.p0557_reverse_words_in_a_string_iii import Solution


def two_boundary_source_index_oracle(text):
    left = [0] * len(text)
    right = [0] * len(text)
    previous_space = -1
    for index, char in enumerate(text):
        if char == ' ':
            previous_space = index
        left[index] = previous_space + 1
    next_space = len(text)
    for index in range(len(text) - 1, -1, -1):
        if text[index] == ' ':
            next_space = index
        right[index] = next_space
    return ''.join(' ' if char == ' ' else text[left[index] + right[index] - 1 - index]
                   for index, char in enumerate(text))


class PerWordCharacterReverseTests(unittest.TestCase):
    def check(self, text, expected=None):
        actual = Solution().reverseWords(text)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, two_boundary_source_index_oracle(text) if expected is None else expected)
        self.assertEqual(len(actual), len(text))

    def test_all_short_ascii_word_lists_against_boundary_source_indices(self):
        vocabulary = [''.join(chars) for size in range(1, 4) for chars in product('aB!', repeat=size)]
        records = 0
        for size in range(1, 4):
            for words in product(vocabulary, repeat=size):
                self.check(' '.join(words))
                records += 1
        self.assertEqual((len(vocabulary), records), (39, 60879))

    def test_maximum_length_single_word_many_words_and_printable_ascii(self):
        text = 'aB!' * 16666 + 'aB'
        self.assertEqual(len(text), 50000)
        self.check(text)
        text = 'a ' * 24999 + 'ab'
        self.assertEqual(len(text), 50000)
        self.check(text, 'a ' * 24999 + 'ba')
        text = 'ab ' * 16666 + 'ab'
        self.assertEqual(len(text), 50000)
        self.check(text, 'ba ' * 16666 + 'ba')
        self.check("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc")
        self.check('Mr Ding', 'rM gniD')
        self.check('12!? aB', '?!21 Ba')
        self.check('!', '!')


if __name__ == '__main__':
    unittest.main()
