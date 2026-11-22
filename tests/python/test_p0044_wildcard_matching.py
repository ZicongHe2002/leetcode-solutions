import unittest
from fnmatch import fnmatchcase
from itertools import product

from python.p0044_wildcard_matching import Solution


class WildcardTests(unittest.TestCase):
    def check(self, text, pattern, expected=None):
        if expected is None:
            expected = fnmatchcase(text, pattern)
        result = Solution().isMatch(text, pattern)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, (text, pattern))

    def test_all_small_glob_patterns_and_texts_against_fnmatchcase(self):
        patterns = [''.join(values) for size in range(6) for values in product('ab?*', repeat=size)]
        texts = [''.join(values) for size in range(6) for values in product('ab', repeat=size)]
        checks = 0
        for pattern in patterns:
            for text in texts:
                self.check(text, pattern)
                checks += 1
        self.assertEqual((len(patterns), len(texts), checks), (1365, 63, 85995))

    def test_maximum_lengths_empty_inputs_repeated_stars_and_wrong_tail(self):
        self.check('a' * 2000, '*' * 2000, True)
        self.check('a' * 2000, '*a' * 1000, True)
        self.check('a' * 1999 + 'b', 'a' * 2000, False)
        self.check('ab' * 1000, '?' * 2000, True)
        self.check('', '*' * 2000, True)
        self.check('a' * 2000, '', False)


if __name__ == '__main__':
    unittest.main()
