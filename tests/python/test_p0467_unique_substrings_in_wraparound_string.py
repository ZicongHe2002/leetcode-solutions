from itertools import product
import unittest

from python.p0467_unique_substrings_in_wraparound_string import Solution


def explicit_substring_oracle(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    successor = dict(zip(alphabet, alphabet[1:] + alphabet[:1]))
    valid = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            candidate = s[start:end]
            if all(successor[left] == right for left, right in zip(candidate, candidate[1:])):
                valid.add(candidate)
    return len(valid)


class WraparoundSuffixCountTests(unittest.TestCase):
    def check(self, s, expected=None):
        actual = Solution().findSubstringInWraproundString(s)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, explicit_substring_oracle(s) if expected is None else expected)

    def test_all_small_wrap_and_break_strings_against_actual_substring_sets(self):
        strings = 0
        for size in range(9):
            for chars in product('abz', repeat=size):
                self.check(''.join(chars))
                strings += 1
        self.assertEqual(strings, 9841)

    def test_maximum_length_cycles_repeated_letters_and_wrap_boundaries(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.check((alphabet * 3847)[:100000], 26 * 100000 - 325)
        self.check('a' * 100000, 1)
        self.check('za' * 50000, 3)
        self.check('zab', 6)
        self.check(alphabet, 351)
        self.check('cac', 2)
        self.check('az', 2)


if __name__ == '__main__':
    unittest.main()
