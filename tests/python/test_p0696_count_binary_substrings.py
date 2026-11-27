import unittest
from itertools import product

from python.p0696_count_binary_substrings import Solution


def all_substrings(s):
    result = 0
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            text = s[start:end]
            result += (text.count('0') == text.count('1')
                       and sum(a != b for a, b in zip(text, text[1:])) == 1)
    return result


class BinarySubstringCountTests(unittest.TestCase):
    def check(self, s, expected=None):
        result = Solution().countBinarySubstrings(s)
        self.assertIs(type(result), int)
        self.assertEqual(result, all_substrings(s) if expected is None else expected)

    def test_all_small_binary_strings_against_actual_balanced_one_change_slices(self):
        checked = 0
        for size in range(1, 13):
            for chars in product('01', repeat=size):
                self.check(''.join(chars))
                checked += 1
        self.assertEqual(checked, 8190)

    def test_one_hundred_thousand_characters_boundaries_and_repeated_occurrences(self):
        self.check('0' * 100000, 0)
        self.check('01' * 50000, 99999)
        self.check('0' * 50000 + '1' * 50000, 50000)
        self.check('0' * 99999 + '1', 1)
        self.check('0' * 40000 + '1' * 20000 + '0' * 40000, 40000)
        self.check('00110011', 6)
        self.check('10101', 4)


if __name__ == '__main__':
    unittest.main()
