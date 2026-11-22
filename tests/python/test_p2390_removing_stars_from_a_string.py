from functools import lru_cache
from itertools import product
import unittest

from python.p2390_removing_stars_from_a_string import Solution


def completable(text):
    available = 0
    for letter in text:
        available += -1 if letter == '*' else 1
        if available < 0:
            return False
    return True


@lru_cache(None)
def all_star_deletion_endings(text):
    if '*' not in text:
        return frozenset((text,))
    outcomes = set()
    for star, letter in enumerate(text):
        if letter != '*':
            continue
        previous = star - 1
        while previous >= 0 and text[previous] == '*':
            previous -= 1
        if previous >= 0:
            reduced = text[:previous] + text[previous + 1:star] + text[star + 1:]
            outcomes.update(all_star_deletion_endings(reduced))
    return frozenset(outcomes)


class StarPredecessorDeletionTests(unittest.TestCase):
    def check(self, text, expected=None):
        result = Solution().removeStars(text)
        self.assertIs(type(result), str)
        if expected is None:
            self.assertEqual(all_star_deletion_endings(text), frozenset((result,)))
        else:
            self.assertEqual(result, expected)

    def test_every_small_completable_input_against_all_star_choices(self):
        checks = 0
        for size in range(1, 9):
            for letters in product('ab*', repeat=size):
                text = ''.join(letters)
                if completable(text):
                    self.check(text)
                    checks += 1
        self.assertEqual(checks, 5352)

    def test_maximum_length_total_removal_and_surviving_suffix(self):
        self.check('a' * 100000, 'a' * 100000)
        self.check('a' * 50000 + '*' * 50000, '')
        self.check('ab**' * 25000, '')
        self.check('a*' * 49999 + 'bc', 'bc')
        self.check('leet**cod*e', 'lecoe')
        self.check('erase*****', '')


if __name__ == '__main__':
    unittest.main()
