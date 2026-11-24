import unittest
from collections import Counter
from itertools import product

from python.p0567_permutation_in_string import Solution


class PermutationWindowTests(unittest.TestCase):
    def check(self, pattern, text, expected=None):
        if expected is None:
            wanted = Counter(pattern)
            expected = any(Counter(text[start:start + len(pattern)]) == wanted
                           for start in range(len(text) - len(pattern) + 1))
        result = Solution().checkInclusion(pattern, text)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_binary_pairs_and_empty_extensions_against_slice_counters(self):
        patterns = [''.join(chars) for size in range(6) for chars in product('ab', repeat=size)]
        texts = [''.join(chars) for size in range(8) for chars in product('ab', repeat=size)]
        checks = 0
        for pattern in patterns:
            for text in texts:
                self.check(pattern, text)
                checks += 1
        self.assertEqual(checks, 16065)

    def test_maximum_lengths_missing_character_and_terminal_match(self):
        self.check('b', 'a' * 10000, False)
        self.check('a' * 10000, 'a' * 10000, True)
        self.check('a' * 9999 + 'b', 'b' + 'a' * 9999, True)
        self.check('a' * 10000, 'a', False)


if __name__ == '__main__':
    unittest.main()
