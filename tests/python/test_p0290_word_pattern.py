import unittest
from itertools import product

from python.p0290_word_pattern import Solution


class WordPatternTests(unittest.TestCase):
    def check(self, pattern, words, expected=None):
        if expected is None:
            expected = len(pattern) == len(words) and all((pattern[i] == pattern[j]) == (words[i] == words[j])
                                                         for i in range(len(pattern)) for j in range(len(pattern)))
        result = Solution().wordPattern(pattern, ' '.join(words))
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_patterns_and_word_sequences_against_position_equivalence(self):
        checks = 0
        for size in range(1, 5):
            for letters in product('abc', repeat=size):
                pattern = ''.join(letters)
                for words in product(('x', 'y', 'xy'), repeat=size):
                    self.check(pattern, words)
                    checks += 1
        self.assertEqual(checks, 7380)

    def test_maximum_sizes_collisions_counts_and_spacing_extensions(self):
        self.check('ab' * 150, ['foo', 'bar'] * 150, True)
        self.check('a', ['x' * 3000], True)
        self.check('ab', ['same', 'same'], False)
        self.check('aa', ['one'], False)
        self.check('', [], True)
        self.assertTrue(Solution().wordPattern('abba', '  dog   cat cat   dog  '))


if __name__ == '__main__':
    unittest.main()
