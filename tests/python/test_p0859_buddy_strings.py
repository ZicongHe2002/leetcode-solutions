from itertools import product
import unittest

from python.p0859_buddy_strings import Solution


def all_distinct_index_swaps(value, goal):
    for first in range(len(value)):
        for second in range(first + 1, len(value)):
            chars = list(value)
            chars[first], chars[second] = chars[second], chars[first]
            if ''.join(chars) == goal:
                return True
    return False


class ExactlyOneSwapTests(unittest.TestCase):
    def check(self, value, goal, expected=None):
        if expected is None:
            expected = all_distinct_index_swaps(value, goal)
        result = Solution().buddyStrings(value, goal)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_equal_length_pairs_against_actual_swaps(self):
        checks = 0
        for size in range(1, 6):
            strings = [''.join(chars) for chars in product('abc', repeat=size)]
            for value in strings:
                for goal in strings:
                    self.check(value, goal)
                    checks += 1
        self.assertEqual(checks, 66429)

    def test_maximum_length_required_swap_and_different_lengths(self):
        self.check('a' * 20000, 'a' * 20000, True)
        self.check('a' + 'c' * 19998 + 'b', 'b' + 'c' * 19998 + 'a', True)
        self.check('a' * 20000, 'a' * 19999 + 'b', False)
        self.check('ab', 'ab', False)
        self.check('aa', 'aa', True)
        self.check('a', 'a', False)
        self.check('ab', 'aba', False)
        self.check('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', False)


if __name__ == '__main__':
    unittest.main()
