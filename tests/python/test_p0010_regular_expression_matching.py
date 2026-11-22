import re
import unittest
from itertools import product

from python.p0010_regular_expression_matching import Solution


class RegexMatchingTests(unittest.TestCase):
    def check(self, text, pattern, expected=None):
        if expected is None:
            expected = re.fullmatch(pattern, text) is not None
        result = Solution().isMatch(text, pattern)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected, (text, pattern))

    def test_all_small_valid_patterns_and_texts_including_empty_extensions(self):
        patterns = [''.join(tokens) for count in range(4)
                    for tokens in product(('a', 'a*', 'b', 'b*', '.', '.*'), repeat=count)]
        texts = [''.join(values) for size in range(6) for values in product('ab', repeat=size)]
        checks = extensions = 0
        for pattern in patterns:
            for text in texts:
                self.check(text, pattern)
                checks += 1
                extensions += not text or not pattern
        self.assertEqual((len(patterns), len(texts), checks, extensions), (259, 63, 16317, 321))

    def test_original_maximum_lengths_repeated_tokens_and_mismatching_tail(self):
        self.check('a' * 20, 'a*' * 10, True)
        self.check('a' * 19 + 'b', 'a*' * 10, False)
        self.check('ab' * 10, '.*', True)
        self.check('a' * 20, '.' * 20, True)
        self.check('a' * 20, 'a' * 19 + 'b', False)
        self.check('ab', '.*b', True)


if __name__ == '__main__':
    unittest.main()
