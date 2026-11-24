import re
import unittest
from itertools import product

from python.p0065_valid_number import Solution


GRAMMAR = re.compile(r'[+-]?(?:[0-9]+(?:\.[0-9]*)?|\.[0-9]+)(?:[eE][+-]?[0-9]+)?')


class ValidNumberTests(unittest.TestCase):
    def test_small_strings_against_independent_grammar(self):
        count = 0
        for size in range(6):
            for characters in product('01.eE+-x', repeat=size):
                text = ''.join(characters)
                self.assertIs(Solution().isNumber(text), GRAMMAR.fullmatch(text) is not None, text)
                count += 1
        self.assertEqual(count, 37449)

    def test_examples_signs_exponents_and_twenty_character_boundaries(self):
        valid = ('2', '0089', '-0.1', '+3.14', '4.', '-.9', '2e10', '-90E3',
                 '3e+7', '+6e-1', '53.5e93', '-123.456e789', '1.e2',
                 '9' * 20, '-' + '9' * 19, '.' + '1' * 19,
                 '1e' + '9' * 18, '-.1E+' + '9' * 15)
        invalid = ('abc', '1a', '1e', 'e3', '99e2.5', '--6', '-+3', '95a54e53',
                   '.', '+.', '.e1', '1e+', '1e-+2', '1ee2', '1e2e3',
                   'NaN', 'Infinity', '9' * 19 + 'x', '1' * 18 + 'e+', '')
        for text in valid:
            self.assertLessEqual(len(text), 20)
            self.assertIsNotNone(GRAMMAR.fullmatch(text))
            self.assertIs(Solution().isNumber(text), True, text)
        for text in invalid:
            self.assertLessEqual(len(text), 20)
            self.assertIsNone(GRAMMAR.fullmatch(text))
            self.assertIs(Solution().isNumber(text), False, text)


if __name__ == '__main__':
    unittest.main()
