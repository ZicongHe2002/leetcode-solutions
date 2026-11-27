from itertools import product
import unittest

from python.p0680_valid_palindrome_ii import Solution


def every_deletion_reference(value):
    if value == value[::-1]:
        return True
    for index in range(len(value)):
        candidate = value[:index] + value[index + 1:]
        if candidate == candidate[::-1]:
            return True
    return False


class OneDeletionPalindromeTests(unittest.TestCase):
    def check(self, value, expected=None):
        if expected is None:
            expected = every_deletion_reference(value)
        result = Solution().validPalindrome(value)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_strings_against_every_deleted_position(self):
        checks = 0
        for size in range(1, 9):
            for value in product('abc', repeat=size):
                self.check(''.join(value))
                checks += 1
        self.assertEqual(checks, 9840)

    def test_maximum_length_and_each_deletion_branch(self):
        self.check('a' * 100000, True)
        self.check('b' + 'a' * 99999, True)
        self.check('a' * 99999 + 'b', True)
        self.check('a' * 49999 + 'bc' + 'a' * 49999, True)
        self.check('a' * 49999 + 'bc' + 'a' * 49998 + 'd', False)
        self.check('abc', False)
        self.check('abca', True)
        self.check('deeee', True)


if __name__ == '__main__':
    unittest.main()
