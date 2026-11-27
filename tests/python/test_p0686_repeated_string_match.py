import unittest
from itertools import product

from python.p0686_repeated_string_match import Solution


def actual_repetitions(a, b):
    for count in range(1, len(b) + 2):
        if b in a * count:
            return count
    return -1


class RepeatedStringMatchTests(unittest.TestCase):
    def check(self, a, b, expected=None):
        result = Solution().repeatedStringMatch(a, b)
        self.assertIs(type(result), int)
        self.assertEqual(result, actual_repetitions(a, b) if expected is None else expected, (a[:20], b[:20]))

    def test_all_small_binary_strings_against_actual_repeated_text(self):
        sources = [''.join(chars) for size in range(1, 5) for chars in product('ab', repeat=size)]
        targets = [''.join(chars) for size in range(1, 8) for chars in product('ab', repeat=size)]
        checked = 0
        for a in sources:
            for b in targets:
                self.check(a, b)
                checked += 1
        self.assertEqual(checked, 7620)

    def test_ten_thousand_characters_virtual_boundaries_and_long_fallbacks(self):
        self.check('a', 'a' * 10000, 10000)
        self.check('ab', 'ba' * 5000, 5001)
        self.check('ab' * 5000, 'ba' * 5000, 2)
        self.check('a' * 9999 + 'b', 'b' + 'a' * 9999, 2)
        self.check('a' * 10000, 'a' * 9999 + 'b', -1)
        self.check('abcd', 'cdabcdab', 3)
        self.check('abc', 'abc', 1)
        self.check('abc', 'ac', -1)


if __name__ == '__main__':
    unittest.main()
