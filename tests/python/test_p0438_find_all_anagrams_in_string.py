import unittest
from collections import Counter
from itertools import product

from python.p0438_find_all_anagrams_in_string import Solution


class AllAnagramTests(unittest.TestCase):
    def check(self, text, pattern, expected=None):
        if expected is None:
            wanted = Counter(pattern)
            expected = [start for start in range(len(text) - len(pattern) + 1)
                        if Counter(text[start:start + len(pattern)]) == wanted]
        self.assertEqual(Solution().findAnagrams(text, pattern), expected)

    def test_all_small_binary_pairs_and_empty_text_extension_against_slices(self):
        texts = [''.join(chars) for size in range(8) for chars in product('ab', repeat=size)]
        patterns = [''.join(chars) for size in range(1, 5) for chars in product('ab', repeat=size)]
        checks = 0
        for text in texts:
            for pattern in patterns:
                self.check(text, pattern)
                checks += 1
        self.assertEqual(checks, 7650)

    def test_maximum_lengths_repeated_and_overlapping_windows(self):
        self.check('a' * 30000, 'a' * 100, list(range(29901)))
        self.check('ab' * 15000, 'ab' * 50, list(range(29901)))
        self.check('a' * 30000, 'a' * 30000, [0])
        self.check('a', 'a' * 30000, [])
        self.check('ab' * 15000, 'aa', [])


if __name__ == '__main__':
    unittest.main()
