from itertools import product
import re
import unittest

from python.p0520_detect_capital import Solution


CAPITAL_GRAMMAR = re.compile(r'(?:[A-Z]+|[a-z]+|[A-Z][a-z]+)')


class CapitalDistributionTests(unittest.TestCase):
    def check(self, word, expected=None):
        actual = Solution().detectCapitalUse(word)
        self.assertIs(type(actual), bool)
        self.assertEqual(actual, bool(CAPITAL_GRAMMAR.fullmatch(word)) if expected is None else expected)

    def test_all_short_case_patterns_against_complete_word_grammar(self):
        words = 0
        for size in range(1, 8):
            for chars in product('aAbB', repeat=size):
                self.check(''.join(chars))
                words += 1
        self.assertEqual(words, 21844)

    def test_maximum_length_initial_final_case_and_single_letters(self):
        self.check('A' * 100, True)
        self.check('a' * 100, True)
        self.check('A' + 'b' * 99, True)
        self.check('a' * 99 + 'A', False)
        self.check('A' * 99 + 'a', False)
        self.check('USA', True)
        self.check('Google', True)
        self.check('FlaG', False)
        self.check('A', True)
        self.check('a', True)


if __name__ == '__main__':
    unittest.main()
