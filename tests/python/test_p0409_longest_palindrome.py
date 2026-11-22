from functools import lru_cache
from itertools import product
import string
import unittest

from python.p0409_longest_palindrome import Solution


@lru_cache(None)
def actual_palindrome_candidates(text):
    alphabet = sorted(set(text))
    for size in range(len(text), 0, -1):
        for half in product(alphabet, repeat=size // 2):
            for center in alphabet if size % 2 else ('',):
                candidate = ''.join(half) + center + ''.join(reversed(half))
                available = list(text)
                for letter in candidate:
                    if letter not in available:
                        break
                    available.remove(letter)
                else:
                    return size
    return 0


class PalindromePairCapacityTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = actual_palindrome_candidates(''.join(sorted(text)))
        result = Solution().longestPalindrome(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_case_sensitive_strings_against_palindrome_texts(self):
        checks = 0
        for size in range(1, 8):
            for letters in product('aAb', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_case_sensitivity_and_distinct_characters(self):
        self.check('a' * 2000, 2000)
        self.check('a' * 1999 + 'A', 1999)
        self.check(string.ascii_letters, 1)
        self.check(string.ascii_letters * 38, 52 * 38)
        self.check('Aa', 1)
        self.check('abccccdd')


if __name__ == '__main__':
    unittest.main()
