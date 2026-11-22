from itertools import product
import unittest

from python.p0678_valid_parenthesis_string import Solution


def explicit_replacements(text):
    choices = [('', '(', ')') if letter == '*' else (letter,) for letter in text]
    for candidate in product(*choices):
        balance = 0
        for letter in ''.join(candidate):
            balance += 1 if letter == '(' else -1
            if balance < 0:
                break
        else:
            if balance == 0:
                return True
    return False


class StarReplacementTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = explicit_replacements(text)
        result = Solution().checkValidString(text)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_every_small_input_against_all_literal_star_replacements(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('()*', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_balanced_empty_choices_and_failed_prefix(self):
        self.check('*' * 100, True)
        self.check('(' * 50 + ')' * 50, True)
        self.check('(' * 50 + '*' * 50, True)
        self.check('(' * 51 + '*' * 49, False)
        self.check(')' + '*' * 99, False)
        self.check('(' * 100, False)


if __name__ == '__main__':
    unittest.main()
