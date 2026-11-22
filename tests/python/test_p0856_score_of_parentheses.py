from functools import lru_cache
import unittest

from python.p0856_score_of_parentheses import Solution



@lru_cache(None)
def valid_words(pairs):
    if pairs == 0:
        return ('',)
    return tuple('(' + inside + ')' + suffix for inside_size in range(pairs)
                 for inside in valid_words(inside_size)
                 for suffix in valid_words(pairs - inside_size - 1))



def grammar_score(word):
    if not word:
        return 0
    balance = 0
    for index, letter in enumerate(word):
        balance += 1 if letter == '(' else -1
        if balance == 0:
            first = 1 if index == 1 else 2 * grammar_score(word[1:index])
            return first + grammar_score(word[index + 1:])
    raise AssertionError('reference input is not balanced')


class ParenthesesLeafScoreTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = grammar_score(text)
        result = Solution().scoreOfParentheses(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_balanced_word_against_original_scoring_grammar(self):
        checks = 0
        for pairs in range(1, 9):
            for word in valid_words(pairs):
                self.check(word)
                checks += 1
        self.assertEqual(checks, 2055)

    def test_maximum_length_nested_concatenated_and_wrapped_leaves(self):
        self.check('(' * 25 + ')' * 25, 1 << 24)
        self.check('()' * 25, 25)
        self.check('(' + '()' * 24 + ')', 48)


if __name__ == '__main__':
    unittest.main()
