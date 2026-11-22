from functools import lru_cache
from itertools import product
import unittest

from python.p1544_make_the_string_great import Solution


@lru_cache(None)
def all_good_endings(text):
    outcomes = set()
    for index in range(len(text) - 1):
        if text[index].swapcase() == text[index + 1]:
            outcomes.update(all_good_endings(text[:index] + text[index + 2:]))
    return frozenset(outcomes or (text,))


class OppositeCaseDeletionTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().makeGood(text)
        self.assertIs(type(result), str)
        if expected is None:
            self.assertEqual(all_good_endings(text), frozenset((result,)))
        else:
            self.assertEqual(result, expected)

    def test_all_small_texts_against_all_swapcase_rewrite_orders(self):
        checks = 0
        for size in range(1, 7):
            for letters in product('aAbB', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 5460)

    def test_maximum_length_cascades_and_same_case_preservation(self):
        self.check('a' * 50 + 'A' * 50, '')
        self.check('ab' * 50, 'ab' * 50)
        self.check('A' * 100, 'A' * 100)
        self.check('aA' * 50, '')
        self.check('zZ', '')
        self.check('Zz', '')
        self.check('leEeetcode', 'leetcode')
        self.check('abBAcC', '')


if __name__ == '__main__':
    unittest.main()
