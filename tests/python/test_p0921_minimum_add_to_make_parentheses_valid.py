from functools import lru_cache
from itertools import product
import unittest

from python.p0921_minimum_add_to_make_parentheses_valid import Solution



@lru_cache(None)
def valid_words(pairs):
    if pairs == 0:
        return ('',)
    return tuple('(' + inside + ')' + suffix for inside_size in range(pairs)
                 for inside in valid_words(inside_size)
                 for suffix in valid_words(pairs - inside_size - 1))



def is_subsequence(needle, haystack):
    position = 0
    for letter in haystack:
        if position < len(needle) and needle[position] == letter:
            position += 1
    return position == len(needle)



def shortest_valid_supersequence(text):
    for pairs in range((len(text) + 1) // 2, len(text) + 1):
        for candidate in valid_words(pairs):
            if is_subsequence(text, candidate):
                return len(candidate) - len(text)
    raise AssertionError('a valid insertion target must exist within this bound')


class MinimumAddedParenthesesTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = shortest_valid_supersequence(text)
        result = Solution().minAddToMakeValid(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_inputs_against_generated_valid_supersequences(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('()', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 510)

    def test_maximum_length_all_one_side_balanced_and_reversed_groups(self):
        self.check('(' * 1000, 1000)
        self.check(')' * 1000, 1000)
        self.check('()' * 500, 0)
        self.check(')' * 500 + '(' * 500, 1000)


if __name__ == '__main__':
    unittest.main()
