import unittest
from itertools import product

from python.p0097_interleaving_string import Solution


def explicit_interleavings(first, second):
    if not first:
        return {second}
    if not second:
        return {first}
    return ({first[0] + tail for tail in explicit_interleavings(first[1:], second)} |
            {second[0] + tail for tail in explicit_interleavings(first, second[1:])})


class InterleavingTests(unittest.TestCase):
    def check(self, first, second, target, expected):
        result = Solution().isInterleave(first, second, target)
        self.assertIs(type(result), bool)
        self.assertEqual(result, expected)

    def test_all_small_sources_and_targets_against_explicit_merges(self):
        words = [''.join(chars) for size in range(4) for chars in product('ab', repeat=size)]
        pairs = checks = 0
        for first in words:
            for second in words:
                pairs += 1
                possible = explicit_interleavings(first, second)
                for letters in product('ab', repeat=len(first) + len(second)):
                    target = ''.join(letters)
                    self.check(first, second, target, target in possible)
                    checks += 1
        self.assertEqual((pairs, checks), (225, 7225))

    def test_maximum_lengths_order_empty_and_length_mismatch(self):
        self.check('a' * 100, 'a' * 100, 'a' * 200, True)
        self.check('a' * 100, 'b' * 100, 'a' * 99 + 'b' * 100 + 'a', True)
        self.check('a' * 99 + 'b', 'a' * 100, 'b' + 'a' * 199, False)
        self.check('a' * 99 + 'b', 'a' * 100, 'a' * 199 + 'b', True)
        self.check('', '', '', True)
        self.check('a', 'b', 'a', False)
        self.check('', 'abc', 'abc', True)


if __name__ == '__main__':
    unittest.main()
