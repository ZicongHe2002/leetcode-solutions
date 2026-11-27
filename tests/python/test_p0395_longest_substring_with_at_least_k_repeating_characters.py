from collections import Counter
from itertools import product
import unittest

from python.p0395_longest_substring_with_at_least_k_repeating_characters import Solution


def all_substring_frequency_oracle(text, k):
    best = 0
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            counts = Counter(text[start:end])
            if all(value >= k for value in counts.values()):
                best = max(best, end - start)
    return best


class RepeatedLetterWindowTests(unittest.TestCase):
    def check(self, text, k, expected=None):
        actual = Solution().longestSubstring(text, k)
        self.assertIs(type(actual), int)
        self.assertEqual(actual, all_substring_frequency_oracle(text, k) if expected is None else expected)

    def test_all_small_strings_and_thresholds_against_all_intervals(self):
        strings = queries = 0
        for size in range(8):
            for chars in product('abc', repeat=size):
                text = ''.join(chars)
                strings += 1
                for k in range(1, 6):
                    self.check(text, k)
                    queries += 1
        self.assertEqual((strings, queries), (3280, 16400))

    def test_maximum_length_alphabet_and_frequency_boundaries(self):
        self.check('aaabb', 3, 3)
        self.check('ababbc', 2, 5)
        self.check('a' * 10000, 10000, 10000)
        self.check('a' * 9999 + 'b', 10000, 0)
        self.check('a' * 4999 + 'b' + 'a' * 5000, 5000, 5000)
        self.check('a' * 10000, 100000, 0)
        text = 'abcdefghijklmnopqrstuvwxyz' * 384 + 'abcdefghijklmnop'
        self.assertEqual(len(text), 10000)
        self.check(text, 384, 10000)
        self.check(text, 385, 0)


if __name__ == '__main__':
    unittest.main()
