from functools import lru_cache
from itertools import product
import unittest

from python.p1541_minimum_insertions_to_balance_a_parentheses_string import Solution


@lru_cache(None)
def double_close_words(pairs):
    if pairs == 0:
        return ('',)
    return tuple('(' + inside + '))' + suffix for inside_size in range(pairs)
                 for inside in double_close_words(inside_size)
                 for suffix in double_close_words(pairs - inside_size - 1))



def is_subsequence(needle, haystack):
    position = 0
    for letter in haystack:
        if position < len(needle) and needle[position] == letter:
            position += 1
    return position == len(needle)



def shortest_double_close_target(text):
    for pairs in range((len(text) + 2) // 3, len(text) + 1):
        for candidate in double_close_words(pairs):
            if is_subsequence(text, candidate):
                return len(candidate) - len(text)
    raise AssertionError('a valid insertion target must exist within this bound')


class DoubleClosingInsertionTests(unittest.TestCase):
    def check(self, text, expected=None):
        if expected is None:
            expected = shortest_double_close_target(text)
        result = Solution().minInsertions(text)
        self.assertIs(type(result), int)
        self.assertEqual(result, expected)

    def test_all_small_inputs_against_double_close_grammar_targets(self):
        checks = 0
        for size in range(1, 8):
            for letters in product('()', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 254)

    def test_maximum_length_single_sides_odd_closes_and_repeated_pairs(self):
        self.check('(' * 100000, 200000)
        self.check(')' * 100000, 50000)
        self.check(')' * 99999, 50001)
        self.check('()' * 50000, 50000)
        self.check('))())(', 3)


if __name__ == '__main__':
    unittest.main()
