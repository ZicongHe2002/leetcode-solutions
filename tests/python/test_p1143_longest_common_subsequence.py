import unittest
from itertools import product

from python.p1143_longest_common_subsequence import Solution


def subsequences(text):
    return {''.join(letter for index, letter in enumerate(text) if mask & (1 << index))
            for mask in range(1 << len(text))}


class CommonSubsequenceTests(unittest.TestCase):
    def check(self, left, right, expected):
        self.assertEqual(Solution().longestCommonSubsequence(left, right), expected)

    def test_all_small_binary_string_pairs_against_subsequence_intersection(self):
        words = [''.join(letters) for size in range(6) for letters in product('ab', repeat=size)]
        choices = {word: subsequences(word) for word in words}
        checks = 0
        for left in words:
            for right in words:
                expected = max(map(len, choices[left] & choices[right]))
                self.check(left, right, expected)
                checks += 1
        self.assertEqual((len(words), checks), (63, 3969))

    def test_examples_repeated_characters_and_maximum_lengths(self):
        self.check('abcde', 'ace', 3)
        self.check('abc', 'def', 0)
        self.check('aaaa', 'aa', 2)
        self.check('', 'abc', 0)
        self.check('abc', '', 0)
        self.check('a' * 1000, 'a' * 1000, 1000)
        self.check('a' * 1000, 'b' * 1000, 0)
        self.check('z' * 1000, 'z', 1)
        self.check('z', 'z' * 1000, 1)


if __name__ == '__main__':
    unittest.main()
