from functools import lru_cache
import unittest

from python.p1614_maximum_nesting_depth_of_the_parentheses import Solution



@lru_cache(None)
def valid_words(pairs):
    if pairs == 0:
        return ('',)
    return tuple('(' + inside + ')' + suffix for inside_size in range(pairs)
                 for inside in valid_words(inside_size)
                 for suffix in valid_words(pairs - inside_size - 1))



def grammar_depth(word):
    if not word:
        return 0
    balance = 0
    for index, letter in enumerate(word):
        balance += 1 if letter == '(' else -1
        if balance == 0:
            return max(1 + grammar_depth(word[1:index]), grammar_depth(word[index + 1:]))
    raise AssertionError('reference input is not balanced')


class ParenthesesGrammarDepthTests(unittest.TestCase):
    def check(self, text, expected):
        result = Solution().maxDepth(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_every_small_balanced_structure_with_non_parenthesis_digit(self):
        checks = 0
        for pairs in range(8):
            for word in valid_words(pairs):
                self.check('0' + word, grammar_depth(word))
                checks += 1
        self.assertEqual(checks, 626)

    def test_maximum_length_depth_and_all_allowed_non_parenthesis_types(self):
        self.check('(' * 50 + ')' * 50, 50)
        self.check('0' * 100, 0)
        self.check('0123456789+-*/', 0)
        self.check('(1+(2*3)+((8)/4))+1', 3)


if __name__ == '__main__':
    unittest.main()
