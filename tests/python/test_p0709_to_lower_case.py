import random
import string
import unittest
from itertools import product

from python.p0709_to_lower_case import Solution


UPPER_TO_LOWER = dict(zip(string.ascii_uppercase, string.ascii_lowercase))


def letter_table(s):
    return ''.join(UPPER_TO_LOWER.get(char, char) for char in s)


class ToLowerCaseTests(unittest.TestCase):
    def check(self, s):
        result = Solution().toLowerCase(s)
        self.assertIs(type(result), str)
        self.assertEqual(result, letter_table(s))
        self.assertEqual(len(result), len(s))
        self.assertEqual(Solution().toLowerCase(result), result)

    def test_every_printable_ascii_character_and_pair_against_letter_table(self):
        alphabet = ''.join(chr(code) for code in range(32, 127))
        checked = 0
        for size in (1, 2):
            for chars in product(alphabet, repeat=size):
                self.check(''.join(chars))
                checked += 1
        self.assertEqual(checked, 9120)

    def test_hundred_character_boundaries_seeded_mixtures_and_adjacent_punctuation(self):
        alphabet = ''.join(chr(code) for code in range(32, 127))
        self.check((alphabet * 2)[:100])
        self.check('A' * 100)
        self.check('Z' * 100)
        self.check(' ' * 100)
        self.check('@AZ[' + chr(92) + ']^_`az{|}~0123456789')
        rng = random.Random(709)
        for _ in range(1000):
            self.check(''.join(rng.choice(alphabet) for _ in range(rng.randrange(1, 101))))
        for text in ('Hello', 'here', 'LOVELY'):
            self.check(text)


if __name__ == '__main__':
    unittest.main()
