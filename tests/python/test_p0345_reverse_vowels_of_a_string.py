from itertools import product
import unittest

from python.p0345_reverse_vowels_of_a_string import Solution


def vowel_position_oracle(text):
    vowels = [char for char in text if char in 'aeiouAEIOU']
    reversed_vowels = iter(vowels[::-1])
    return ''.join(next(reversed_vowels) if char in 'aeiouAEIOU' else char for char in text)


class VowelPositionReverseTests(unittest.TestCase):
    def check(self, text, expected=None):
        actual = Solution().reverseVowels(text)
        self.assertIs(type(actual), str)
        self.assertEqual(actual, vowel_position_oracle(text) if expected is None else expected)
        self.assertEqual(len(actual), len(text))
        for index, char in enumerate(text):
            if char not in 'aeiouAEIOU':
                self.assertEqual(actual[index], char)

    def test_all_small_strings_against_position_reconstruction(self):
        inputs = 0
        for size in range(8):
            for chars in product('aEbx', repeat=size):
                self.check(''.join(chars))
                inputs += 1
        self.assertEqual(inputs, 21845)

    def test_uppercase_punctuation_and_maximum_length(self):
        self.check('AEIOUaeiou', 'uoieaUOIEA')
        self.check('a.,E', 'E.,a')
        self.check('a' * 150000 + 'E' * 150000, 'E' * 150000 + 'a' * 150000)
        self.check('b' * 300000, 'b' * 300000)
        self.check('leetcode', 'leotcede')
        self.check('bAb', 'bAb')


if __name__ == '__main__':
    unittest.main()
