from functools import lru_cache
from itertools import product
import unittest

from python.p0383_ransom_note import Solution


def assign_source_positions(target, source):
    @lru_cache(None)
    def assign(index, used):
        if index == len(target):
            return True
        return any(letter == target[index] and not (used >> position & 1)
                   and assign(index + 1, used | (1 << position))
                   for position, letter in enumerate(source))
    return assign(0, 0)


class RansomSourcePositionTests(unittest.TestCase):
    def check(self, target, source, expected=None):
        if expected is None:
            expected = assign_source_positions(target, source)
        result = Solution().canConstruct(target, source)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_nonempty_string_pairs_against_source_assignments(self):
        texts = [''.join(letters) for size in range(1, 6) for letters in product('ab', repeat=size)]
        checks = 0
        for target in texts:
            for source in texts:
                self.check(target, source)
                checks += 1
        self.assertEqual((len(texts), checks), (62, 3844))

    def test_maximum_lengths_exact_budget_missing_letter_and_order(self):
        self.check('a' * 100000, 'a' * 100000, True)
        self.check('a' * 99999 + 'b', 'a' * 100000, False)
        self.check('a' * 100000, 'a' * 99999, False)
        self.check('abcde' * 20000, ''.join(letter * 20000 for letter in 'edcba'), True)


if __name__ == '__main__':
    unittest.main()
