import unittest
from itertools import product

from python.p0316_remove_duplicate_letters import Solution


def all_distinct_letter_choices(word):
    required = set(word)
    choices = []
    for mask in range(1 << len(word)):
        candidate = ''.join(character for index, character in enumerate(word) if mask & (1 << index))
        if len(candidate) == len(required) and set(candidate) == required:
            choices.append(candidate)
    return min(choices)


class DeduplicatedLetterTests(unittest.TestCase):
    def check(self, word, expected=None):
        if expected is None:
            expected = all_distinct_letter_choices(word)
        result = Solution().removeDuplicateLetters(word)
        self.assertIs(type(result), str)
        self.assertEqual(result, expected)

    def test_all_small_ternary_strings_against_position_subsequences(self):
        checks = 0
        for size in range(8):
            for characters in product('abc', repeat=size):
                self.check(''.join(characters))
                checks += 1
        self.assertEqual(checks, 3280)

    def test_maximum_lengths_order_last_occurrence_and_alphabet_cycles(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.check('z' * 10000, 'z')
        self.check(alphabet * 384 + alphabet[:16], alphabet)
        self.check(alphabet[::-1] * 384 + alphabet[::-1][:16], alphabet)
        self.check('ba', 'ba')
        self.check('bcabc', 'abc')
        self.check('cbacdcbc', 'acdb')


if __name__ == '__main__':
    unittest.main()
