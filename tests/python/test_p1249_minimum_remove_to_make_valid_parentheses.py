from functools import lru_cache
from itertools import product
import unittest

from python.p1249_minimum_remove_to_make_valid_parentheses import Solution


def balanced(text):
    count = 0
    for letter in text:
        if letter == '(':
            count += 1
        elif letter == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


@lru_cache(None)
def minimum_removed_from_skeleton(skeleton):
    best = 0
    for mask in range(1 << len(skeleton)):
        candidate = ''.join(letter for index, letter in enumerate(skeleton) if mask >> index & 1)
        if balanced(candidate):
            best = max(best, len(candidate))
    return len(skeleton) - best


class MinimumRemovalOutputTests(unittest.TestCase):
    def check(self, text, expected_removed=None):
        if expected_removed is None:
            skeleton = ''.join(letter for letter in text if letter in '()')
            expected_removed = minimum_removed_from_skeleton(skeleton)
        result = Solution().minRemoveToMakeValid(text)
        self.assertIs(type(result), str)
        self.assertTrue(balanced(result))
        self.assertEqual(''.join(letter for letter in result if letter not in '()'),
                         ''.join(letter for letter in text if letter not in '()'))
        position = 0
        for letter in result:
            while position < len(text) and text[position] != letter:
                position += 1
            self.assertLess(position, len(text))
            position += 1
        self.assertEqual(len(text) - len(result), expected_removed)

    def test_all_small_texts_against_all_retained_parentheses_subsets(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('a()', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_letters_balanced_and_unmatchable_groups(self):
        self.check('a' * 100000, 0)
        self.check('(' * 100000, 100000)
        self.check('(' * 50000 + ')' * 50000, 0)
        self.check(')' * 25000 + 'a' * 50000 + '(' * 25000, 50000)


if __name__ == '__main__':
    unittest.main()
