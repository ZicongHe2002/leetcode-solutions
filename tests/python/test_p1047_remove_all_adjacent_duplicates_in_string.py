from functools import lru_cache
from itertools import product
import unittest

from python.p1047_remove_all_adjacent_duplicates_in_string import Solution


@lru_cache(None)
def every_terminal_text(text):
    outcomes = set()
    for index in range(len(text) - 1):
        if text[index] == text[index + 1]:
            outcomes.update(every_terminal_text(text[:index] + text[index + 2:]))
    return frozenset(outcomes or (text,))


class AdjacentPairDeletionTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().removeDuplicates(text)
        self.assertIs(type(result), str)
        if expected is None:
            self.assertEqual(every_terminal_text(text), frozenset((result,)))
        else:
            self.assertEqual(result, expected)

    def test_all_small_texts_against_every_legal_rewrite_order(self):
        checks = 0
        for size in range(1, 8):
            for letters in product('abc', repeat=size):
                self.check(''.join(letters))
                checks += 1
        self.assertEqual(checks, 3279)

    def test_maximum_length_no_deletion_and_cascading_deletions(self):
        self.check('a' * 100000, '')
        self.check('ab' * 50000, 'ab' * 50000)
        self.check('a' * 49999 + 'bb' + 'a' * 49999, '')
        self.check('abbaca', 'ca')
        self.check('azxxzy', 'ay')


if __name__ == '__main__':
    unittest.main()
